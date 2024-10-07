students = []

while True:
    print('''\
성적 관리 프로그램
------------------
1. 입력
2. 출력
3. 종료
------------------''')
    num = int(input('번호 : '))
    print()
    
    if num == 1:
        student = {}
        student['name'] = input('이름 : ')
        student['kor'] = int(input('국어 : '))
        student['eng'] = int(input('영어 : '))
        student['mat'] = int(input('수학 : '))
        student['tot'] = student['kor'] + student['eng'] + student['mat']
        student['avg'] = student['tot']/3
        # 리스트에 추가
        students.append(student)
    elif num == 2:
        print('이름\t\t국어\t영어\t수학\t총점\t평균')
        for s in students:
            st1 = '{name}\t{kor}\t{eng}\t{mat}\t{tot}\t{avg:.1f}'.format(**s)
            print(st1)
    elif num == 3:
        print("종료")
        break;
    
    print()


