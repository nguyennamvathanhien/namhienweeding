from pathlib import Path
import re, tinycss2
base=Path('/mnt/data/AAC_V12_8_work')
css_update='''
/* AAC Wedding V12.8 · 1 mobile phone card on all devices
   The same lightweight mobile design is used on iPhone, Android, iPad and desktop. */
:root { --aac-phone-width: 440px; }
body {
  background:radial-gradient(ellipse at 20% 6%,#ffe9f4 0%,transparent 53%),
             radial-gradient(ellipse at 83% 40%,#f7e3f2 0%,transparent 58%),
             linear-gradient(150deg,#fff0f7,#f9e9f4 52%,#fff3f8)!important;
}
#app {
  width:100%!important;
  max-width:var(--aac-phone-width)!important;
  margin-inline:auto!important;
  container-type:inline-size;
  box-shadow:0 0 38px rgba(164,99,141,.16),0 0 0 1px rgba(235,193,213,.32)!important;
}
#app::before{max-width:var(--aac-phone-width)!important;}
#bar,#live {width:min(100%,var(--aac-phone-width))!important;max-width:var(--aac-phone-width)!important;left:50%!important;transform:translateX(-50%)!important;}
#museumDoor {width:min(100%,var(--aac-phone-width))!important;max-width:var(--aac-phone-width)!important;left:50%!important;right:auto!important;transform:translateX(-50%)!important;}
#petalLayer,#heartLayer,.floating-heart-balloons {
  width:min(100%,var(--aac-phone-width))!important;
  left:50%!important;
  right:auto!important;
  transform:translateX(-50%)!important;
  overflow:hidden!important;
}
@media (min-width:600px){
  #app {border-left:1px solid rgba(255,255,255,.8);border-right:1px solid rgba(255,255,255,.8)}
  #bar {box-shadow:0 -8px 26px rgba(171,102,143,.08)}
  #museumDoor .door-couple{font-size:clamp(2.7rem,8cqw,3.4rem)!important}
  #museumDoor .door-intro.cute-door-intro{width:min(100%,345px)!important}
}
/* Chapter 04: title and chapter label float in a translucent cloud at the top
   of the original full 2:3 photo. Only the short story note crosses its foot. */
#journeyRoom .j-item:not(.j-item--final) .j-image {position:relative!important;isolation:isolate!important;}
#journeyRoom .j-item:not(.j-item--final) .j-photo-caption{display:none!important}
#journeyRoom .j-item:not(.j-item--final) .j-visual-heading{
  position:absolute;top:clamp(17px,5cqw,27px);left:clamp(15px,4.5cqw,25px);
  z-index:7;max-width:calc(100% - 44px);width:max-content;
  padding:.7rem 1.05rem .8rem;
  border-radius:20px 24px 22px 8px;
  border:1px solid rgba(255,255,255,.9);
  background:linear-gradient(135deg,rgba(255,251,253,.84),rgba(255,244,250,.56));
  box-shadow:0 6px 22px rgba(103,66,97,.09);
  -webkit-backdrop-filter:blur(4px);backdrop-filter:blur(4px);
  pointer-events:none;
}
#journeyRoom .j-visual-heading .j-year{font-size:.55rem!important;letter-spacing:.05em!important;white-space:normal!important;color:#b77b9e!important}
#journeyRoom .j-visual-heading .j-title{
  font-family:var(--rounded)!important;font-size:clamp(1.85rem,7cqw,2.3rem)!important;
  line-height:1.03!important;font-weight:500!important;
  color:#675570!important;margin:.32rem 0 0!important;
  text-shadow:0 2px 8px rgba(255,255,255,.65)!important;
}
#journeyRoom .j-visual-heading .j-title em{color:#e08eaf!important;}
#journeyRoom .j-item:not(.j-item--final) .j-card,
#journeyRoom .j-item--right:not(.j-item--final) .j-card{
  position:relative!important;z-index:8!important;
  width:calc(100% - 42px)!important;
  margin:-54px 0 0 40px!important;
  padding:.95rem 1rem 1.05rem!important;
  border:2px solid rgba(255,255,255,.98)!important;
  border-radius:25px!important;
  background:linear-gradient(145deg,rgba(255,252,254,.83),rgba(255,240,249,.78))!important;
  -webkit-backdrop-filter:blur(5px);backdrop-filter:blur(5px);
  box-shadow:0 13px 26px rgba(148,103,139,.14)!important;
  text-align:left!important;
}
#journeyRoom .j-item:not(.j-item--final) .j-card .j-story-rule{width:54px!important;margin:.22rem 0 .55rem!important;height:3px!important}
#journeyRoom .j-item:not(.j-item--final) .j-card .j-desc{
  font-size:clamp(.9rem,3.2cqw,1rem)!important;line-height:1.65!important;
  color:#7f7085!important;max-width:none!important;margin:0!important;
}
#journeyRoom .j-item:not(.j-item--final) .j-card .j-script-note{
  font-size:clamp(1.45rem,5cqw,1.85rem)!important;
  margin-top:.48rem!important;color:#d984ae!important;
}
#journeyRoom .j-item:not(.j-item--final) .j-card .j-number{display:none!important}
@media (max-width:355px){
  #journeyRoom .j-item:not(.j-item--final) .j-card{width:calc(100% - 35px)!important;margin-left:34px!important}
  #journeyRoom .j-visual-heading .j-title{font-size:1.75rem!important}
}
/* Chapter 05: 9 and 10 are the final two matching portrait cards in one row. */
#exhibitRoom .archive-tiles{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:clamp(.62rem,2cqw,.9rem)!important;align-items:stretch!important}
#exhibitRoom .archive-tiles>.archive-tile:nth-child(9),
#exhibitRoom .archive-tiles>.archive-tile:nth-child(10){
  grid-column:auto!important;grid-row:auto!important;
  width:100%!important;max-width:none!important;min-width:0!important;
  margin:0!important;justify-self:stretch!important;
}
#exhibitRoom .archive-tiles>.archive-tile:nth-child(9) .archive-media,
#exhibitRoom .archive-tiles>.archive-tile:nth-child(10) .archive-media{
  aspect-ratio:2/3!important;height:auto!important;
}
/* Keep readable, functional controls at 320-440px without desktop-specific scaling. */
#app,#bar,#live,#museumDoor{box-sizing:border-box}
@media (prefers-reduced-motion: reduce){
  #journeyRoom .j-visual-heading{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}
}
'''

