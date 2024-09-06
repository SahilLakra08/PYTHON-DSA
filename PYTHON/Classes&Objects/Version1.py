  # self means pointer to itself
class Dishes:
    RestaurantName='CafeCoffeeDay'
    def __init__(self,DishN0,DishName,Price,Discription):
        self.DishNo = DishN0
        self.DishName = DishName
        self.Price = Price
        self.Discription = Discription

    def display(self):  
        print(self.DishNo)
        print(self.DishName)
        print(self.Price)
        print(self.Discription)

# Main Program starts here :
dish1=Dishes(1,'Dosa',70,'South Indian Dish')
dish2=Dishes(2,'Rajma Rice',100,'North Indian Dish')
print(Dishes.RestaurantName)
dish1.display()
dish2.display()