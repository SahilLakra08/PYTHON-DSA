class pclass:
    def __init__ (self):
        self.rollno=int(input('Enter the RollNo:'))
        self.name=input('Enter the Name:')
        self.hindi=0
        self.english=0
        self.math=0
    def display_std(self):
        print(self.rollno)
        print(self.name)
        print(self.hindi)
        print(self.english)
        print(self.math)
    def perf_data(self):
        self.hindi=int(input('Hindi Marks: '))
        self.english=int(input('English Marks: '))
        self.math=int(input('Math Marks: '))

std1=pclass()
std1.display_std()
std1.perf_data()
std1.display_std()