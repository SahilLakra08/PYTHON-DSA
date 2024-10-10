class node:
    def __init__(self,d):
        self.data=d
        self.link= None

#main
start=node(15)
print(start.data)
ptr=node(50)
q=node(75)
print(ptr)
start.link=ptr
ptr.link=q
print(start.data,start.link.data,start.link.link.data)