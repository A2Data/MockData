# Mock数据使用说明

**项目使用必备库**

## Mac

 pip install pymysql


## 1 生成表数据配置

在*config_all.conf*中输入所需的表格信息配置。

在配置文件中，如下每个section均为一张表的配置信息：

```python
#示例：

[table_1]
tb_name = tb1
type = a
columns = name,Phone
row_number = 10
```

中括号内固定格式为**table_数字**，数字需从1开始，每张表递增1。



**tb_name**：在等号右侧输入表名。



**type**：如要多张表内相同字段生成的内容一致，需在各表type等号右侧输入相同的字段。等号右侧内容不能为空。

如下示例，tb1和tb2的“type”均为a，因此两表name字段内容相关联；tb3的“type”为b，则与前两张表无关：

```python
#示例：

[table_1]
tb_name = tb1
type = a
columns = name,Phone
row_number = 10

[table_2]
tb_name = tb2
type = a
columns = name,Phone,Address
row_number = 20

[table_3]
tb_name = tb3
type = b
columns = Xin,Ming,MaleName
row_number = 30
```



**columns**：在等号右侧输入表中所需的字段名，多个字段名以英文逗号隔开。

目前可以生成的字段名有（需注意大小写）：

```python
name,Xin,Ming,MaleName,FemaleName,Phone,Address,SSN,Email,Ipv4,url,company,job,uuid,card,date_time,ThisDate,Time,pyint,randomMxStr,randomList,profile,profile1,browser,platform,seed,mobile_user
```



**row_number**：在等号右侧输入表行数。



## 2 数据库连接配置

[sql_config]内输入数据库配置。

```python
#示例：

[sql_config]
数据库类型 = mysql
数据库驱动选择 = M
用户名 = root
密码 = 123456
服务器 = localhost
端口 = 3306
目标数据库名 = mock
```

目标数据库名根据数据库中具体目标库名修改。

## 3 运行数据

完成上述配置后，打开main.py文件运行即可。



## 4 本地留存生成数据的csv文件

在*mock.py*同一文件夹下可以找到总表和子表生成数据的csv文件，表名相同的仅保留当日最后一次生成文件。





# 关于后续优化的一点笔记

## 1 新增样本池

在FakerData.py文件构造新增的类和函数对于需要样本池的随机数，读入相应csv样本池文件，用random.choice返回随机数；

在*FakerData.py*文件中直接构造新增的类和函数；

对于需要样本池的随机数：

​	先在*pool*文件夹中建立样本池，格式为csv文件，csv文件内列名为对应函数名称，内容按列书写；

​	再在*FakerData.py*文件中读取样本池csv文件，返回随机数；

## 2 类和函数映射关系配置维护

在*FunctionClassConfig.py*文件中维护类和函数的对应关系，所有*FakerData.py*中的类和函数必须在*FunctionClassConfig.py*添加和维护确保一致；

注意区分大小写；

dict1记录格式为：

```python
字段名:函数名
```

后续可以扩展为多场景字段名对应同一函数名；

dict2记录格式为：

```python
函数名:类名
```



