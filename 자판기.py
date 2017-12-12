# 2017-12-12 자판기.py
write = """먹고 싶은 음료를 선택하세요
1. 코카콜라
2. 펩시
3. 맥콜
4. 칠성사이다 """
money = 5000
while money:
    print(write)
    number = int(input("먹고 싶은 음료의 번호를 입력하세요:"))
    if number == 1:
        if money >= 500:
            print("코카콜라를 먹었습니다.")
            money -= 500
            print("잔고: {0}".format(money))
        else:
            print("잔액이 부족합니다.")
            continue
    elif number == 2:
        if money >= 300:
            print("펩시를 먹었습니다.")
            money -= 300
            print("잔고:{}".format(money))
        else:
            print("잔액이 부족합니다.")
            continue
    elif number == 3:
        if money >= 1000:
            print("맥콜을 먹었습니다")
            money -= 1000
            print("잔고: {money}".format(money))
        else:
            print("잔액이 부족합니다.")
            continue
    else:
        print("이상한 숫자를 입력했습니다.")
