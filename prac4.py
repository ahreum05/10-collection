juchajang = [False for i in range(5)]

while True :
    print('*'*20)
    print("\t1. 입차\n\t2. 출차\n\t3. 리스트\n\t4. 종료")
    print('*'*20)
    num = int(input('메뉴 : '))
    print()

    if num == 1:
        # 주차위치 : 1~5
        parking = int(input("위치 입력 : ")) 
        if juchajang[parking-1] == False:
            juchajang[parking-1] = True
            print("%d번위치에 주차되었습니다."%parking)
        else : print("%d번위치에 이미 주차되어있습니다."%parking)

    elif num == 2:
        # 주차위치 : 1~5
        parking = int(input("위치 입력 : "))
        if juchajang[parking-1] == True:
            juchajang[parking-1] = False
            print("%d번위치에 출차되었습니다."%parking)
        else : print("%d번위치에 주차되어 있지않습니다."%parking)

    elif num == 3:
        for i in range(len(juchajang)) :
            print("%s위치 : %s"%(i+1, juchajang[i]))

    elif num == 4:
        print("종료")
        break

    print()