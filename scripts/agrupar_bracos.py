import json, math, sys
M=json.load(open(sys.argv[1]))
out=[]
for x,y,d in M["bracos"]:
    for o in out:
        if o[2]==d and math.hypot(o[0]-x,o[1]-y)<0.11:
            o[3].append((x,y)); break
    else: out.append([x,y,d,[(x,y)]])
br=[[round(sum(p[0] for p in o[3])/len(o[3]),3),round(sum(p[1] for p in o[3])/len(o[3]),3),o[2]] for o in out]
print(len(br), sorted(set(len(o[3]) for o in out)))
from collections import Counter; print(Counter(b[2] for b in br))
M["bracos"]=br; json.dump(M,open(sys.argv[1],"w"),separators=(",",":"))
