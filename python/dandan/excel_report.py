#-*- coding: utf8 -*-

import xlrd
import xlwt
import pymysql
from datetime import date,datetime


def set_style(font_name, font_height, bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = font_name         # 'Times New Roman'
    font.height = font_height
    font.bold = bold
    font.colour_index = 0

    borders = xlwt.Borders()
    borders.left = 1
    borders.right = 1
    borders.top = 1
    borders.bottom = 1

    style.font = font
    style.borders = borders
    return style


def handle_excel_by_xlrd_xlwt():
    #*****************************************    Read    ********************
    # file
    TC_workbook = xlrd.open_workbook(r"CODE.xlsx")

    # sheet
    all_sheets_list = TC_workbook.sheet_names()
    print("All sheets name in File:", all_sheets_list)

    first_sheet = TC_workbook.sheet_by_index(0)
    print("First sheet Name:", first_sheet.name)
    print("First sheet Rows:", first_sheet.nrows)
    print("First sheet Cols:", first_sheet.ncols)

    second_sheet = TC_workbook.sheet_by_name("原始数据表")
    print("Second sheet Rows:", second_sheet.nrows)
    print("Second sheet Cols:", second_sheet.ncols)

    first_row = first_sheet.row_values(0)
    print("First row:", first_row)
    first_col = first_sheet.col_values(0)
    print("First Column:", first_col)

    # cell
    cell_value = first_sheet.cell(1, 0).value
    print("The 1th method to get Cell value of row 2 & col 1:", cell_value)
    cell_value2 = first_sheet.row(1)[0].value
    print("The 2th method to get Cell value of row 2 & col 1:", cell_value2)
    cell_value3 = first_sheet.col(0)[1].value
    print("The 3th method to get Cell value of row 2 & col 1:", cell_value3)

    #*****************************************    Write    *******************
    new_workbook = xlwt.Workbook()
    new_sheet = new_workbook.add_sheet("透视表")
    new_sheet.write(0, 0, "hello")
    # write cell with style
    new_sheet.write(0, 1, "world", set_style("Times New Roman", 220, True))

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='YYYY-MM-DD')
    new_sheet.write(1, 0, 1234.56, style0)
    new_sheet.write(1, 1, datetime.now(), style1)

    # write cell with formula
    new_sheet.write(2, 0, 5)
    new_sheet.write(2, 1, 8)
    new_sheet.write(3, 0, xlwt.Formula("A3+B3"))

    # if change to xlsx,then open failed
    new_workbook.save(r"透视表.xls")

def read_excel_to_database():
    
    workbook = xlrd.open_workbook(r"CODE - 副本.xlsx")
    sheet_source_data = workbook.sheet_by_name("原始数据表")
    print("原始数据表 sheet Rows:", sheet_source_data.nrows)
    print("原始数据表 sheet Cols:", sheet_source_data.ncols)
    
    # 打开数据库连接
    db = pymysql.connect("localhost","admin","admin","sales_data")
    bach_list = []
    sql = ""
    
    for each in range(1,sheet_source_data.nrows):
        bach_list.append(multipleRows([
            convert_dot_num_to_int(sheet_source_data.row(each)[6].value),
            convert_dot_num_to_int(sheet_source_data.row(each)[0].value),
            convert_dot_num_to_int(sheet_source_data.row(each)[1].value),
            sheet_source_data.row(each)[2].value,
            sheet_source_data.row(each)[3].value,
            sheet_source_data.row(each)[4].value,
            sheet_source_data.row(each)[5].value,
            sheet_source_data.row(each)[7].value,
            sheet_source_data.row(each)[8].value,
            sheet_source_data.row(each)[9].value,
            sheet_source_data.row(each)[10].value,
            sheet_source_data.row(each)[11].value,
            sheet_source_data.row(each)[12].value,
            convert_dot_num_to_int(sheet_source_data.row(each)[13].value),
            float('%.2f' % sheet_source_data.row(each)[14].value),
            float('%.2f' % sheet_source_data.row(each)[15].value),
            sheet_source_data.row(each)[16].value,
            sheet_source_data.row(each)[17].value,
            sheet_source_data.row(each)[18].value,
            convert_excel_date_to_str(sheet_source_data.row(each)[19].value,workbook),
            sheet_source_data.row(each)[20].value
        ]))


        sql = """INSERT INTO product(
                code,`year`,`month`,store_code, store_name,province,
                city,bar_code,product_name,product_class,category,brand,
                product_section,sales_volume,cost_marketing,sales_amount,
                sales_type,ul_store_code,ul_sku_code,`year_month`,customer)
                VALUES %s """ % ','.join(bach_list)

    #print(sql)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    cursor.execute(sql)

    cursor.close()
    db.commit()

    # 关闭数据库连接
    db.close()

def save_data_to_excel():
    db = pymysql.connect("localhost","admin","admin","sales_data")
    sql = """
        SELECT 
            ifnull(t.category,'总计') as category,
            ifnull(t.brand,t.category) as brand,
            SUM(IF(t.`month` = '1', t.sales_amount, 0)) AS '1',
            SUM(IF(t.`month` = '2', t.sales_amount, 0)) AS '2'
        FROM
            sales_data.product t
        GROUP BY t.category , t.brand
        WITH ROLLUP
    """
    cursor = db.cursor()
    count = cursor.execute(sql)
    print("has %d record" %count)
    cursor.scroll(0,mode='absolute')
    results = cursor.fetchall()
    fields = cursor.description
    print(fields)
    print(results)

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('透视表',cell_overwrite_ok=True)
    for title in range(0,len(fields)):
        sheet.write(0,title,fields[title][0],set_style("宋体", 250, True))

    ics=1
    jcs=0
    for ics in range(1,len(results)+1):
        for jcs in range(0,len(fields)):
            sheet.write(ics,jcs,results[ics-1][jcs])
    workbook.save('透视表.xls')
 
def multipleRows(params):
    ret = []
    # 根据不同值类型分别进行sql语法拼装
    for param in params:
        if isinstance(param, (int, float, bool)):
            ret.append(str(param))
        elif isinstance(param, (str)):
            ret.append('"' + param + '"')
        else:
            print_log('unsupport value: %s ' % param)
    return '(' + ','.join(ret) + ')'

def convert_dot_num_to_int(args_key):
    if(args_key == ''):
        return args_key
    args_key = float(args_key)
    if args_key == int(args_key):
        return int(args_key)
    else:
        return args_key

def convert_excel_date_to_str(args_key,book):
    date_value = xlrd.xldate_as_tuple(args_key,book.datemode)
    date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
    return date_tmp

if __name__ == "__main__":
    #read_excel_to_database()
    save_data_to_excel()
    #handle_excel_by_xlrd_xlwt()
    