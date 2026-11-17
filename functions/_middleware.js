/**
 * AAC Wedding V12.8.2 – dynamic guest-specific metadata on Cloudflare Pages.
 * HTML layout and behavior remain V12.8.2; only sharing metadata is adjusted.
 * This function runs only on /, /index.html, /nhagai(.html) per _routes.json.
 * It works for guests as well as Messenger/Meta crawlers without JavaScript.
 */
const cleanGuest = value => (value || '')
  .normalize('NFC')
  .replace(/[<>\u0000-\u001f\u007f]/g, '')
  .replace(/[-_]+/g, ' ')
  .replace(/\s+/g, ' ')
  .trim()
  .slice(0, 100);

class MetaValue {
  constructor(value) { this.value = value; }
  element(el) { el.setAttribute('content', this.value); }
}
class TitleValue {
  constructor(value) { this.value = value; }
  element(el) { el.setInnerContent(this.value); }
}

export async function onRequest(context) {
  const request = context.request;
  if (request.method !== 'GET' && request.method !== 'HEAD') return context.next();

  const url = new URL(request.url);
  const path = url.pathname.replace(/\/+$/, '') || '/';
  const isBride = path.toLowerCase().endsWith('/nhagai') || path.toLowerCase().endsWith('/nhagai.html');
  const isGroom = path === '/' || path.toLowerCase().endsWith('/index.html') || path.toLowerCase().endsWith('/index');
  if (!isBride && !isGroom) return context.next();

  const response = await context.next();
  if (!response.ok || !((response.headers.get('content-type') || '').includes('text/html'))) return response;

  let candidate = url.searchParams.get('guest') || url.searchParams.get('Guest') || url.searchParams.get('guset') || '';
  const guest = cleanGuest(candidate);
  const event = isBride && url.searchParams.get('event') === '29' ? '29' : (isBride ? '28' : '29');
  const when = event === '28' ? 'vào lúc 17:00 ngày 28.11.2026' : 'vào sáng 10:00 ngày 29.11.2026';
  const address = guest || 'bạn';
  const title = 'Thiệp cưới Nguyễn Nam và Thân Hiền';
  const description = `Trân trọng kính mời ${address} tới chung vui cùng chúng mình ${when} ♡`;
  // A distinct canonical URL per invitation stops the different guests being merged.
  // Keep event before guest, just like the original invitation pages expect.
  const canonical = new URL(isBride ? '/nhagai.html' : '/', url.origin);
  canonical.searchParams.set('event', event);
  if (guest) canonical.searchParams.set('guest', guest);
  const image = new URL('/hero.webp?og=v1284', url.origin).href;

  const rewritten = new HTMLRewriter()
    .on('title', new TitleValue(title))
    .on('meta[name="description"]', new MetaValue(description))
    .on('meta[property="og:description"]', new MetaValue(description))
    .on('meta[name="twitter:description"]', new MetaValue(description))
    .on('meta[property="og:title"]', new MetaValue(title))
    .on('meta[name="twitter:title"]', new MetaValue(title))
    .on('meta[property="og:url"]', new MetaValue(canonical.href))
    .on('meta[property="og:image"]', new MetaValue(image))
    .on('meta[property="og:image:secure_url"]', new MetaValue(image))
    .on('meta[name="twitter:image"]', new MetaValue(image))
    .transform(response);

  // Per-invitation HTML is not publicly cacheable because it contains a guest's name.
  const headers = new Headers(rewritten.headers);
  headers.delete('Content-Length');
  headers.set('Cache-Control', 'private, no-store, max-age=0');
  headers.delete('ETag');
  return new Response(rewritten.body, { status: rewritten.status, statusText: rewritten.statusText, headers });
}
