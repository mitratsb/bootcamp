
class Father:
    
    def __init__(self,name,gender) -> None:
        self.name= name
        self.gender=gender
        
class Mother:
    
    def __init__(self,name,gender) -> None:
        self.name=name
        self.gender=gender
        
        
class Student(Father,Mother):
    
    def __init__(self,n) -> None:
        #این سوپر میره اینیت کلاس والد اولی رو میبینه و ازش با وریبل مقدار میگیره
        super().__init__()
    
obj1=Father("Reza","male")
obj2=Mother("Baran","female")
obj3=Student()
