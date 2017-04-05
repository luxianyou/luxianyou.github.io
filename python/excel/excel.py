#-*- coding: utf8 -*-

import xlrd
import xlwt
from datetime import datetime


def set_style(font_name, font_height, bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = font_name         # 'Times New Roman'
    font.height = font_height
    font.bold = bold
    font.colour_index = 4

    borders = xlwt.Borders()
    borders.left = 6
    borders.right = 6
    borders.top = 6
    borders.bottom = 6

    style.font = font
    style.borders = borders
    return style


def handle_excel_by_xlrd_xlwt():
    #*****************************************    Read    ********************
    # file
    TC_workbook = xlrd.open_workbook(r"基础jekins统计情况表 - 副本.xlsx")

    # sheet
    all_sheets_list = TC_workbook.sheet_names()
    print("All sheets name in File:", all_sheets_list)

    first_sheet = TC_workbook.sheet_by_index(0)
    print("First sheet Name:", first_sheet.name)
    print("First sheet Rows:", first_sheet.nrows)
    print("First sheet Cols:", first_sheet.ncols)

    second_sheet = TC_workbook.sheet_by_name("Sheet2")
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
    new_sheet = new_workbook.add_sheet("SheetName_test")
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
    new_workbook.save(r"NewCreateWorkbook.xls")


if __name__ == "__main__":
    handle_excel_by_xlrd_xlwt()
