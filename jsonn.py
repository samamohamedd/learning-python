import json

data = {}
data['pizza'] = {
    'name' : 'pizza',
    'size' : 'med',
    'price' : 200
}
data['burger'] = {
    'name' : 'burger',
    'size' : 'L',
    'price' : 250
}
data['cola'] = {
    'name' : 'cola',
    'size' : 'med',
    'price' : 21
}

s = json.dumps(data) #converting the object to data exchande format
#print(s)

with open('S:\college\programming\python\projects\data.txt' , 'r') as t:
    e = t.read()
    dic = json.loads(e) #conver it back to an object(dictionary)
    print(dic)
    print(dic['pizza']['price']) 
    print(type(dic)) 

