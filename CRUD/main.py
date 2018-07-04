"""
C R U D

Create

Read

Update

Delete

"""
from mongoengine import *
connect('store', host='localhost', port=27017)


class Stock(Document):
  name= StringField(required=True, max_length=200)
  price= DecimalField(required=True)
  description=StringField(requiled=False)




def Create(name, price, description):
    Stock(name=name, price=price, description=description).save()

def readAll():

    for i in range(0,len(Stock.objects.all())):
        print('ID: %s'%(Stock.objects.all()[i].id))
        print("Name: "+Stock.objects.all()[i].name+'. Price %s Description: %s'%(Stock.objects.all()[i].price, Stock.objects.all()[i].description))
        print(" ")
def readOne():
    pass

def update():
    pass

def delete():
    pass

#Create("phone",20000,"its expensive")
readAll()
