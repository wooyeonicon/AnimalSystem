# 作者 : 杨航
# 开发时间 : 2022/9/30 19:09
import pymysql
db = pymysql.connect(host='127.0.0.1', user='root', password='password', database='animalsystem')
def useMysql_features():
    cursor1 = db.cursor()
    cursor1.execute('select * from features')
    data_feature = cursor1.fetchall() # 元组特征
    # 将事实放入一维数组中
    list = []
    for i in data_feature:
        list.append(i[1])
    # print(list)
    # print(data_feature)
    return list
def useMysql_Relu():
    cursor2 = db.cursor()
    cursor2.execute('select * from relu')
    data_relu = cursor2.fetchall()  # 元组规则
    # 将规则放入二维数组中（不包含id）
    list1 = []
    for i in data_relu:
        list2 = []  # 列
        for j in range(1, 6):
            list2.append(i[j])
        list1.append(list2)
    # print(list1)
    return list1
def useMysql_Relu_id():
    db = pymysql.connect(host='127.0.0.1', user='root', password='password', database='animalsystem')
    cursor2 = db.cursor()
    cursor2.execute('select * from relu')
    data_relu = cursor2.fetchall()  # 元组规则
    # 将规则放入二维数组中(包含id)
    list1_1 = []
    for i in data_relu:
        list2 = []
        for j in range(6):
            list2.append(i[j])
        list1_1.append(list2)
    return list1_1
# 正向推理
def forward(f1,f2,f3,f4):
    # 输入特征（四个，没有的输入0）
    input_feature = []  # 输入的事实。
    list1 = useMysql_Relu()
    list = useMysql_features()
    # 第一种情况：输入的四个特征刚好在规则库里有，则直接得出结论。
    # 获取数据库中所有规则存放在list中
    if f1 != 0:
        input_feature.append(f1)
    if f2 != 0:
        input_feature.append(f2)
    if f3 != 0:
        input_feature.append(f3)
    if f4 != 0:
        input_feature.append(f4)
    list_dic = []
    print('1',list1)
    w = 0
    for i in range(len(input_feature)):
        for n in range(len(list1)):
            for m in range(len(list1[0])):
                if input_feature[i] == list1[n][m]: # 如果这一行中有
                    flag=1
                    for x in range(4):
                        if list1[n][x] != 0 and (list1[n][x] not in input_feature):
                            flag = 0
                    if flag==1:
                        input_feature.append(list1[n][4])
                        w += 1
                        m = 0
                        s = ''
                        dict = {}
                        for j in range(4):
                            if list1[n][j] != 0:
                                m += 1
                        for b in range(m):  # 4
                            if m == 1:
                                if '类' in list[list1[n][4]-1] and '类' in list[list1[n][b]-1]:
                                    s = s +'Type(' + list[list1[n][b] - 1] + ')' + '->' + 'Type(' + list[list1[n][4] - 1] + ')'
                                elif '类' in list[list1[n][4]-1] and '类' not in list[list1[n][b]-1]:
                                    s = s + 'F(' + list[list1[n][b] - 1] + ')' + '->' + 'Type(' + list[list1[n][4] - 1] + ')'
                                elif '类' not in list[list1[n][4]-1] and '类' in list[list1[n][b]-1]:
                                    s = s + 'Type(' + list[list1[n][b] - 1] + ')' + '->' + 'Animal(' + list[list1[n][4] - 1] + ')'
                                elif '类' not in list[list1[n][4]-1] and '类' not in list[list1[n][b]-1]:
                                    s = s + 'F(' + list[list1[n][b] - 1] + ')' + '->' + 'Animal(' + list[list1[n][4] - 1] + ')'
                            if m > 1 and b < m - 1:
                                if '类' not in list[list1[n][b]-1]:
                                    s = s + 'F(' + list[list1[n][b] - 1] + ')' + '+'
                                elif '类' in list[list1[n][b]-1]:
                                    s = s + 'Type(' + list[list1[n][b] - 1] + ')' + '+'
                            if m > 1 and b == m - 1:
                                if '类' in list[list1[n][4]-1] and '类' in list[list1[n][b]-1]:
                                    s = s +'Type(' + list[list1[n][b] - 1] + ')' + '->' + 'Type(' + list[list1[n][4] - 1] + ')'
                                elif '类' in list[list1[n][4]-1] and '类' not in list[list1[n][b]-1]:
                                    s = s + 'F(' + list[list1[n][b] - 1] + ')' + '->' + 'Type(' + list[list1[n][4] - 1] + ')'
                                elif '类' not in list[list1[n][4]-1] and '类' in list[list1[n][b]-1]:
                                    s = s + 'Type(' + list[list1[n][b] - 1] + ')' + '->' + 'Animal(' + list[list1[n][4] - 1] + ')'
                                elif '类' not in list[list1[n][4]-1] and '类' not in list[list1[n][b]-1]:
                                    s = s + 'F(' + list[list1[n][b] - 1] + ')' + '->' + 'Animal(' + list[list1[n][4] - 1] + ')'
                                    # s = s + list[list1[n][b] - 1] + '->' + list[list1[n][4] - 1]
                            print(s)
                        dict['id'] = w
                        dict['relu'] = s
                        list_dic.append(dict)
    print(list_dic)
    # 特征
    cursor1 = db.cursor()
    cursor1.execute('select * from features')
    data_feature = cursor1.fetchall()  # 元组特征

    list3 = []
    for i in data_feature:
        list3.append(i[1])
    print('结果：======',list3[input_feature[-1]-1])
    return list_dic,list3[input_feature[-1] - 1]

