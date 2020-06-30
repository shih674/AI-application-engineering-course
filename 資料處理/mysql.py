import pymysql

connect_database = pymysql.connect( host = 'localhost',
                                    user = 'root',
                                    passwd = '',
                                    db = '2020-06-30',
                                    charset = 'utf8'
                                    )

cursor = connect_database.cursor()

x = 'xxxx'
y = 'yyyy'
z = 'zzzzzzz'
'''
# 新增資料>型1
cursor.execute('INSERT INTO `news`(`title`, `source`, `create_time`, `description`)'+'VALUES(%s, %s, %s, %s)',['aaa', 'bbb','2020-06-30','cccccccc'])
connect_database.commit()

#connect_database.close()

# 新增資料>型2:變化型
cursor.execute('INSERT INTO `news`(`title`, `source`, `create_time`, `description`)'+'VALUES(%s, %s, %s, %s)',[input('::title\n\t>>'), input('::source\n\t>>'), input('::create time\n\t>>'), input('::description\n\t>>')])
connect_database.commit()

# 新增資料>型3:變化型 不用LIST用DIC
cursor.execute('INSERT INTO `news`(`title`, `source`, `create_time`, `description`)'+'VALUES(%(a)s, %(b)s, %(c)s, %(d)s)',{'a':input('::title\n\t>>'), 'b':input('::source\n\t>>'), 'c':input('::create time\n\t>>'), 'd':input('::description\n\t>>')})
connect_database.commit()

# 刪除資料
cursor.execute('DELETE FROM `news` WHERE `id`=%s',[input('::id\n\t>>')])
connect_database.commit()
'''
# 搜尋資料 fetchall
cursor.execute('SELECT * FROM `news`')
r = cursor.fetchall()
for ele in r:
    print(ele[0], ele[1], ele[2])

# 搜尋資料 fetchone
cursor.execute('SELECT * FROM `news`')
first = cursor.fetchone()
print('\nfirst', first[0], first[1], first[2])
second= cursor.fetchone()
print('\nsecond', second[0], second[1], second[2])
# 沒有下一個會回傳錯誤

# rowcount
cursor.execute('SELECT * FROM `news`')
print('\nrowcount:', cursor.rowcount())

connect_database.close()