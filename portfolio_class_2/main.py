import report
from datetime import datetime
          
# 출력
# Name : 종목
# Shares : 구매수량
# Price : 가격
# Change : 전날과 금액차이
# input : report list
# output : None
def Display(report):
    print('#', datetime.today())    
    print('-----------------------------------------')
    print('Name'.rjust(6), 'Shares'.rjust(10), 'Price'.rjust(10), 'Change'.rjust(12))
    print('-----------------------------------------')

    for i in range(len(report)):
        print(report[i][0].rjust(6)
            , report[i][1].rjust(10)
            , report[i][2].rjust(10)
            , '{:+.2f}'.format(report[i][3]).rjust(12))        
    print('-----------------------------------------')


# 하루에 한번 반복하도록 만들수 있을 것 같다.
# 일정 시간에 기존 포트폴리오 file1과 새로 갱신된 file2를 받아서 report를 출력
# input : portfolio filename, price filename
# output : None
def Routine(file1, file2):
    portpolio = report.read_portfolio(file1)
    price = report.read_price(file2)
    Display(report.Update(portpolio, price))

# Main
Routine('portfolio.csv', 'prices.csv')