# portfolio 파일 오픈해서 리스트로 저장
# price 파일과 바교해서 가격이 갱신됬다면 업데이트 
# 최종적으로 가격과 이전가격과의 +,-
# total cost 출력

import csv
from datetime import datetime

Stock_list = list()
Stock_list_update = list()
Stock_list_pre = list()       

# 파일 불러오기 -> 리스트에 저장
def File_Open(filename, type):
    if type == 'A':
        with open(filename) as f:
            reader = csv.reader(f)      
            header = next(reader)
            for row in reader:
                Stock_list.append([row[0], int(row[1]), float(row[2])])  

    elif type == 'B':
        with open(filename) as f:
            reader = csv.reader(f)     
            for row in reader:
                try:
                    Stock_list_update.append([row[0], float(row[1])])      
                except IndexError:
                    pass

#price 업데이트
#Name이 같은 것을 찾고 (index를 찾기)
#price 변경 전 Stock_list_pre리스트에 원본을 저장한다. 
#찾은 index를 가지고 Stock_list에 Stock_list_update의 price값으로 바꾼다                     
def Update():
    for i in range(len(Stock_list)):
        Stock_list_pre.append([Stock_list[i][0], Stock_list[i][1], Stock_list[i][2]])

    for i in range(len(Stock_list_update)):
        for j in range(len(Stock_list)):
             if Stock_list[j][0] == Stock_list_update[i][0] and Stock_list[j][2] != Stock_list_update[i][1]:                             
                Stock_list[j][2] = Stock_list_update[i][1]
    Display()                         
          
# 출력
# Name : 종목
# Shares : 구매수량
# Price : 가격
# Net Change : 전날대비 가격
# Total Cost : 종목별 총 금액
def Display():
    print('#', datetime.today())    
    print('----------------------------------------------------------')
    print('Name'.ljust(8), 'Shares'.ljust(10), 'Price'.ljust(12), 'Net Change'.ljust(14), 'Total Cost'.ljust(16))
    print('----------------------------------------------------------')
    for i in range(len(Stock_list)):
        print(Stock_list[i][0].ljust(8)
              , str(Stock_list[i][1]).ljust(10)
              , str(Stock_list[i][2]).ljust(12)
              , '{:+.2f}'.format(float(Stock_list[i][2]) - float(Stock_list_pre[i][2])).ljust(14)
              , '{:,.1f}'.format(int(Stock_list[i][1]) * Stock_list[i][2]).ljust(16))
    print('----------------------------------------------------------')

# 메인
File_Open('portfolio.csv', 'A')
File_Open('prices.csv', 'B')
Update()

