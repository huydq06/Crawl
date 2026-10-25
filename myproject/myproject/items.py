from dataclasses import dataclass

@dataclass
class JobItem:
    # --- Từ trang danh sách ---
    job_id: str = "N/A"
    trang: int = 1
    tieu_de: str = "N/A"
    cong_ty: str = "N/A"
    muc_luong: str = "N/A"
    dia_diem: str = "N/A"
    kinh_nghiem: str = "N/A"
    link_chi_tiet: str = "N/A"

    # --- Từ trang chi tiết ---
    mo_ta: str = "N/A"
    yeu_cau: str = "N/A"
    quyen_loi: str = "N/A"
    kien_thuc_nganh: str = "N/A"
    ky_nang_can_co: str = "N/A"
    ky_nang_nen_co: str = "N/A"
    dia_diem_chi_tiet: str = "N/A"
    thoi_gian_lam_viec: str = "N/A"
    han_nop: str = "N/A"
    cap_bac: str = "N/A"
    hoc_van: str = "N/A"
    so_luong_tuyen: str = "N/A"
    hinh_thuc_lam_viec: str = "N/A"
    loai_hinh_lam_viec: str = "N/A"
    quy_mo_cong_ty: str = "N/A"
    dia_chi_cong_ty: str = "N/A"
    nganh_nghe_cong_ty: str = "N/A"