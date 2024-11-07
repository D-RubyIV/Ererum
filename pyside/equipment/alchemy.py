from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
# Tạo engine kết nối với cơ sở dữ liệu
engine = create_engine(
    f"sqlite+pysqlite:///{settings.DBPATH}",
    pool_size=10,  # Số lượng kết nối tối đa trong pool
    max_overflow=20,  # Số kết nối vượt quá pool_size có thể được tạo thêm
    pool_timeout=30,  # Thời gian tối đa chờ đợi khi lấy kết nối từ pool
    pool_recycle=3600,  # Thời gian làm mới kết nối sau mỗi 3600 giây (1 giờ)
    echo=True  # Hiển thị các câu lệnh SQL trên console (debugging)
)
print(f"DB: ", settings.DBPATH)

# Cấu hình session với các thuộc tính
SessionLocal = sessionmaker(
    autocommit=False,   # Không tự động commit
    autoflush=True,     # Tự động flush thay đổi vào DB trước khi thực hiện truy vấn
    bind=engine         # Gắn kết session với engine đã tạo
)

# Hàm để tạo session
def get_session():
    db = SessionLocal()  # Tạo một phiên làm việc (session) mới
    try:
        yield db  # Trả về session để thao tác với cơ sở dữ liệu
    finally:
        db.close()  # Đảm bảo đóng session sau khi sử dụng
