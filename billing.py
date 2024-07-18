from datetime import datetime
name=input("enter your name:")
#LIST OF ITEMS:
lists='''
Rice  Rs.20kg
sugar Rs.30kg
salt  Rs.20kg
oil   Rs.80kg
'''
print(lists)
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates per items
items={'rice':20,'sugar':30,'salt':20,'oil':80}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)) :
    inp1=int(input("if you want to buy press 1 or 2 for exit")) 
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes 0r no:")
    if inp=='yes':
        pass             
        if finalamount!=0:
            print(25*"=","sarvesh supermarket",25*"=")
        print(28*" ","tadipatri")
        print("Name:",name,30*" ","date:",datetime.now())
        print(75*"-")
        print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
        for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*' ',qlist[i],8*" ",plist[i])
        print(75*"-")
        print(50*" ",'TotalAmount:','Rs',totalprice)
        print("gst amount",50*" ",'Rs',gst)
        print(75*"_")
        print(50*" ",'finalAmount:','Rs',finalamount)
        print(75*"-")
        print(50*" ","thanks for visiting")
            
        
                   
            
            
        
            
            
           
    
