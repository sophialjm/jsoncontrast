#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from jsoncontrast.Contrast_Json import compare_dict
from jsoncontrast.Gen_Csv import gen_csv
import sys
def check(src_data, dst_data,model='contains',string_model='strict',num_model='equal',num_limit=None,explicit=True,basedir=None):
    if model not in ['contains','strict']:
        print("请检查参数：model参数值应为 ['contains','strict']其一")
        sys.exit(-2)
    if string_model not in ['contains','strict','start','end','exist','re_expr']:
        print("请检查参数：string_model参数值应为 ['contains','strict','start','end','exist','re_expr']其一")
        sys.exit(-2)
    if num_model not in ['equal','nequal','big','small']:
        print("请检查参数：num_model参数值应为 ['equal','nequal','big','small']其一")
        sys.exit(-2)
    elif num_model in ['big','small'] and (not (type(num_limit)==int or type(num_limit)==float)):
        print("请检查参数：num_limit应为数字")
        sys.exit(-2)
    if not (type(explicit)==bool):
        print("请检查参数：explicit应为True或False")
        sys.exit(-2)
    r1=compare_dict(src_data, dst_data,string_model,num_model,num_limit)
    if model=='contains':
        r2=True
    elif model=='strict':
        r2=compare_dict(dst_data,src_data,string_model,num_model,num_limit)
    else:
        print("请检查参数,model取值范围：'contains'或'strict'")
    if r1 and r2:
        print("比对通过")
    if explicit and ((not r1) or (not r2)):
        csvpath=gen_csv(src_data,dst_data,basedir)
        print("比对失败，结果已生成至{}目录".format(csvpath))
    elif explicit==False:
        print("比对失败，未设置结果生成")



