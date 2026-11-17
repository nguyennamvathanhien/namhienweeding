AAC Wedding V12.6 — Responsive Portrait & Performance Fix
Ngày cập nhật: 17/11/2026

TRANG SỬ DỤNG
- index.html : Nhà Trai.
- nhagai.html : Nhà Gái; event=28 (17:00, 28/11/2026) hoặc event=29 (10:00, 29/11/2026).
- Tham số guest= vẫn giữ nguyên và dùng sau event=, ví dụ:
  nhagai.html?event=28&guest=Nguyen%20Van%20A

THAY ĐỔI
1. Chương 03: thay ảnh tiệc cưới minh họa trên internet bằng họa tiết pastel nhẹ.
2. Chương 04: khung ảnh dọc 2:3, giữ trọn người, lời kể xuống dưới ảnh, bức ảnh cuối cũng dọc.
3. Chương 05: toàn bộ 9 ảnh kỷ niệm đều hiển thị dọc, bỏ ba ô ảnh ngang.
4. Desktop/iPad: khung ảnh hero/closing không cắt đầu, tay hay váy; giao diện RSVP và quà mừng gọn hơn.
5. Hiệu năng: bổ sung ảnh responsive trong optimized/ và giảm hiệu ứng GPU trên thiết bị yếu.
6. Đã giữ nguyên mã Google Apps Script, Google Sheets, QR, các URL đường đi và các chức năng thiệp.

TRIỂN KHAI
- Giải nén và upload TOÀN BỘ nội dung ZIP ở thư mục gốc của Cloudflare Pages/Netlify.
- Đừng bỏ thư mục optimized/: trình duyệt dùng ảnh nhẹ từ thư mục này.
- Ảnh số gốc (1.webp…18.webp, end.webp) được giữ nguyên để có thể thay ảnh sau này.
- Nếu bạn thay các ảnh gốc, hãy tạo lại ảnh optimized tương ứng hoặc xóa srcset trước khi triển khai,
  nếu không trình duyệt có thể vẫn hiển thị ảnh phiên bản nhẹ của tệp cũ.
- Kiểm tra bằng điện thoại sau khi deploy; nếu thấy bản cũ, dùng tải lại bỏ cache.

LƯU Ý KIỂM THỬ
- Đã kiểm tra trực tiếp bằng Chromium với các kích thước 390, 768, 1366 và 1920 px.
- Đã kiểm tra cú pháp toàn bộ JavaScript, ảnh tham chiếu và tràn chiều ngang.
- Lưu lời chúc thực tế trên Google Sheets không được gửi thử để tránh làm bẩn dữ liệu.
