num=int(input("write a cost that you bought a Strawberries for? "))
sel=int(input("write a cost that you sold a Strawberrries for? "))
if num > sel:
    print("You made a loss in money by",num-sel)
else:
    print("You made a profit in money by",sel-num)