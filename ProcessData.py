import xlrd


def FindData(filedir):
    list = []
    list2 = []
    data = xlrd.open_workbook(filedir)
    table = data.sheets()[0]
    #list = table.col_values(4)#第五列数据
    #print(table.col_types(4))
    list = table.col_values(4,6,16)#先试验10个数据
    print(list)
    for i in range(len(list)):#转化为str类型方便填入
        num = list[i]
        str = "%.3f" %num
        list2.append(str)
    print(list2)
    print(len(list))
    return list2,list

