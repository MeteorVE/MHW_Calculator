# -*- coding: utf-8 -*-

import csv
import json

# 設計用來切護石的。

def csv_to_json(csvFile,jsonFile) :
	f = open(csvFile, 'r')
	fw = open(jsonFile,'w')
	i=0
	head_dir=[]
	for row in csv.DictReader(f):
		if i<3:

			material_dir = {}
			material_arr = []
			mNUM = []

			for key in list(row.keys()):
				if "material" in key :
					material_arr.append(row[key])
					del row[key]
				elif "mNUM" in key:
					mNUM.append(row[key])
					del row[key]

			for el in mNUM:
				if el.replace(' ','') != "":
					material_dir[material_arr[mNUM.index(el)]] = el
			#print("\n\n\n")

			row['material'] = material_dir
			head_dir.append(row)
			#print(row)#debug
			#i+=1 #debug
		#print(json.dumps(row, ensure_ascii=False)) # e04 ...
	    #print (row['defense1'])
	fw.write(json.dumps(head_dir,ensure_ascii=False))
	f.close()
csv_to_json('MHW_GUARDIANSTONE.csv','MHW_GUARDIANSTONE.json')
'''
csv_to_json('MHW_BODY.csv','MHW_BODY.json')
csv_to_json('MHW_WAIST.csv','MHW_WAIST.json')
csv_to_json('MHW_LEG.csv','MHW_LEG.json')
csv_to_json('MHW_HAND.csv','MHW_HAND.json')
'''