# 反向推理
def backward(f1):
    list1 = useMysql_Relu()
    input_features = []       # 事实
    input_features.append(f1) # 把事实放入数组中
    list = useMysql_features()
    flag = True
    i = 0  # 循环事实数组
    list_dic = []
    w = 0
    while flag:
        for j in range(len(list1)):       # 从规则数组中找
            if (input_features[i] == list1[j][4]):   # console
                for n in range(0,4): # 0-3
                    if list1[j][n]!=0 and (list1[j][n] not in input_features):
                        input_features.append(list1[j][n])
                w += 1
                m = 0
                s = ''
                dict = {}
                for a in range(4):
                    if list1[j][a] != 0:
                        m += 1
                for b in range(m):  # 4
                    if m == 1:
                        if '类' in list[list1[j][4] - 1] and '类' in list[list1[j][b] - 1]:
                            s = 'Type(' + list[list1[j][4] - 1] + ')' + '->' + 'Type(' + list[list1[j][b] - 1] + ')'
                        elif '类' in list[list1[j][4] - 1] and '类' not in list[list1[j][b] - 1]:
                            s = 'Type(' + list[list1[j][4] - 1] + ')' + '->' + 'F(' + list[list1[j][b] - 1] + ')'
                        elif '类' not in list[list1[j][4] - 1] and '类' in list[list1[j][b] - 1]:
                            s = 'Animal(' + list[list1[j][4] - 1] + ')' + '->' + 'Type(' + list[list1[j][b] - 1] + ')'
                        elif '类' not in list[list1[j][4] - 1] and '类' not in list[list1[j][b] - 1]:
                            s = 'Animal(' + list[list1[j][4] - 1] + ')' + '->' + 'F(' + list[list1[j][b] - 1] + ')'
                            # s = list[list1[j][4] - 1] + '->' + list[list1[j][b] - 1]
                    if m > 1 and b < m - 1:
                        if '类' not in list[list1[j][b] - 1]:
                            s = '+' + 'F(' + list[list1[j][b] - 1] + ')' + s
                        elif '类' in list[list1[j][b] - 1]:
                            s = '+' + 'Type(' + list[list1[j][b] - 1] + ')' + s
                            # s = '+' + list[list1[j][b] - 1] + s
                    if m > 1 and b == m - 1:
                        if '类' in list[list1[j][4] - 1] and '类' in list[list1[j][b] - 1]:
                            s = 'Type(' + list[list1[j][4] - 1] + ')' + '->' + 'Type(' + list[list1[j][b] - 1] + ')' + s
                        elif '类' in list[list1[j][4] - 1] and '类' not in list[list1[j][b] - 1]:
                            s = 'Type(' + list[list1[j][4] - 1] + ')' + '->' + 'F(' + list[list1[j][b] - 1] + ')' + s
                        elif '类' not in list[list1[j][4] - 1] and '类' in list[list1[j][b] - 1]:
                            s = 'Animal(' + list[list1[n][b] - 1] + ')' + '->' + 'Type(' + list[list1[n][4] - 1] + ')' + s
                        elif '类' not in list[list1[j][4] - 1] and '类' not in list[list1[j][b] - 1]:
                            s = 'Animal(' + list[list1[n][b] - 1] + ')' + '->' + 'F(' + list[list1[n][4] - 1] + ')' + s
                            # s = list[list1[j][4] - 1] + '->' + list[list1[j][b] - 1] + s
                    print(s)
                dict['id'] = w
                dict['relu'] = s
                list_dic.append(dict)
        i += 1
        if i < len(input_features):
            flag = True
        else:
            flag = False
    print('结果==：',input_features)
    print('1', list_dic)

    for i in range(len(input_features)):
        for j in range(len(list)):
            if input_features[i] == j+1:
                input_features[i] = list[j]
    print('list',input_features)
    return list_dic,input_features

