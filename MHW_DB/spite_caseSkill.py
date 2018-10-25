# -*- coding: utf-8 -*-

import csv
import json

def csv_to_json(csvFile,jsonFile) :
	f = open(csvFile, 'r')
	fw = open(jsonFile,'w')

	new_arr=[]
	for row in csv.DictReader(f):
		new_arr.append(row)
	fw.write(json.dumps(new_arr,ensure_ascii=False))
	f.close()
csv_to_json('MHW_CASESKILL.csv','MHW_CASESKILL.json')
