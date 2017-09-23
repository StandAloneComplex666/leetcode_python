# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:30:44 2017

@author: hp
"""

def transaction(price):
    max_profit = 0
    sell = price(0)
    
    for x in price:
        if price.index(x) > price.index(sell):
            if sell - x > max_profit :
                max_profit = sell - x
    return max_profit

if __name__ == '__main__':
    price = [7 ,1 ,5, 3, 6, 4]
    money = transaction(price)
            
            