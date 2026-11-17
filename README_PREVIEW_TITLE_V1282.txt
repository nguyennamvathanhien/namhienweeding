AAC Wedding V12.8.2 + taoten.html – Messenger preview title update

Nền bản: AAC_Wedding_V12.8.2_TaoTen_HeroWebP_Messenger_Fix.zip

Mục tiêu:
- Dòng tiêu đề link Facebook/Messenger: Thiệp cưới Nguyễn Nam và Thân Hiền
- Dòng mô tả link: Trân trọng kính mời [tên khách] tới chung vui cùng chúng mình vào ...
- Thời gian lấy từ event=, tên khách lấy từ guest=.
- Giữ ảnh xem trước hero.webp (1600 x 1021); không đổi ảnh web.

Đã cập nhật đồng nhất tại ba nơi:
- index.html: title, og:title, twitter:title, description mặc định và JavaScript.
- nhagai.html: tương tự.
- functions/_middleware.js: HTML trả về phía Cloudflare Pages theo từng link khách mời.

Tất cả file còn lại của bản nguồn được giữ nguyên, bao gồm taoten.html, ảnh, âm thanh, thư mục optimized và cấu hình Google Sheets.

Cập nhật bằng GitHub Desktop:
1. Giải nén ZIP vào thư mục repository; ghi đè file trùng tên.
2. Phải có functions/_middleware.js và _routes.json trong thư mục gốc repository.
3. Commit rồi Push origin; kiểm tra Cloudflare Pages deployment thành công.
4. Mở Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/
   Dán một URL khách mời cụ thể, bấm Debug/Scrape Again; sau đó gửi tin nhắn MỚI.

Lưu ý: Messenger Web và Messenger App có thể có cách hiển thị preview khác nhau.
Việc đổi og:title không thể ép giao diện Messenger Web phải hiển thị ảnh nếu nền tảng đang ẩn ảnh đó.
