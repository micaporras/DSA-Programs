# Test Program for Lab Assignment 3.3 - THE STOCK CLASS

from Stock import Stock

def main():
    # A stock object with stock symbol: INTC, name: Intel Corporation, 
    # previous closing price: 20.5, current price: 20.35
    stock = Stock("INTC", "Intel Corporation", 20.5, 20.35)
    print(f"The {stock.getName()}({stock.getSymbol()}) has a price-range percentage of {stock.getChangePercent()}%")

main()