#2017-12-12 틱택토.py
#중요 사실(?) 문자열 관련함수는 x = x.어쩌구 형식 리스트 관련은 그냥 해야한다  이유 궁금
#sort와 sorted 차이
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
Line_0 = "*************"
Line_1 = "* 1 * 2 * 3 *"
Line_2 = "* 4 * 5 * 6 *"
Line_3 = "* 7 * 8 * 9 *"
Count = 1
Player1 = list()
Player2 = list()
while True:
    Player1.sort()
    Player2.sort()
    print(Line_0)
    print(Line_1)
    print(Line_2)
    print(Line_3)
    print(Line_0)
    total = Line_1 + Line_2 + Line_3
    if Player1 == [1,2,3] or Player1 == [4,5,6]:
        print("Player1 승리")
        break
    elif Player1 == [7,8,9] or Player1 == [1,4,7]:
        print("Player1 승리")
        break
    elif Player1 == [2,5,8] or Player1 == [3,6,9]:
        print("Player1 승리")
        break
    elif Player1 == [1,5,9] or Player1 == [3,5,7]:
        print("Player1 승리")
        break
    if Player2 == [1,2,3] or Player1 == [4,5,6]:
        print("Player2 승리")
        break
    elif Player2 == [7,8,9] or Player1 == [1,4,7]:
        print("Player2 승리")
        break
    elif Player2 == [2,5,8] or Player1 == [3,6,9]:
        print("Player2 승리")
        break
    elif Player2 == [1,5,9] or Player2 == [3,5,7]:
        print("Player2 승리")
        break
    if total.count("O") == 5: #이떄는 1부터 세네 ㄷㄷ
        print("무승부")
        break
    if Count % 2 != 0:
        Count += 1
        print("Player1의 턴")
        Plinput = input("원하는 숫자를 입력하십시오:")
        if Plinput in Line_1:
            if Plinput == "1":
                Player1.append(1)
                Line_1 = Line_1.replace("1","O") #아뉘! 조심좀 해라 돌쇠스
            elif Plinput == "2":
                Player1.append(2)
                Line_1 = Line_1.replace("2","O")
            elif Plinput == "3":
                Player1.append(3)
                Line_1 = Line_1.replace("3","O")
        elif Plinput in Line_2:
            if Plinput == "4":
                Player1.append(4)
                Line_2 = Line_2.replace("4","O")
            elif Plinput == "5":
                Player1.append(5)
                Line_2 = Line_2.replace("5","O")
            elif Plinput == "6":
                Player1.append(6)
                Line_2 = Line_2.replace("6","O")
        elif Plinput in Line_3:
            if Plinput == "7":
                Player1.append(7)
                Line_3 = Line_3.replace("7","O")
            elif Plinput == "8":
                Player1.append(8)
                Line_3 = Line_3.replace("8","O")
            elif Plinput == "9":
                Player1.append(9)
                Line_3 = Line_3.replace("9","O")
        else:
            print("이상한 수를 입력하셨습니다.")
    else:
        Count += 1
        print("Player2의 턴")
        Pl2input = input("원하는 숫자를 입력하세요:")
        if Pl2input in Line_1:
            if Pl2input == "1":
                Player2.append(1)
                Line_1 = Line_1.replace("1","X") #아뉘! 조심좀 해라 돌쇠스
            elif Pl2input == "2":
                Player2.append(2)
                Line_1 = Line_1.replace("2","X")
            elif Pl2input == "3":
                Player2.append(3)
                Line_1 = Line_1.replace("3","X")
        elif Pl2input in Line_2:
            if Pl2input == "4":
                Player2.append(4)
                Line_2 = Line_2.replace("4","X")
            elif Pl2input == "5":
                Player2.append(5)
                Line_2 = Line_2.replace("5","X")
            elif Pl2input == "6":
                Player2.append(6)
                Line_2 = Line_2.replace("6","X")
        elif Pl2input in Line_3:
            if Pl2input == "7":
                Player2.append(7)
                Line_3 = Line_3.replace("7","X")
            elif Pl2input == "8":
                Player2.append(8)
                Line_3 = Line_3.replace("8","X")
            elif Pl2input == "9":
                Player2.append(9)
                Line_3 = Line_3.replace("9","X")
        else:
            print("이상한 수를 입력하셨습니다.")
print("게임 종료")
