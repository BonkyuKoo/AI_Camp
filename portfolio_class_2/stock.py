class Stock:
    def __init__(self, name, share, price):
        self.Name = name
        self.Share = share
        self.Price = price 
     
    def Get_Name(self):
        return self.Name
    
    def Get_Share(self):
        return self.Share
    
    def Get_Price(self):
        return self.Price
    
    def Set_Price(self, price):
        self.Price = price
