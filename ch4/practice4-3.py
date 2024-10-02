# 使⽤者輸入好友名與⾝上現⾦， 輸入完後以 dictionary ⽅式儲存好友資訊 
# 之後讓使⽤者輸入欲借⾦額，便會顯⽰可借錢給他的好友姓名以及總數
# 請問有幾個好友? 5 
# 請輸入第1個好友名與⾝上現⾦: Mary 2000 
# 請輸入第2個好友名與⾝上現⾦: John 1000 
# 請輸入第3個好友名與⾝上現⾦: Sue 800 
# 請輸入第4個好友名與⾝上現⾦: Linda 1200 
# 請輸入第5個好友名與⾝上現⾦: Ken 500 
# -------------------------------------------------- 
# 請輸入欲借現⾦: 1200 
# 可借錢的好友: Mary, Linda, 共2⼈


num_friend = int(input(f"請問有幾個好友? "))
friend_dict = {}
for i in range(num_friend):
    # 方法一
    friend_list = input(f"請輸入第{i+1}個好友名宇身上現金: ").split()
    friend_dict[friend_list[0]] = int(friend_list[1])
    # 方法二
    name, cash = input(f"請輸入第{i+1}個好友名宇身上現金: ").split()
    friend_dict[name] = int(cash)

print(f"--------------------")
money = int(input(f"請輸入欲借現金: "))
ok = 0
print(f"可借錢的好友:", end = " ")
for key, value in friend_dict.items():
    if money <= value:
        ok += 1
        print(f"{key}", end = ", ")
print(f"共{ok}人")


