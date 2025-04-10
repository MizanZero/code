s = "a1b2c3d4e"
ns = []
for l in s:
    if not l.isdigit(): ns.append(l)
    else: ns.pop()

print(ns) 