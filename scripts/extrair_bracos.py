import json, math, sys
G=json.load(open(sys.argv[1],encoding="utf8")); B=G["bounds"]
def inbox(x,y,m=0.15): return B[0]-m<=x<=B[2]+m and B[1]-m<=y<=B[3]+m
br=[]
for x1,y1,x2,y2 in G["platform"]:
    ln=math.hypot(x2-x1,y2-y1)
    if not 2.95<=ln<=3.05: continue
    a,b=(x1,y1),(x2,y2)
    if inbox(*a)==inbox(*b): continue
    p,q=(a,b) if inbox(*a) else (b,a)
    br.append([round(p[0],3),round(p[1],3),round(math.degrees(math.atan2(q[1]-p[1],q[0]-p[0])))])
br=sorted({tuple(r) for r in br})
fac=[[-13.1,7.025],[-7.55,7.025],[-7.55,7.425],[7.55,7.425],[7.55,7.025],[13.1,7.025],[13.1,-6.975],[3.2,-6.975],[3.2,-7.425],[0.4,-7.425],[0.4,-5.425],[-3.05,-5.425],[-3.05,-6.975],[-13.1,-6.975]]
json.dump({"bracos":br,"fachada":fac},open(sys.argv[2],"w"),separators=(",",":"))
print(len(br))
