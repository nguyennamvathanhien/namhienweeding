AAC Wedding V12.8.2 + taoten.html — Sua preview Messenger dung hero.webp

Da sua:
- index.html va nhagai.html: Open Graph va Twitter dang dung dung anh /hero.webp?og=v1284; them type=image/webp, kich thuoc 1600x1021.
- functions/_middleware.js: khi Cloudflare Pages tra metadata theo guest=, giu anh hero.webp, khong thay sang file JPG.
- Thay query ?og=v1284 chi de Meta phan biet URL anh voi ban da cache. File thuc te van la hero.webp, khong tao anh thu hai.
- Giu lai toan bo ca hai thiệp, taoten.html, metadata ten guest, RSVP va Google Sheets.

Cach upload: unzip va copy toan bo vao thu muc repo GitHub Desktop, Commit, Push. Bao gom functions/ va _routes.json.

Sau khi Cloudflare Pages Deploy Success:
1. Mo URL https://namhienloveweddinginvitation.pages.dev/hero.webp?og=v1284 de kiem tra anh tai duoc.
2. Mo Facebook Sharing Debugger, dan link co event= va guest=; bam Debug, Scrape Again. Check og:image la .../hero.webp?og=v1284.
3. Gui tin nhan Messenger moi. Preview trong hop soan tin co the chua hien truoc khi gui va Meta co the xu ly WebP khong dong nhat. Neu Meta tu choi WebP, can dung JPG rieng cho preview; giu hero.webp lam anh hien thi tren trang.
