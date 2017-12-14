# 2017-12-14 머드게임.py
# 2017 인기게임 배틀그라운드 머드 게임화
# 배틀로얄 장르가 아닌 하나의 모드로 나왔던 좀비 모드와 비슷하다
# 높은 스코어를 기록 하는 것이 목표

#변수 선언 영역
Main = """1.게임시작(S)
2.크레딧(C)
3.게임 종료(Q)"""

InGame = """1.이동(M)
2.탐색(S)
3.인벤토리(I)"""

Map = """1.로스 레오네스(L)
2.엘 포소(E)
3.몬테 누에보(M)
4.바예 델 마르(V)
5.군사 지대(C)
6.산 마르틴(S)
7.페카도(P)"""
#메뉴
while True:
    print(Main)
    UserInput= input("원하는 명령을 입력하세요:")
    UserInput = UserInput.upper()
    # 게임 시작
    if UserInput == "S":
        while True:
            MapNum = 2 # 시작 위치 (엘 포소) 번호가 맵 번호
            print(InGame)
            #현재 위치 출력
            if MapNum == 2: print("현재 위치:엘 포소")
            elif MapNum == 1: print("현재 위치: 로스 레오네스")
            elif MapeNum == 3: print("현재 위치: 몬테 누에보")
            elif MapNum == 4: print("현재 위치: 페카도")
            elif MapNum == 5: print("현재 위치:군사 지대")
            UserInput = input("원하는 명령을 입력하세요.")
            UserInput = UserInput.upper()
            #이동
            if UserInput == "M":
                print(Map)
            #탐색
            elif UserInput == "S":
                print()
            #인벤토리
            elif UserInput == "I":
                print()
            #오류
            else:
                print("에러)잘못된 명령")
                continue
    # 크레딧
    elif UserInput == "C":
        print("이 게임은 PUGB의 팬 게임입니다.")
    #게임 종료
    elif UserInput == "Q":
        print("게임을 종료합니다.")
        break
    #오류
    else:
        print("에러)잘못된 명령")
        continue
