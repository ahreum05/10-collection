# 방법1
student = {}

student['name'] = input('이름 입력: ')
student['kor'] = int(input('국어 입력: '))
student['eng'] = int(input('영어 입력: '))
student['mat'] = int(input('수학 입력: '))
student['tot'] = sum((student['kor'], student['eng'], student['mat']))
#student['tot'] = student['kor'] + student['eng'] + student['mat']
student['avg'] = student['tot']/3

print(student)
print('-' * 20)

# 방법2
name = input('이름 입력: ')
kor = int(input('국어 입력: '))
eng = int(input('영어 입력: '))
mat = int(input('수학 입력: '))
tot = kor + eng + mat
avg = tot / 3

student = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat,
           'tot': tot, 'avg': avg}
print(student)
print('-' * 20)


