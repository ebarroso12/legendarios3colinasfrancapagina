import re,sys,base64,io
from PIL import Image
src,out=sys.argv[1],sys.argv[2]
h=open(src,encoding='utf-8').read()
IG='ig/';OLD='dl/imgs/'
def enc(path,box,maxw=1400):
    im=Image.open(path).convert('RGB');W,H=im.size
    im=im.crop((int(box[0]*W),int(box[1]*H),int(box[2]*W),int(box[3]*H)))
    if im.width>maxw: im=im.resize((maxw,int(im.height*maxw/im.width)),Image.LANCZOS)
    b=io.BytesIO();im.save(b,'JPEG',quality=82,optimize=True,progressive=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
WIDE=(0,0,.915,.775)  # remove carimbo "#TOP" (inferior esq.) e logo (sup. dir.)
gal=[ (IG+'emb_Deh-dWqnztN_0.jpg',(.03,0,.905,.775),'Irmandade'),
      (OLD+'img3.jpeg',(0,.1,.86,.84),'Rendição'),
      (OLD+'img4.jpeg',WIDE,'Confronto'),
      (IG+'emb_Deh-dWqnztN_3.jpg',(0,0,.915,.775),'Compromisso'),
      (OLD+'img2.jpeg',WIDE,'Desfrute o Caminho'),
      (OLD+'img6.jpeg',WIDE,'Transformação')]
fam=[ (OLD+'img8.jpeg',WIDE,'Família aguardando'),
      (IG+'emb_DXorFOnCIH7_0.jpg',(0,.04,1,.72),'Criança com cartaz de boas-vindas'),
      (OLD+'img10.jpeg',WIDE,'Família com cartaz')]
# galeria
items=re.findall(r'<div class="(?:gal-[a-f] gal-item|gal-item gal-[a-f])"><img src="data:[^"]+" alt="[^"]*" loading="lazy"><div class="gal-caption">[^<]*</div></div>',h)
assert len(items)==6,len(items)
for it,(p,box,cap) in zip(items,gal):
    cls=re.match(r'<div class="([^"]+)"',it).group(1)
    h=h.replace(it,f'<div class="{cls}"><img src="{enc(p,box)}" alt="{cap}" loading="lazy"><div class="gal-caption">{cap}</div></div>',1)
items=re.findall(r'<div class="fam-item"><img src="data:[^"]+" alt="[^"]*" loading="lazy"></div>',h)
assert len(items)==3,len(items)
for it,(p,box,alt) in zip(items,fam):
    h=h.replace(it,f'<div class="fam-item"><img src="{enc(p,box,1000)}" alt="{alt}" loading="lazy"></div>',1)
h=h.replace('alt="Rendição" loading','alt="Rendição" style="object-position:center 22%" loading',1)
open(out,'w',encoding='utf-8').write(h);print('ok',len(h))
