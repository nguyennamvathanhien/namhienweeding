AAC WEDDING V12.8.2 + TAOTEN.HTML
=================================

GIỮ LẠI V12.8.2
- index.html = Nhà trai (29/11/2026 lúc 10:00)
- nhagai.html = Nhà gái (28/11/2026 lúc 17:00 hoặc 29/11/2026 lúc 10:00)
- Giao diện, cánh cửa mở, hình ảnh Chương 4, bộ sưu tập 10 ảnh, RSVP, Google Sheets đều từ V12.8.2.
- Chỉ điều chỉnh chuỗi meta description ở 2 file HTML để khớp câu mô tả khi có event/guest.
- Không sử dụng giao diện/nút chỉnh tên của V12.8.3.

FILE BỔ SUNG
- taoten.html: Nhập tên và tạo nhiều link (tự động lưu trên trình duyệt), chỉnh/xóa, sao chép từng link,
  sao chép bảng tên và link để dán Excel, xuất CSV sao lưu.
- functions/_middleware.js: Cloudflare Pages Function tạo nội dung meta name=description,
  og:description, og:title, og:url, og:image riêng cho URL ?event=...&guest=...
- _routes.json: chỉ chạy Function trên trang Nhà trai/Nhà gái; file ảnh, nhạc, trang tạo tên là tệp tĩnh.
- share-hero-v1282.jpg: ảnh xem trước Messenger (JPEG 1200x630 tạo từ hero.webp gốc).

CÁCH TRIỂN KHAI QUA GITHUB DESKTOP + CLOUDFLARE PAGES
1. Giải nén ZIP này, mở thư mục code GitHub bằng Repository > Show in Explorer.
2. Sao chép index.html, nhagai.html, taoten.html, functions/, _routes.json,
   share-hero-v1282.jpg và các file website vào GỐC thư mục repository.
   Nhớ đảm bảo functions/_middleware.js không ở dưới một thư mục lồng bên trong!
3. Trở lại GitHub Desktop > Changes > Commit to main > Push origin.
4. Kiểm tra Cloudflare Pages > Deployments đã Success.
5. Mở https://TEN-TRANG-WEB-CUA-BAN/taoten.html để tạo link.
6. Khi nhập tên khách/nhà/ngày, bấm Tạo link & lưu danh sách; copy từng link
   hoặc nhấn Sao chép cho Excel / Xuất CSV.

VÍ DỤ
- Nhà trai: https://TEN-TRANG-WEB-CUA-BAN/index.html?event=29&guest=Nguyen+Van+A
- Nhà gái 28: https://TEN-TRANG-WEB-CUA-BAN/nhagai.html?event=28&guest=Tran+Thi+B
- Nhà gái 29: https://TEN-TRANG-WEB-CUA-BAN/nhagai.html?event=29&guest=Tran+Thi+B

META TRẢ VỀ CHO NHÀ TRAI
<meta name="description" content="Trân trọng kính mời Nguyễn Văn A tới chung vui cùng chúng mình vào sáng 10:00 ngày 29.11.2026 ♡"/>
<meta property="og:description" content="Trân trọng kính mời Nguyễn Văn A tới chung vui cùng chúng mình vào sáng 10:00 ngày 29.11.2026 ♡"/>

LƯU Ý QUAN TRỌNG
- Metadata theo tên khách PHẢI được trả về từ máy chủ; không thể giải quyết bằng JS tĩnh thuần túy.
  Cần triển khai trên Cloudflare Pages có Pages Functions hoạt động. GitHub Pages đơn lẻ không chạy Function này.
- Nếu thay đổi website Cloudflare, phải sửa Địa chỉ website trong taoten.html.
- Danh sách khách lưu bằng localStorage trên trình duyệt, KHÔNG đồng bộ giữa các máy.
  Hãy Xuất CSV để sao lưu trước khi xóa dữ liệu trình duyệt hoặc đổi máy.
- Đường link chứa tên khách mời có thể được người sở hữu đường link xem/copy.
- Facebook/Messenger có cache link preview. Sau khi Deploy thành công, dùng
  https://developers.facebook.com/tools/debug/ và nhấn Scrape Again trên link mới.
- Địa chỉ Cloudflare đang điền sẵn trong form là tên miền đọc được từ V12.8.2,
  chưa xác minh website thực tế của bạn có đang sử dụng tên miền này hay không.
