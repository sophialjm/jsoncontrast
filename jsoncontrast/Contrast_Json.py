#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys,re
def meta_string_compare(src_data, dst_data,model):
    if model=='strict'and dst_data == src_data:
        return True
    elif model=='contains'and dst_data in src_data:
        return True
    elif model=='start'and src_data.startswith(dst_data):
        return True
    elif model=='end'and src_data.endswith(dst_data):
        return True
    elif model=='exist'and src_data and dst_data=='<EE>':
        return True
    elif model=='re_expr':
        if "re." in dst_data:
            dst_data=dst_data.replace('{{src}}',src_data)
            r=eval(dst_data)
            if r:
                return True
        else:
            return meta_string_compare(src_data,dst_data,'strict')
    return False
def meta_num_compare(src_data, dst_data,model,limit=None):
    if model=='big'and limit<=dst_data:
        print("big模式下，num_limit作为上限值，应大于dst_data")
        sys.exit(-2)
    if model=='small'and limit>=dst_data:
        print("small模式下，num_limit作为下限值，应小于dst_data")
        sys.exit(-2)
    if model=='equal'and dst_data == src_data:
        return True
    elif model=='nequal'and dst_data != src_data:
        return True
    elif model=='big'and dst_data>src_data:
        if limit is None or limit>dst_data:
            return True
        else:
            return False
    elif model=='small'and dst_data<src_data:
        if limit is None or limit<dst_data:
            return True
        else:
            return False
    return False

def compare_dict(src_data, dst_data,string_model='strict',num_model='equal',num_limit=None):
    try:
        if isinstance(dst_data, dict):
            for key in dst_data:
                if key not in src_data:
                    return False
            for key in dst_data:
                dst_val = dst_data.get(key)
                src_val = src_data.get(key)
                flag = compare_dict(src_val, dst_val,string_model,num_model,num_limit)
                if flag is False:
                    return False
            return True
        elif isinstance(dst_data, list):
            if len(dst_data) > len(src_data) or not isinstance(src_data, list):
                return False
            for dst_list in dst_data:
                flag=False
                for src_list in src_data:
                    if type(dst_list)==type(src_list) and compare_dict(src_list, dst_list,string_model,num_model,num_limit):
                        flag=True
                        src_data.remove(src_list)
                        break
                if flag==False:
                    return False
            return flag
        elif isinstance(dst_data, int) or isinstance(dst_data, float):
            return meta_num_compare(src_data, dst_data,num_model,num_limit)
        else:
            return meta_string_compare(src_data, dst_data,string_model)
    except Exception as e:
        print("-----______报错了_______-----\n",e)


