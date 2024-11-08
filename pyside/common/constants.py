import os

ROOT_PATH = os.getcwd()


class Constants:
    TG_PATH = os.path.join(ROOT_PATH, "storage\\session")

    # TG_TABLE
    lbTGTableFile = "Tệp"
    lbTGTableUsername = "Người dùng"
    lbTGTableFirstname = "Tên"
    lbTGTableLastname = "Họ"
    lbTGTablePhone = "Số điện thoại"
    lbTGTableProxy = "Proxy"
    lbTGTableAction = "Hành động"
    lbTGTableStatus = "Trạng thái"
    lbTGTableWasOnline = "Đã trực tuyến"
