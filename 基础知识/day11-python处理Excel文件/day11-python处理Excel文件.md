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

![](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day11-python处理Excel文件/excel.png)

![](https://github.com/SunshineBrother/PythonStudy/blob/main/基础知识/day11-python处理Excel文件/excel1.png)

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

## 行列处理

获取 sheet 对象后，后续即可进行行列操作，包括行列读取，添加，删除等。


### 读行列

- 获取全部行和列，然后可以进行遍历：`sheet.rows ，sheet.columns`
- 读取部分行列：读一行`sheet[1]`,读多行`sheet[2:3]`，读一列`sheet['A']`，读多列`sheet['B:C']`


```
def demo5():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    # 遍历全部行
    for row in sheet.rows:
        print("row:",row)
    # 读取部分行列
    print("-----------------------")
    print(sheet[1])
    print("-----------------------")
    print(sheet["A:B"])
```


### 添加行列

添加行列，可以指定位置添加单个行列或多个行列。

- 直接在工作表中追加行数据：`sheet.append(rowdata)`
- 在指定 index（从1开始计算） 位置添加行列：`sheet.insert_rows,sheet.insert_cols`

```
def demo6():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    # 在第4行插入1行空行
    sheet.insert_rows(4)
    # 在第2行插入2行空行
    sheet.insert_rows(idx=2,amount=2)
    # 添加一行数据到表
    row_data = ["tom", 15, "tom@test.com"]
    sheet.append(row_data)
    workbook.save(file_path)
```

### 删除行列

删除操作与插入行列操作方式一致，使用delete_rows及delete_cols方法。

```
def demo7():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    # 删除行
    sheet.delete_rows(2, 2)
    workbook.save(file_path)
```


## 单元格处理

我们的数据最终是保存在每一个单元格（Cell）中，因此，最终我们操作数据其实就是单元格中的数据，单元格中，openpyxl 使用是 Cell 对象。前面在遍历行列数据时，可以看到输出<Cell 'Sheet1'.A1>的内容，这对应的单元格对象。下面对单元格的操作进行说明。
 


### 获取单元格数据值及属性值

定位获取单元格有两种方式：

- 直接指定行列名：`sheet[A1]`
- 使用 cell 函数（行列下标从1开始）：`sheet.cell(row=2,column=1)`

```
def demo8():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    # 指定行列坐标获取单元格
    cell_1 = sheet["A1"]
    print("指定行列坐标获取单元格:",cell_1)

    # cell函数获取单元格
    cell_2 = sheet.cell(row=1,column=1)
    print("cell函数获取单元格:",cell_2)

    # cell 值
    value = cell_2.value
    print("cell 值:",value)
    print("cell_2.coordinate:",cell_2.coordinate)
    print("cell_2.row:",cell_2.row)
    print("cell_2.column:",cell_2.column)
```


### 移动单元格

通过对单元格区域，可以向上、下、左、右进行移动，使用的是move_range(range,rows,cols)，其中 rows 和 cols 为整数，正整数表示向下或向右，负整数为向上或向左。

```
def demo9():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    # 移动数据区域(向上移动2行，向右移动3列)，正整数为向下或向右，负整数为向上或向左
    sheet.move_range("A3:C3", rows=-2, cols=3)
    workbook.save(file_path)
```


### 合并拆分单元格

对于跨行和跨列，需要对单元格进行合并，使用的是merge_cells(range_string, start_row, start_column, end_row, end_column)。如果要合并的单元格都有数据，只会保留左上角的数据，其他则丢弃。合并及拆分都可以通过行列坐标（如A1）或者行列下标（如1,2）进行。
 
 ```
 def demo10():
    file_path = "/Users/yunna/Desktop/1.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    # 单元格合并，使用范围坐标
    sheet.merge_cells("A2:B3")
    # 单元格合并，指定行列下标（下标从1开始）
    sheet.merge_cells(start_row=5, start_column=3, end_row=7, end_column=4)
    workbook.save(file_path)
    # 拆分单元格
    sheet.unmerge_cells("A2:B3")
    sheet.unmerge_cells(start_row=5, start_column=3, end_row=7, end_column=4)
    # 保存文件
    workbook.save(file_path)

 ```



### 写入单元格

对单元格值进行修改和写入，直接对cell.value进行赋值即可。这里需要注意的是，可以写入 excel 公式，具体公式与 excel 中用到公式一致，另外，若是写入公式，读取时获取到的 value 值也是公式，而非公式值。

```
# 写入值
cell.value = "张三"
# 写入公式(求平均值)
cell.value = "=AVERAGE(B2:B6)"

```


### 设置单元格格式

单元格的格式包括行高，列宽，字体、边框、对齐方式、填充颜色等。这些都在 openpyxl 的 styles 模块中。

- 行高/列宽：`row_dimensions[row_num].height = xx，sheet.column_dimensions[col_name].width = xx`
- 字体( Font 对象)：包括字段名称，大小、加粗、斜体、颜色等，`Font(name="微软雅黑", size=20, bold=True, italic=True, color="000000")`
- 边框（ Border 对象和 Side 对象）：边框每一条边的格式大小/颜色`Side(style="thin", color="000000")`，通过边构建边框对象：`Border(left=side, right=side, top=side, bottom=side)`
- 对齐（ Alignment 对象）：垂直和水平对齐方向，是否自动换行。`Alignment(horizontal="center", vertical="center", wrap_text=True)`
- 填充颜色，分为普通颜色填充和渐变颜色填充：`PatternFill(fill_type="solid", fgColor="FF0000")和 GradientFill(stop=("FF0000", "FD1111", "000000"))`
 
```
# 设置行高和列宽
sheet.row_dimensions[1].height = 50
sheet.column_dimensions["A"].width = 20
# 设置单元格字体
cell = sheet["A1"]
current_font = cell.font
font = Font(name="微软雅黑", size=20, bold=True, italic=True, color="000000")
cell.font = font
# 设置边框(细边，黑色)
side_style = Side(style="thin", color="000000")
border = Border(left=side_style, right=side_style, top=side_style, bottom=side_style)
cell.border = border
# 居中对齐，自动换行
cell_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
cell.alignment = cell_alignment
# 填充颜色（红色填充，和红色到黑色渐变填充）
p_fill = PatternFill(fill_type="solid", fgColor="FF0000")
g_fill = GradientFill(stop=("FF0000", "FD1111", "000000"))
cell.fill = p_fill
sheet["B1"].fill = g_fill


```



最后注意的是，这些修改操作最后都需要通过保存操作（wb.save(file_path)）才能生效。

















