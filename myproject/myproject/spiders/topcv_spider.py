from urllib.parse import parse_qs, urlparse
import scrapy
from scrapy_playwright.page import PageMethod
from myproject.items import JobItem

class TopcvSpider(scrapy.Spider):
    name= "topcv"
    base_url= "https://www.topcv.vn/tim-viec-lam-tester"
    start_page= 1
    async def start(self):
        url=f"{self.base_url}?page={self.start_page}"
        yield self.make_request(url, self.start_page)
    def make_request(self, url, page_num):
        return scrapy.Request(
            url=url,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod(
                        "add_init_script",
                        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
                    ),
                    PageMethod("wait_for_selector", "div.job-item-search-result", timeout=30000)
                ]
            },
            callback=self.parse,
            cb_kwargs={"requested_page": page_num},
            dont_filter=True # bật tự có thể ghi log ra ngoài
        )
    def parse(self, response, requested_page):
        parsed_url= urlparse(response.url)
        query_params= parse_qs(parsed_url.query)
        actual_page=int(query_params.get("page", ["1"])[0])
        if actual_page!=requested_page:
            self.logger.info(
                f"Đang là page max từ page={requested_page} nhưng bị redirect về page={actual_page} - DỪng cào"
            )
            return
        job_cards = response.css("div.job-item-search-result")
        self.logger.info(f"--> Trang {requested_page}: tìm thấy {len(job_cards)} công việc")
        for card in job_cards:
            yield JobItem(
                job_id=card.css("::attr(data-job-id)").get(default="N/A").strip(),
                trang=requested_page,
                tieu_de=card.css("h3.title a span::text").get(default="N/A").strip(),
                cong_ty=card.css("a.company span.company-name::text").get(default="N/A").strip(),
                muc_luong=card.css("label.salary span::text").get(default="Thoả thuận").strip(),
                dia_diem=card.css("span.city-text::text").get(default="N/A").strip(),
                kinh_nghiem=card.css("label.exp span::text").get(default="Không yêu cầu").strip(),
                link_chi_tiet=response.urljoin(card.css("h3.title a::attr(href)").get(default=""))
            )
        next_page=requested_page+1
        next_url= f"{self.base_url}?page={next_page}"
        yield self.make_request(next_url, next_page)

    def parse_detail (self, response, item: JobItem):
        self.logger.info(f"Đang lấy jobid : {item.job_id}")

