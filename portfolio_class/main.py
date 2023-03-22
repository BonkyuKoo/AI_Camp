import report
import stock
from datetime import datetime

pre_portfolio = list()

def Update():
    for i in range(len(portpolio)):
        pre_portfolio.append(stock.Stock(portpolio[i].Get_Name(), portpolio[i].Get_Share(), portpolio[i].Get_Price()))
    
    for i in range(len(price)):
        for j in range(len(portpolio)):
             if portpolio[j].Get_Name() == price[i][0] and portpolio[j].Get_Price() != price[i][1]:                             
                portpolio[j].Set_Price(price[i][1])
    Display() 
          
# 출력
# Name : 종목
# Shares : 구매수량
# Price : 가격
# Change : 전날과 금액차이
def Display():
    print('#', datetime.today())    
    print('-----------------------------------------')
    print('Name'.rjust(6), 'Shares'.rjust(10), 'Price'.rjust(10), 'Change'.rjust(12))
    print('-----------------------------------------')

    for i in range(len(portpolio)):
        print(portpolio[i].Get_Name().rjust(6)
            , str(portpolio[i].Get_Share()).rjust(10)
            , str(portpolio[i].Get_Price()).rjust(10)
            , '{:+.2f}'.format(float(portpolio[i].Get_Price()) - float(pre_portfolio[i].Get_Price())).rjust(12))        
    print('-----------------------------------------')


# 메인
portpolio = report.read_portfolio('portfolio.csv')
price = report.read_price('prices.csv')
Update()

