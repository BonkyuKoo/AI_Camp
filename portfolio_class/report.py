import csv
import stock

# 파일 불러오기 -> 리스트에 저장
def read_portfolio(filename):
    Stock_list = list()
    with open(filename) as f:
        reader = csv.reader(f)      
        header = next(reader)
        
        for row in reader:
           Stock_list.append(stock.Stock(row[0], int(row[1]), float(row[2])))
    return Stock_list
              
      

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