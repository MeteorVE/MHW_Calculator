# -*- coding: utf-8 -*-

import csv
import json

def csv_to_json(csvFile,jsonFile) :
	f = open(csvFile, 'r')
	fw = open(jsonFile,'w')
	i=0
	head_dir=[]
	for row in csv.DictReader(f):
		if i<3:
			defense_arr = []

			skill_dir = {}
			skill_arr = []
			skill_LV = []

			material_dir = {}
			material_arr = []
			mNUM = []

			deco = [0,0,0]
			deco_dir={}
			#print("row:\n")
			#print(row)
			#print("\n\n\n")
			for key in list(row.keys()):
				if "skill" in key:
					skill_arr.append(row[key])
					del row[key]
				elif "skLV" in key:
					skill_LV.append(row[key])
					del row[key]
				elif "defense" in key :
					defense_arr.append(row[key]) # just use array not fire water ...
					del row[key]
				elif "material" in key :
					material_arr.append(row[key])
					del row[key]
				elif "mNUM" in key:
					mNUM.append(row[key])
					del row[key]
				elif "decoration" in key:
					for idx in range(0,3):
						if row[key][idx] != '-':
							#print(key,key[idx],"???")
							#print(deco[int(row[key][idx])-1])
							deco[int(row[key][idx])-1]+=1
					del row[key]
				elif "caseSk" in key:
					caseSkill_copy = row[key]
					del row[key]
					row["caseSkill"] = caseSkill_copy
			for el in skill_LV:
				if el.replace(' ','') != "":
					skill_dir[skill_arr[skill_LV.index(el)]] = el
			for el in mNUM:
				if el.replace(' ','') != "":
					material_dir[material_arr[mNUM.index(el)]] = el
			for idx in range(0,3):
				if idx==0 :
					deco_dir['一級珠'] = deco[idx]
				if idx==1 :
					deco_dir['二級珠'] = deco[idx]
				if idx==2 :
					deco_dir['三級珠'] = deco[idx]
			#print("\n\n\n")

			row['defense'] = defense_arr
			row['material'] = material_dir
			row['skill'] = skill_dir
			row['decoration'] = deco_dir
			head_dir.append(row)
			#print(row)#debug
			#i+=1 #debug
		#print(json.dumps(row, ensure_ascii=False)) # e04 ...
	    #print (row['defense1'])
	fw.write(json.dumps(head_dir,ensure_ascii=False))
	f.close()
csv_to_json('MHW_HEAD.csv','MHW_HEAD.json')
'''
csv_to_json('MHW_BODY.csv','MHW_BODY.json')
csv_to_json('MHW_WAIST.csv','MHW_WAIST.json')
csv_to_json('MHW_LEG.csv','MHW_LEG.json')
csv_to_json('MHW_HAND.csv','MHW_HAND.json')
'''
