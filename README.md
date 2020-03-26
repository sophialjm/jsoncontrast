# pip install jsoncontrast 出于尝试的心态~
## Used to contrast two json,especially for testers.
`jsoncontrast.check(src_data, dst_data,model='contains',string_model='strict',num_model='equal',num_limit=None,explicit=True,basedir=None)`
#### 主要用来对比json串的期望值和返回值，用于接口测试，方法包括以下8个入参：
* 2个必选参数：
  * src_data-----用来做对比的一个json串，一般地，例如：接口实际返回的json
  * dst_data-----用来做对比的另一个json串，一般地，例如：校验接口的期望返回json
* 6个可选参数：
  * model='contains'-----可选范围['contains','strict']
    * contains: src_data包含dst_data
    * strict: src_data与dst_data不计顺序内容一致
  * string_model='strict'-----可选范围['contains','strict','start','end','exist']
    * contains: dst_data中的字符串项包含于src_data中对应的字符串
    * strict: dst_data中的字符串等于src_data中对应的字符串
    * start: src_data中的字符串以dst_data中对应的字符串开头
    * end: src_data中的字符串以dst_data中对应的字符串结尾
    * exist: 只想判断dst_data中某项存在，不需要比较具体值，对应值的位置写成'<EE>'
  * num_model='equal'-----可选范围['equal','nequal','big','small']
    * equal: dst_data中的数字项等于src_data中对应的数字项
    * nequal: dst_data中的数字项不等于src_data中对应的数字项
    * big: dst_data中的数字项大于src_data中对应的数字项
    * small: dst_data中的数字项小于src_data中对应的数字项  
  * num_limit=None-----可选范围：无或任意整数或浮点数
    * 仅在num_model等于big或small时起效，用于额外的设定dst_data中的数字项的上限或下限
  * explicit=True-----可选范围：True或False
    * 用于设定是否需要生成json对比文件
  * basedir=None-----可选：用于设定结果存放目录，默认存放于项目文件夹
    * 仅在explicit=True时起效  
 ## 举例，eg.  
 `src={"k1" :{"k11":[{"listk111": "北京"},{"listk112": "上海"}],"k12":{"listk121": 7}},"k2":{"listk21": "广州"} }`  
 `dst={"k1":{"k12":{"listk121": 5}}}`  
 `jsoncontrast.check(src,dst,num_model='small',num_limit=4)`  
 

## It offers a method jsontester.check,you can use it according to what above descripted in Chinese,or just guess and try,it is so easy!
