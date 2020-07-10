import pymysql
import os
import prettytable

class system0:
    def __init__(self):
        self.title = ['編號', '姓名', '生日', '地址', '電話']

    def menu(self):
        print('(0) 離開程式\n(1) 顯示會員列表\n(2) 新增會員資料\n(3) 更新會員資料\n(4) 刪除會員資料\n(5) 新增會員的電話\n(6) 刪除會員的電話')
        user_input = input('>>指令:')
        os.system('cls')
        return user_input

    def function1(self):
        connect_DB = pymysql.connect(host=self.host0,
                                     user='root',
                                     passwd=self.passwd0,
                                     db='python_ai',
                                     charset='utf8')

        cursor = connect_DB.cursor()

        cursor.execute('SELECT `a`.*, `b`.`tel` FROM `member` AS `a` LEFT JOIN `tel` AS `b` ON `a`.`id`=`b`.`member_id`')

        r = cursor.fetchall()
        table = prettytable.PrettyTable(self.title, encoding='utf8')

        # 我選用id作為比較的依據，因為不同會員的id一定不同
        last_id = None # 用來記錄上一輪的id
        for ele in r:

            # 這一輪id 與 上一輪id 相同，則代表是同一個會員。我就把電話以外的欄位設定成空字串
            if ele[0] == last_id:
                #ele[0] = ''
                table.add_row(['', '', '', '', ele[4]])
            # 這一輪id 與 上一輪id 不同，代表不同會員。
            else:
                table.add_row([ele[0], ele[1], ele[2], ele[3], ele[4]])

            # 把這一輪的id放進變數"上一輪id"，供比對用
            last_id = ele[0]
        print(table)

        connect_DB.close()
    def function2(self):
        name0  = input('>> 請輸入會員姓名: ')
        birth0 = input('>> 請輸入會員生日: ')
        addr0  = input('>> 請輸入會員地址: ')
        connect_DB = pymysql.connect(host=self.host0,
                                     user='root',
                                     passwd=self.passwd0,
                                     db='python_ai',
                                     charset='utf8')

        cursor = connect_DB.cursor()

        cursor.execute('INSERT INTO `member`(`name`, `birthday`, `address`)'+'VALUES(%s, %s, %s)',[name0, birth0, addr0])
        connect_DB.commit()
        connect_DB.close()

    def function3(self):
        self.function1()
        memberID = input('>> 請輸入你要修改的資料編號: ')
        name0  = input('>> 請輸入會員姓名: ')
        birth0 = input('>> 請輸入會員生日: ')
        addr0  = input('>> 請輸入會員地址: ')
        connect_DB = pymysql.connect(host=self.host0,
                                     user='root',
                                     passwd=self.passwd0,
                                     db='python_ai',
                                     charset='utf8')

        cursor = connect_DB.cursor()

        cursor.execute('UPDATE `member` SET `name`=%s,`birthday`=%s,`address`=%s WHERE `id`=%s',[name0, birth0, addr0, memberID] )
        connect_DB.commit()
        connect_DB.close()

    def function4(self):
        self.function1()
        memberID = input('>> 請輸入你要刪除的資料編號: ')

        connect_DB = pymysql.connect(host=self.host0,
                                     user='root',
                                     passwd=self.passwd0,
                                     db='python_ai',
                                     charset='utf8')

        cursor = connect_DB.cursor()

        cursor.execute('DELETE FROM `member` WHERE `id`=%s',[memberID])
        connect_DB.commit()
        connect_DB.close()
        os.system('cls')

    def function5(self):
        # 新增會員電話
        self.function1()
        memID  = input('>> 請選擇要添加電話的會員編號: ')
        tel0   = input('>> 請輸入電話:')
        connect_DB = pymysql.connect(host=self.host0,
                                     user='root',
                                     passwd=self.passwd0,
                                     db='python_ai',
                                     charset='utf8')

        cursor = connect_DB.cursor()

        cursor.execute('INSERT INTO `tel`(`member_id`, `tel`)'+'VALUES(%s, %s)',[memID, tel0])
        connect_DB.commit()
        connect_DB.close()

    def function6(self):
        # 刪除會員電話
        self.function1()
        memberID = input('>> 請輸入要刪除電話的會員編號: ')

        connect_DB = pymysql.connect(host=self.host0,
                                     user='root',
                                     passwd=self.passwd0,
                                     db='python_ai',
                                     charset='utf8')

        cursor = connect_DB.cursor()

        cursor.execute('SELECT * FROM `tel` WHERE `member_id`=%s',[memberID])

        r = cursor.fetchall()
        table0 = prettytable.PrettyTable([self.title[0], self.title[4]], encoding='utf8')
        print(r)
        for ele in r:
            #print(ele)
            table0.add_row([ele[0], ele[2]])
        print(table0)
        telID = input('>> 請輸入要刪除電話的電話編號: ')

        cursor.execute('DELETE FROM `tel` WHERE `id`=%s',[telID])
        connect_DB.commit()

        connect_DB.close()
        os.system('cls')


    def main(self):
        os.system('cls')

        self.host0 = 'localhost'
        self.passwd0 = input('>> 請輸入資料庫root密碼: ')
        #host0 = 'localhost:' + input('\n>> 請輸入資料庫的Port: ')

        os.system('cls')
        while True:
            k = self.menu()
            if k == '0':
                break
            elif k == '1':
                self.function1()
            elif k == '2':
                self.function2()
            elif k == '3':
                self.function3()
            elif k == '4':
                self.function4()
            elif k == '5':
                self.function5()
            elif k == '6':
                self.function6()

if __name__ == '__main__':
    main = system0()
    main.main()