for page in ('index.html','nhagai.html'):
    file=base/page
    doc=file.read_text(encoding='utf-8')
    head, tail=doc.split('<style>',1)
    style, rest=tail.split('</style>',1)
    nodes=tinycss2.parse_stylesheet(style,skip_comments=False,skip_whitespace=False)
    result=[]
    removed=[]; forced=[]
    for n in nodes:
        if n.type=='at-rule' and n.lower_at_keyword=='media':
            condition=tinycss2.serialize(n.prelude).strip()
            if re.search(r'\(\s*min-width\s*:\s*(?:600|650|700|750|800|900|1000|1100|1200)\s*px\s*\)',condition):
                removed.append(condition)
                continue
            if re.fullmatch(r'\(\s*max-width\s*:\s*(?:599|799)\s*px\s*\)',condition):
                n.prelude=tinycss2.parse_component_value_list('(min-width:0px)')
                forced.append(condition)
        result.append(n)
    style=tinycss2.serialize(result)
    # In text-only css: use phone container query units for viewport-relative dimensions
    # inside phone frame; for elements outside the frame the fallback is viewport sizing.
    style=re.sub(r'(?<=\d)vw\b','cqw',style)
    style=style+'\n'+css_update
    # Move the real heading from the story card onto the picture, keeping content/semantics intact
    before, after=rest.split('  <section id="journeyRoom"',1)
    journey, afterjourney=after.split('  <section id="exhibitRoom"',1)
    ptrn=re.compile(r'(<figure class="j-image">.*?<img.*?>)(\s*<figcaption class="j-photo-caption">.*?</figcaption>\s*</figure>\s*<div class="j-card">\s*<div class="j-number".*?</div>)\s*(<div class="j-year">.*?</div>\s*<h3 class="j-title">.*?</h3>)',re.S)
    count=0
    def shift(m):
        nonlocal_dict['count']+=1
        return m.group(1)+'\n          <div class="j-visual-heading">'+m.group(3)+'</div>'+m.group(2)
    nonlocal_dict={'count':0}
    journey=ptrn.sub(shift,journey)
    assert nonlocal_dict['count']==3,(page,nonlocal_dict['count'])
    # robot counter initial state matches gallery count
    afterjourney=afterjourney.replace('id="robotCounter">01 / 09<','id="robotCounter">01 / 10<')
    rest=before+'  <section id="journeyRoom"'+journey+'  <section id="exhibitRoom"'+afterjourney
    doc=head+'<style>'+style+'</style>'+rest
    # correct version metadata, leave all functional scripts and image filenames unchanged
    doc=re.sub(r'(<meta name="aac-build" content=")[^"]+',r'\g<1>V12.8-ONE-PHONE-10-PHOTOS-'+('NHATRAI' if page=='index.html' else 'NHAGAI'),doc,1)
    file.write_text(doc,encoding='utf-8')
    print(page,'media removed',len(removed),'mobile media universal',len(forced),'shifted heading',nonlocal_dict['count'],'bytes',len(doc))

(base/'README_V12.8.txt').write_text('''AAC Wedding V12.8 – One Phone Frame / Story Heading Overlay / 10 Portraits

- index.html: Nhà trai; nhagai.html: Nhà gái.
- Máy tính và iPad: chỉ một khung giao diện điện thoại ~440px ở chính giữa, nền ngoài màu hồng; không có bố cục máy tính riêng.
- Điện thoại: chiều rộng theo màn hình thực tế tới tối đa 440px, tiếp tục sử dụng CSS cho máy nhỏ.
- Chương 04: tiêu đề và nhãn câu chuyện đặt ở phía trên ảnh trong lớp màu hồng trắng mờ. Khối lời kể tiếp tục chèn nhẹ lên phần dưới ảnh, giảm chiều cao che ảnh.
- Chương 05: ảnh 09 và 10 trong cùng một hàng hai cột, đều là ảnh dọc 2:3. Ảnh 10 lấy từ 17.webp; robot cập nhật 10 ảnh.
- Giữ các chức năng Google Sheets, RSVP, event=, guest=, nhạc nền, thư mời, lịch và QR. Không thay đổi hình gốc.
- CSS loại bỏ các quy tắc chỉ dành cho desktop/iPad và dùng một bộ mobile layout để hạn chế xung đột.
- V12.7 vẫn được giữ riêng, không ghi đè.

Cách dùng: tải/giải nén ZIP, upload nguyên các tệp cùng cấp lên Cloudflare Pages (kể cả thư mục optimized/).
''',encoding='utf-8')
