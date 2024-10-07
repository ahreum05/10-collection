students = []

for i in range(3) :
    student = {}
    student['name'] = input('이름 입력: ')
    student['kor'] = int(input('국어 입력: '))
    student['eng'] = int(input('영어 입력: '))
    student['mat'] = int(input('수학 입력: '))
    student['tot'] = student['kor'] + student['eng'] + student['mat']
    student['avg'] = student['tot'] / 3 
    
    students.append(student)
    print()
# 리스트로 출력
print(students)
print('-' * 20)

'''
students = []

for i in range(3) :
    name = input('이름 입력: ')
    kor = int(input('국어 입력: '))
    eng = int(input('영어 입력: '))
    mat = int(input('수학 입력: '))
    tot = kor + eng + mat
    avg = tot / 3
    
    student = {'name': name, 'kor': kor, 'eng': eng, 
               'mat': mat, 'tot': tot, 'avg': avg}
    
    students.append(student)
    print()
# 리스트로 출력
print(students)
print('-' * 20)

# 딕셔너리로 출력
for i in range(len(students)) :
    print(students[i])
'''


