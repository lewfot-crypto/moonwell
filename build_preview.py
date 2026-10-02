from pathlib import Path
import re,base64,mimetypes
root=Path(__file__).resolve().parent
s=(root/'index.html').read_text()
s=re.sub(r'<link[^>]+(?:apple-touch-icon|rel="icon"|rel="manifest")[^>]*>', '', s)
def embed(m):
 p=root/'assets'/m.group(1)
 if not p.is_file():raise FileNotFoundError(p)
 mime={'woff':'font/woff','webp':'image/webp'}.get(p.suffix[1:],mimetypes.guess_type(p.name)[0] or 'application/octet-stream')
 return 'data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()
s=re.sub(r'\./assets/([A-Za-z0-9_.-]+)',embed,s)
(root/'moonwell-preview.html').write_text(s)
print('Saved moonwell-preview.html')
