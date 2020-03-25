#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json,csv,os
from datetime import datetime
def gen_csv(src_data,dst_data,basedir=None):
    if not basedir:
        basedir=os.getcwd()
    jsonpath=basedir+os.sep+"result"+os.sep+"json"
    csvpath=basedir+os.sep+"result"+os.sep+"csv"
    fname=datetime.now().strftime("%Y%m%d_%H_%M_%S")
    if not os.path.exists(jsonpath):
        os.makedirs(jsonpath)
    if not os.path.exists(csvpath):
        os.makedirs(csvpath)
    with open(jsonpath+os.sep+fname+"_src.json","w+") as f:
        json.dump(src_data,f,ensure_ascii=False,indent=4)
    with open(jsonpath+os.sep+fname+'_dst.json','w+') as f:
        json.dump(dst_data,f,ensure_ascii=False,indent=4)
    with open(jsonpath+os.sep+fname+"_src.json",'r') as f:
        srclist=f.readlines()
    with open(jsonpath+os.sep+fname+'_dst.json','r') as f:
        dstlist=f.readlines()
    if len(srclist)>len(dstlist):
        dstlist.extend(['' for i in range(len(srclist)-len(dstlist))])
    elif len(srclist)<len(dstlist):
        srclist.extend(['' for i in range(len(dstlist)-len(srclist))])
    headers=['src_data','dst_data']
    rows=zip(srclist,dstlist)
    dictdatas=list(map(lambda x:dict(zip(headers,x)),rows))
    with open(csvpath+os.sep+fname+'.csv','w+',newline='') as f:
        writer=csv.DictWriter(f,headers)
        writer.writeheader()
        writer.writerows(dictdatas)
