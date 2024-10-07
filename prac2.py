months = [31,28,31,30,31,30,31,31,30,31,30,31]
year = int(input("년 : "))
month = int(input("월 : "))
day = int(input("일 : "))
days = 0

if ((year % 4 == 0) and (year % 100 != 0) or (year % 400 ==0)) :
    months[1] = 29

# 1/1~5/5 : 1월+2월+3월+4월+5
# 방법1
for i in range(month -1):
    days += months[i]   # 1~4월 합
    
days += day  # (1~4월 합) + day
# 방법2
days = 0
days = sum(months[:month-1]) + day

print("1월 1일 부터 %d월 %d일 까지는 총 %d일 입니다" 
      %(month,day,days))
