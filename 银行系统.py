#存储用户账户信息
account_list = [{'account':'123','password':'123','figure':10},
                {'account':'456','password':'456','figure':20},
                {'account':'789','password':'789','figure':30}]
while True:
    print("=" * 12, "欢迎使用XX银行客户端", "=" * 14)
    print('尊敬的用户，您好！请登录!')
    ac = input('请输入您的账户信息：')
    for i in range(len(account_list)):
        if ac == account_list[i]['account']:
            ps = input('请输入您的密码：')
            if ps == account_list[i]['password']:
                print("=" * 40)
                print('{:^30}'.format('登陆成功!'))
                while True:
                    print("=" * 40)
                    print("{0:1} {1:13} {2:15}".format(" ", "1. 查询余额", "2. 存款"))
                    print("{0:1} {1:13} {2:15}".format(" ", "3. 取钱", "  4. 退出系统"))
                    print("=" * 40)
                    key = input("请输入您需要执行的操作：")
                    if key == "1":
                        print( "您的当前账户余额有{}元钱".format(account_list[i]['figure']))
                        input("按回车键继续：")
                    elif key == "2":
                        num = int(input('请输入您的存款金额：'))
                        account_list[i]['figure'] += num
                        print("您已存入{}元，您的当前账户余额有{}元钱".format(num,account_list[i]['figure']))
                        input("按回车键继续：")
                    elif key == "3":
                        while True:
                            num = int(input('请输入您的取款金额：'))
                            if num <= account_list[i]['figure']:
                                account_list[i]['figure'] -= num
                                print("您已取出{}元，您的当前账户余额有{}元钱".format(num,account_list[i]['figure']))
                                input("按回车键继续：")
                                break
                            else:print("当前余额不足,请重新输入")
                            continue
                    elif key == "4":
                        print(" " * 40)
                        print(" " * 40)
                        print("=" * 17, "再见", "=" * 17)
                        print(" " * 40)
                        print(" " * 40)
                        break
            else:
                print('用户密码错误！请重新登录！')

        else:
            continue

