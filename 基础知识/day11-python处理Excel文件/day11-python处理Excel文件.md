# day11-python处理Excel文件


最近需要频繁读写 excel 文件，想通过程序对 excel 文件进行自动化处理，发现使用 python 的 openpyxl 库进行 excel 文件读写实在太方便了，结构清晰，操作简单。本文对 openpyxl 的使用进行总结，主要包含以下内容：

- openpyxl 的介绍及 excel 文件结构说明
- 工作表的读写处理
- 行列的读写处理
- 单元格的读写处理

 ## openpyxl 及 excel 文件结构

 openpyxl 是一个对 xlsx/xlsm/xltx/xltm 格式的 2010 excel 文档进行读写的 python 库。它官网有详细的文档介绍。在进行使用前，需先安装并引入

```
# 安装
pip install openpyxl
# 引入openpyxl 模块
import openpyxl

```
在进行 excel 操作之前，先对 excel 的文件结构做一个简单了解，以便于熟悉后续的操作。如下图：



一个 excel 文件，其内容按层次分为工作簿(文件) -> 工作表(sheet) -> 行列 -> 单元格 ，对应上图，整个 excel 文件即是一个工作簿；工作簿下可以有多个工作表(如图中的 Sheet1/test1 等等)；工作表中就是对应的表格数据，分为行和列，行是用序号表示，列用大写字母表示（也可用序号）；行与列的交点就是每一个存储数据的单元格。因此，我们对 excel 表格进行读写，基本按这个层次思路来操作：读入文件，找到工作表，遍历行列，定位单元格，对单元格进行读写。因此，会涉及到工作表、行列、单元格的读写操作。这些操作之前，需要先把文件加载进来，一个 excel 文件就是一个工作簿 (workbook)，

 
## 工作表读取

工作表( sheet )会有多个，可以读取全部的工作表，读取单个时，可以按 sheet 名称读取，也可以按下标（下标从0开始）。

- 全部工作表对象：`workbook.worksheets`
- 全部工作表名称：`workbook.sheetnames`
- 按名称(sheet_name)获取工作表：`workbook[sheet_name]`
- 按下标(i从0开始)获取工作表：`workbook.worksheets[i]`
- 获取正在使用的工作表：`workbook.active`
- 获取工作表的属性（如工作表名称、最大行数和列数等）：`sheet.title、sheet.max_row、sheet.max_column`
 
```
def demo1():
    print("")
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    # 全部sheet对象
    worksheets = workbook.worksheets
    print("全部sheet对象:",worksheets)
    # 全部sheet名称
    sheet_name = workbook.sheetnames
    print("全部sheet名称:",sheet_name)
    # 按名称读取sheet
    sheet_1 = workbook["SheetJS"]
    print("按名称读取sheet:",sheet_1)
    # 按下标读取
    sheet_2 = worksheets[0]
    print("按下标读取sheet:", sheet_2)
    # 获取当前正在使用的sheet
    sheet_active= workbook.active
    print("获取当前正在使用的sheet:",sheet_active)
    # 获取sheet的属性
    sheet_title = sheet_active.title
    print("获取sheet的属性:",sheet_title)
    # 获取行
    max_row = sheet_active.max_row
    print("获取行:",max_row)
    # 获取列
    max_column = sheet_active.max_column
    print("获取列:",max_column)
```



## 工作表添加


若需要新增工作表，按操作流程，先添加工作表，再保存文件。创建通过`create_sheet`完成，创建后保存(save)文件，添加才能生效。

- 创建工作表，若名称相同，则自动进行重命名：`workbook.create_sheet("test3")`
- 在指定的下标创建工作表：`workbook.create_sheet("test4",1)`
- 保存文件，若文件路径与打开的文件路径相同，则覆盖；不同，则会复制原文件并保存（相当于另存为）：`workbook.save(file_path)`

```
def demo2():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    print(sheet)
    workbook.create_sheet("我是一个新的sheet")
    print(workbook.sheetnames)
    workbook.save(file_path)
```

## 工作表修改

要修改工作表名称，直接通过设置工作表的 title 即可，修改后同样需要保存文件。

```
def demo3():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    # 修改工作表名称
    workbook.active.title = "test"
    # 保存文件
    workbook.save(file_path)
```



## 工作表删除

删除工作表，需要先获取 sheet 对象，然后删除。删除有两种方式，一是使用 workbook 提供的 remove 方法，也可以直接使用 python 的del进行删除。删除操作后，同样需要保存文件：

```
def demo4():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet_active = workbook.active
    # remove删除工作表
    # workbook.remove(sheet_active)
    # del操作删除
    del workbook["test"]
    # 保存文件
    workbook.save(file_path)

```















