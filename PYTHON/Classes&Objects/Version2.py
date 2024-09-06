3  # self means pointer to itself
class Dishes:
    def __init__(self):
        self.DishNo = int(input('Enter the DishN0:'))
        self.DishName = input('Enter the DishName:')
        self.Price = int(input('Enter the Price:'))
        self.Discription = input('Enter the Dish Discription:')

    def display(self):
        print(self.DishNo)
        print(self.DishName)
        print(self.Price)
        print(self.Discription)

# Main Program starts here :
dish1=Dishes()
dish2=Dishes()
dish1.display()
dish2.display()
