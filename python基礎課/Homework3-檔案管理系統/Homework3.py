import os
import codecs


class folder_system:
    def __init__(self):
        self.path = os.getcwd()
        self.folder_list = []
        self.file_list = []

    def main(self):
        while True:

            print(f'工作路徑:{self.path}')
            self.menu()
            self.basic()
            try:
                user_input = int(input('操作:'))
                os.system('cls')
            except Exception as e:
                print(f'!error {e}')

            if user_input == 0:
                break
            elif user_input == 1:
                self.function1()
            elif user_input == 2:
                self.function2()
            elif user_input == 3:
                self.function3()
            elif user_input == 4:
                self.function4()
            elif user_input == 5:
                self.function5()
            elif user_input == 6:
                self.function6()
            elif user_input == 7:
                self.function7()
            elif user_input == 8:
                self.function8()

    def basic(self):
        self.file_list = []
        self.folder_list = []
        # print(os.listdir())
        total_list = os.listdir(self.path)
        for ele in total_list:
            a = self.path + '\\' + ele
            if os.path.isfile(a):
                self.file_list.append(ele)
            else:
                self.folder_list.append(ele)

    def menu(self):
        print('\t(0) 離開程式')
        print('\t(1) 列出檔案')
        print('\t(2) 列出資料夾')
        print('\t(3) 顯示檔案內容')
        print('\t(4) 刪除檔案')
        print('\t(5) 執行檔案')
        print('\t(6) 進入資料夾')
        print('\t(7) 刪除資料夾')
        print('\t(8) 回上層資料夾')

    def function1(self):
        for i in range(len(self.file_list)):
            print(f'\t{i} {self.file_list[i]}')
        print('\n')

    def function2(self):
        for i in range(len(self.folder_list)):
            print(f'\t{i} {self.folder_list[i]}')
        print('\n')

    def function3(self):
        self.function1()
        try:
            user_input = int(input('請輸入檔案索引:'))
        except Exception as e:
            print(f'!error {e}')
        path = os.path.join(self.path, self.file_list[user_input])
        # print(path)
        try:
            with codecs.open(path) as f:
                x = f.read()
        except Exception as e:
            print(e)
        os.system('cls')
        print('=====================檔案開始============================')
        print(x)
        print('=====================檔案結束============================')

    def function4(self):
        '''刪除檔案'''
        self.function1()
        try:
            user_input = int(input('請輸入檔案索引:'))
        except Exception as e:
            print(f'!error {e}')
        path = os.path.join(self.path, self.file_list[user_input])
        os.remove(path)
        os.system('cls')

    def function5(self):
        '''執行檔案'''
        self.function1()
        try:
            user_input = int(input('請輸入檔案索引:'))
        except Exception as e:
            print(f'!error {e}')
        path = os.path.join(self.path, self.file_list[user_input])
        os.popen(path)
        os.system('cls')

    def function6(self):
        '''進入資料夾'''
        self.function2()
        try:
            user_input = int(input('請輸入檔案索引:'))
        except Exception as e:
            print(f'!error {e}')
        path = os.path.join(self.path, self.folder_list[user_input])
        # print(path)
        self.path = path
        os.system('cls')

    def function7(self):
        '''刪除資料夾'''
        self.function2()
        try:
            user_input = int(input('請輸入檔案索引:'))
        except Exception as e:
            print(f'!error {e}')
        path = os.path.join(self.path, self.folder_list[user_input])
        # print(path)
        os.rmdir(path)
        os.system('cls')

    def function8(self):
        '''回上層資料夾'''
        path = self.path.split('\\')
        # print(path)
        k = path.pop()
        # print(path)
        path0 = '\\'.join(path)
        # print(path0)
        self.path = path0


a = folder_system()
a.main()