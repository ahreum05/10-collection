scores = []
num_students = 5

for i in range(1, num_students + 1):
    score = int(input('%d번 학생의 점수를 입력 : ' % i))
    scores.append(score)
    
 #등수 리스트
ranks = [1] * num_students
#ranks = [1 for i in range(5)]
print(ranks)

# 점수 비교
for i in range(num_students):       # 기준값
    for j in range(num_students):   # 비교값
        if scores[i] < scores[j]:
            ranks[i] += 1
            
# 결과 출력
print()
print("결과:")
for i in range(num_students):
    print('%d점 : %d등' % (scores[i], ranks[i]))   

print('-' * 20)

for s, r in zip(scores, ranks):
    print('%d점 : %d등' %(s, r)) 
         
