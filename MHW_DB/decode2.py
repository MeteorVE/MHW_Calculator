bom_file = "MHW_DECO.json"
s = open(bom_file, mode='r', encoding='utf-8-sig').read()
open(bom_file, mode='w', encoding='utf-8').write(s)
