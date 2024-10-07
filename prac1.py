score = []
tot = 0

#for i in range(5): 
for i in range(1, 6): 
    num = int(input('%s번 학생의 점수를 입력 : ' % i))
    score.append(num)

# 총점 구하기 1
for i in range(len(score)):
    tot += score[i]
# 총점 구하기 2
tot = sum(score)    
    
avg = tot / len(score)

print('총점 : %s  평균 : %s' % (tot, avg))