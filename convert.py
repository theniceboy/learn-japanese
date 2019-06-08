from pykakasi import kakasi

fi = open("./sentences.txt", "r")
fo = open("./sentences.sep.txt", "w")

_k2h = kakasi()
_k2h.setMode('J', 'H')
k2h = _k2h.getConverter()

_h2a = kakasi()
_h2a.setMode('H', 'a')
_h2a.setMode('K', 'a')
h2a = _h2a.getConverter()

while True:
    s = fi.readline()
    if s == "":
        break
    num = jp = jph = jpa = cn = ""
    index = 0
    for char in s:
        if index == 0:
            if char == '、':
                index = 1
            else:
                num += char
        elif index == 1:
            jp += char
            if char == '。':
                index = 2
        else:
            cn += char
    jph = k2h.do(jp)
    jpa = h2a.do(jph)
    fo.writelines(num + '\n')
    fo.writelines(jp + '\n')
    fo.writelines(jph + '\n')
    fo.writelines(jpa[:-1] + '\n')
    fo.writelines(cn + '\n')
