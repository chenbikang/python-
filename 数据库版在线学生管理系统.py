#导入pymsql模块
import pymysql

class Stu:
    def __init__(self,db):
        #获取数据库连接
        self.db = pymysql.connect(host="localhost",user="root",password="",db=db,charset="utf8")
        # 创建游标对象
        self.cursor = self.db.cursor()


    #查询
    def findAll(self):
        sql = "select * from stu"

        try:
            # 执行sql操作
            self.cursor.execute(sql)
            print("一共有{}人".format(self.cursor.rowcount))
            # 使用fetchone（）
            while True:
                data = self.cursor.fetchone()
                if data == None:
                    break
                print(data)
        except Exception as err:
            print("SQL执行错误！原因：", err)

    def dele(self,id):
        # 定义sql语句
        sql = "delete from stu where id=%d" % (id)

        try:
            # 执行sql操作
            m = self.cursor.execute(sql)
            # 事务提交
            self.db.commit()
            print("成功删除条数：", m)

        except Exception as err:
            # 事务回滚
            self.db.rollback()
            print("SQL执行错误！原因：", err)


    def insert(self,data):
        # 定义sql语句
        sql = "insert into stu (name,age,sex,classid) values ('%s','%d','%s','%s')" % (data)

        try:
            # 执行sql操作
            m = self.cursor.execute(sql)
            # 事务提交
            self.db.commit()

            print("成功添加条数：", m)

        except Exception as err:
            # 事务回滚
            self.db.rollback()
            print("SQL执行错误！原因：", err)

    def __delete__(self):
        # 关闭数据库连接
        self.db.close()


s = Stu("mydb")
print("=" * 12, "欢迎使用在线学生信息管理系统", "=" * 14)
while True:
    print("=" * 40)
    print("{0:1} {1:13} {2:15}".format(" ", "1. 查询", "2. 删除"))
    print("{0:1} {1:13} {2:15}".format(" ", "3. 添加", "4. 退出系统"))
    print("=" * 40)
    key = input("请输入您需要执行的操作：")
    if key == "1":
        s.findAll()
        input("按回车键继续：")
    elif key == "2":
        num = int(input('请输入您要删除的学生id：'))
        s.dele(num)
        input("按回车键继续：")
    elif key == "3":
        n = input('请输入添加的姓名：')
        a = int(input('请输入年龄：'))
        sex= input('请输入性别（w or m）：')
        c = input('请输入班级：')
        data = (n, a, sex, c)
        print(data)
        s.insert(data)
    elif key == "4":
        print(" " * 40)
        print(" " * 40)
        print("=" * 17, "再见", "=" * 17)
        print(" " * 40)
        print(" " * 40)
        break
