import xlrd


def FindData(filedir):
    list = []
    data = xlrd.open_workbook(filedir)
    table = data.sheets()[0]
    list = table.col_values(2)#第三列数据
    list2 = table.col_slice(2,3,None)
    print(list2)
    #print(len(list))
    return list
