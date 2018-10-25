# -*- coding: utf-8 -*-

f = open("MHW_DECO.json","r")
output = open("MHW_decode.json","w")
s = f.read()
u = s.decode("utf-8-sig") # 得到一个不含BOM的unicode string
s = u.encode("utf-8")   # 将unicode转换为utf-8
output.write(s)
f.close()