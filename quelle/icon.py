from PIL import Image,ImageDraw,ImageFont,ImageFilter
import sys
def make(size,out):
    k=4; W=size*k; im=Image.new('RGB',(W,W)); d=ImageDraw.Draw(im)
    top=(52,104,196); bot=(25,62,140)
    for y in range(W):
        t=y/W; d.line([(0,y),(W,y)],fill=tuple(int(top[i]+(bot[i]-top[i])*t) for i in range(3)))
    step=int(W/18)
    for x in range(0,W,step): d.line([(x,0),(x,W)],fill=(62,114,204),width=k)
    for y in range(0,W,step): d.line([(0,y),(W,y)],fill=(62,114,204),width=k)
    band=int(W*0.18); y0=W-band
    d.rectangle([0,y0-int(W*0.02),W,y0],fill=(15,30,70))
    cols=[(0,35,149),(255,255,255),(237,41,57)]
    for i,c in enumerate(cols): d.rectangle([i*W//3,y0,(i+1)*W//3,W],fill=c)
    f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',int(W*0.64))
    txt='ç'; bb=d.textbbox((0,0),txt,font=f); w=bb[2]-bb[0]; h=bb[3]-bb[1]
    x=(W-w)/2-bb[0]; y=(y0-int(W*0.02)-h)/2-bb[1]
    sh=Image.new('L',(W,W),0); ImageDraw.Draw(sh).text((x+k*3,y+k*4),txt,font=f,fill=110); sh=sh.filter(ImageFilter.GaussianBlur(k*4))
    im.paste((10,25,60),mask=sh)
    d=ImageDraw.Draw(im); d.text((x,y),txt,font=f,fill=(255,255,255))
    im.resize((size,size),Image.LANCZOS).save(out)
make(180,sys.argv[1]+'/fr180.png'); make(192,sys.argv[1]+'/fr192.png')
