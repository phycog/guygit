
fb_stock_price = [12,22,36,59,38,50]


LL_head = 2



def printLL():
    i = LL_head
    if LL_head == 0:
       R = len(fb_stock_price) - 1
    else:
        R = len(fb_stock_price)
    while i < R:
        print(fb_stock_price[i])
        i = i + 1





printLL()