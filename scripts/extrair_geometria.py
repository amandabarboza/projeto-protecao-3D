import sys, ezdxf, json, re
from ezdxf import path
doc=ezdxf.readfile(sys.argv[1]); m=doc.modelspace()
walls=[]
xs=[];ys=[]
for h in m.query("HATCH"):
    if h.dxf.layer!="A-WALL-PATT": continue
    for p in path.from_hatch(h):
        pts=[(q.x,q.y) for q in p.flattening(0.01)]
        if len(pts)>1 and pts[0]==pts[-1]: pts=pts[:-1]
        if len(pts)>=3:
            walls.append(pts); xs+= [a for a,b in pts]; ys+=[b for a,b in pts]
ox=(min(xs)+max(xs))/2; oy=(min(ys)+max(ys))/2
T=lambda x,y:[round(x-ox,3),round(y-oy,3)]
plat=[]
for e in m.query("LINE"):
    if e.dxf.layer=="0":
        plat.append(T(e.dxf.start.x,e.dxf.start.y)+T(e.dxf.end.x,e.dxf.end.y))
labels=[]
for e in m.query("MTEXT"):
    if e.dxf.layer=="A-AREA-IDEN":
        t=e.plain_text().strip()
        if t and not t.startswith("A="): labels.append({"t":t,"p":T(e.dxf.insert.x,e.dxf.insert.y)})
out={"origin":[round(ox,3),round(oy,3)],"walls":[[T(x,y) for x,y in w] for w in walls],"platform":plat,"labels":labels,
     "bounds":[round(min(xs)-ox,3),round(min(ys)-oy,3),round(max(xs)-ox,3),round(max(ys)-oy,3)]}
json.dump(out,open(sys.argv[2],"w",encoding="utf8"),ensure_ascii=False,separators=(",",":"))
print("walls",len(walls),"plat",len(plat),"labels",len(labels),"origin",ox,oy,out["bounds"])
