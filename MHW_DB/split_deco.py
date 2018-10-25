# -*- coding: utf-8 -*-

import csv
import json

def csv_to_json(csvFile,jsonFile) :
	f = open(csvFile, 'r', encoding = 'utf8')
	fw = open(jsonFile,'w', encoding = 'utf8')
	i=0
	head_dir=[]
	for row in csv.DictReader(f):
		if i<3:
			for key in list(row.keys()):
				if "name" in key:
					tmp = row[key]
					del row[key]
					row["name"] = tmp
				if "level" in key:
					#print("KEY:",row[key])
					if "Lv1" in row[key]:
						#del row[key]
						row['level'] = 1;
					elif "Lv2" in row[key]:
						#del row[key]
						row['level'] = 2;
					elif "Lv3" in row[key]:
						#del row[key]
						row['level'] = 3;
		print(row)
		head_dir.append(row)
		#print(json.dumps(row, ensure_ascii=False)) # e04 ...
	fw.write(json.dumps(head_dir,ensure_ascii=False))
	f.close()


csv_to_json('decoration.csv','MHW_DECO.json')

'''
csv_to_json('MHW_DECO.csv','MHW_DECO.json')
csv_to_json('MHW_HEAD.csv','MHW_HEAD.json')
csv_to_json('MHW_BODY.csv','MHW_BODY.json')
csv_to_json('MHW_WAIST.csv','MHW_WAIST.json')
csv_to_json('MHW_LEG.csv','MHW_LEG.json')
csv_to_json('MHW_HAND.csv','MHW_HAND.json')
'''
