hong = [75, 82, 95]
kim = [88, 64, 70]
lee = [100, 95, 70]

tot = [0, 0, 0]
tot[0] = sum(hong) 
tot[1] = sum(kim)
tot[2] = sum(lee)

print('홍길동, 총점=%s, 평균=%.1f' %(tot[0], tot[0]/len(hong)))
print('김철수, 총점=%s, 평균=%.1f' %(tot[1], tot[1]/len(kim)))
print('이영희, 총점=%s, 평균=%.1f' %(tot[2], tot[2]/len(lee)))