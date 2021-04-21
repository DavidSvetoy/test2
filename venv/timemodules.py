#
# # from openpyxl import Workbook
# # wb=Workbook()
# # sheet=wb.active
# # sheet["A1"]="username"
# # sheet["b1"]="password"
# # sheet["a2"]="tester1"
# # sheet["b2"]="1234"
# # sheet["a3"]="tester2"
# # sheet["b3"]="45678"
# # wb.save(filename="login.xlsx")
# from openpyxl import load_workbook
# wb=load_workbook(filename="login.xlsx")
# sheet=wb.active
# print(sheet)
# print(sheet["a1"].value)
# print(sheet["a2"].value)
# print(sheet["a3"].value)
# print(sheet["b1"].value)
# print(sheet["b2"].value)
# print(sheet["b3"].value)
# # for value in sheet.iter_rows(min_row=1,
# #                              max_row=3,
# #                              min_col=1,
# #                              max_col=2,values_only=True):
# #     print(value)
# for value in sheet.iter_cols(min_row=1,
#                              max_row=3,
#                              min_col=1,
#                              max_col=2,values_only=True):
#     print(value)
# import
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
sheet["b1"]="test1"
sheet["c1"]="test2"
sheet["d1"]="test3"
sheet["e1"]="test4"
sheet["f1"]="test5"
sheet["g1"]="test6"
sheet["h1"]="test7"
sheet["a2"]="category"
sheet["a3"]="product id"
sheet["a4"]="quantity"
sheet["a5"]="color"
sheet["b2"]="speakers"
sheet["b3"]="19"
sheet["b4"]="2"
sheet["b5"]="red"
sheet["c2"]="headphones"
sheet["c3"]="12"
sheet["c4"]="2"
sheet["c5"]="purple"
sheet["d2"]="mice"
sheet["d3"]="28"
sheet["d4"]=""
sheet["d5"]="green"
sheet["e2"]="mice"
sheet["e3"]="30"
sheet["e4"]="1"
sheet["e5"]=""
sheet["f2"]="laptops"
sheet["f3"]="9"
sheet["f4"]="2"
sheet["f5"]="blue"
sheet["g2"]="laptops"
sheet["g3"]="7"
sheet["g4"]="3"
sheet["g5"]=""
sheet["h2"]="tablets"
sheet["h3"]="18"
sheet["h4"]=""
sheet["h5"]="yellow"
wb.save(filename="testdata.xlsx")
from openpyxl import load_workbook
wb=load_workbook(filename="testdata.xlsx")
sheet=wb.active
tests = {}
test_arr = {}
for col in sheet.iter_cols(min_row=1,
                             max_row=5,
                             min_col=2,
                             max_col=7,values_only=True):

    test_name = col[0]
    tests = {
        "category":col[1],
        "product_id":col[2],
        "quantity":col[3],
        "color":col[4]
    }
    test_arr[test_name] = tests
print(test_arr)
# import json
# json=json.dumps(value)
# print(json)