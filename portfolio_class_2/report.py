import csv
import stock

# 포트폴리오 파일 읽어오기
# input : csv file
# output : Stock_list(name, shares, price)
def read_portfolio(filename):
    Stock_list = list()
    with open(filename) as f:
        reader = csv.reader(f)      
        header = next(reader)
        
        for row in reader:
           Stock_list.append(stock.Stock(row[0], int(row[1]), float(row[2])))
    return Stock_list
              
      
# 갱신된 가격 파일 읽어오기
# input : csv file
# output : Stock_list_update(name, price)
def read_price(filename):
    Stock_list_update = list()
    with open(filename) as f:
        reader = csv.reader(f)     
        for row in reader:
            try:
                Stock_list_update.append((row[0], float(row[1])))      
            except IndexError:
                pass
    return Stock_list_update


#기존 포트폴리오에 갱신된 가격을 저장하고 report리스트를 작성한다.
# input : portpolio list, price list
# output : report (name, shares, price, change)
def Update(portpolio, price):
    pre_portfolio = list()
    report = list()

    for i in range(len(portpolio)):
        pre_portfolio.append(stock.Stock(portpolio[i].Get_Name(), portpolio[i].Get_Share(), portpolio[i].Get_Price()))
    
    for i in range(len(price)):
        for j in range(len(portpolio)):
             if portpolio[j].Get_Name() == price[i][0] and portpolio[j].Get_Price() != price[i][1]:                             
                portpolio[j].Set_Price(price[i][1])

    for i in range(len(portpolio)):        
        report.append((portpolio[i].Get_Name()
                      , str(portpolio[i].Get_Share())
                      , str(portpolio[i].Get_Price())
                      , float(portpolio[i].Get_Price()) - float(pre_portfolio[i].Get_Price())))

    return report
 