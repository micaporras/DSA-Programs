# Designed Class for Lab Assignment 3.3 - THE STOCK CLASS

class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice
    
    def getName(self):
        return self.name
    
    def getSymbol(self):
        return self.symbol
    
    def getPreviousPrice(self):
        return self.previousClosingPrice
    
    def setPreviousPrice(self, previousPrice):
        self.previousClosingPrice = previousPrice
        return self.previousClosingPrice
    
    def getCurrentPrice(self):
        return self.getCurrentPrice
    
    def setCurrentPrice(self, currentPrice):
        self.currentPrice = currentPrice
        return self.currentPrice
    
    def getChangePercent(self):
        total = self.currentPrice + self.previousClosingPrice
        difference = self.currentPrice - self.previousClosingPrice
        percentage = (difference/total) * 100
        return round(percentage,4)
    

        