# 查询所有的知识
def search_feature():
    cursor1 = db.cursor()
    cursor1.execute('select * from features')
    data_feature = cursor1.fetchall()  # 元组特征
    list_f = []
    for i in data_feature:
        dict_f = {}
        dict_f['id'] = i[0]
        dict_f['features'] = i[1]
        print(dict_f)
        list_f.append(dict_f)
    return list_f

# 查看所有规则
def searchRelu():
    list1_1 = useMysql_Relu_id()
    list_r = []
    for i in range(len(list1_1)):
        dict_r = {}
        for j in range(len(list1_1[1])):
            if j == 0:
                dict_r['id'] = list1_1[i][j]
            if j == 1:
                dict_r['f1'] = list1_1[i][j]
            if j == 2:
                dict_r['f2'] = list1_1[i][j]
            if j == 3:
                dict_r['f3'] = list1_1[i][j]
            if j == 4:
                dict_r['f4'] = list1_1[i][j]
            if j == 5:
                dict_r['console'] = list1_1[i][j]
        list_r.append(dict_r)
    print('111',list_r)
    return list_r

# 增加知识
def add_feature(feature):
    cursor = db.cursor()
    sql = "insert into features(feature) values('%s')"%(feature)
    # dict_add = {}
    # list_add = []
    try:
        cursor.execute(sql)
        db.commit()
        # dict_add['message'] = 1
        # list_add.append(dict_add)
        message = 1
        return message
    except:
        db.rollback()
        # dict_add['message'] = 0
        # list_add.append(dict_add)
        message = 0
        return message

# 增加规则
def add_relu(f1,f2,f3,f4,console):
    cursor = db.cursor()
    sql = "insert into relu(f1,f2,f3,f4,console) values('%d','%d','%d','%d','%d')" % (f1,f2,f3,f4,console)
    try:
        cursor.execute(sql)
        db.commit()
        message = 1
        return message
    except:
        db.rollback()
        message = 0
        return message

# 修改知识
def update_feature(id,feature):
    cursor = db.cursor()
    sql = "UPDATE features SET feature = '%s' WHERE id = '%d'"%(feature,id)
    try:
        cursor.execute(sql)
        db.commit()
        message = 1
        return message
    except:
        # 如果发生错误则回滚
        db.rollback()
        message = 0
        return message

# 修改规则
def update_relu(id,f1,f2,f3,f4,console):
    cursor = db.cursor()
    sql = "UPDATE relu SET f1 = '%d',f2 = '%d',f3 = '%d',f4 = '%d', console = '%d' WHERE id = '%d'" % (id,f1,f2,f3,f4,console)
    try:
        cursor.execute(sql)
        db.commit()
        message = 1
        return message
    except:
        # 如果发生错误则回滚
        db.rollback()
        message = 0
        return message

# 删除知识
def delete_feature(id):
    cursor = db.cursor()
    sql = "DELETE FROM features WHERE id = '%d'"%(id)
    try:
        cursor.execute(sql)
        db.commit()
        message = 1
        return message
    except:
        db.rollback()
        message = 0
        return message

# 删除规则
def delete_relu(id):
    cursor = db.cursor()
    sql = "DELETE FROM relu WHERE id = '%d'" % (id)
    try:
        cursor.execute(sql)
        db.commit()
        message = 1
        return message
    except:
        db.rollback()
        message = 0
        return message


# 查询所有规则
# def search():
#     for i in range(len(list1)):
#         m = 0
#         for j in range(4):
#             if list1[i][j] != 0:
#                 m += 1
#         for n in range(m):  # 4
#             if m == 1:
#                 print(list[list1[i][n]-1]+'->'+list[list1[i][4]-1])
#             if m > 1 and n < m-1:
#                 print(list[list1[i][n]-1]+'+',end='')
#             if m > 1 and n == m-1:
#                 print(list[list1[i][n]-1]+'->'+list[list1[i][4]-1])
#         print('\t')

if __name__ == '__main__':
    # pass

    # test()
    # forward(1,10,14,0)
    # forward(1,0,0,0)
    backward(31)
    # print(search_feature())
    # searchRelu()
    # print(update_feature(9,'眼睛盯前面'))
    # search()

