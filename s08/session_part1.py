#OOP

class Student:
    school="Mahan"
    
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id
        
    
    def __repr__(self) -> str:
        return "repr"
    
    def __str__(self) -> str:
        return "str"
    
    country="iran"
    
    def say_hello(self):
        print(self)  
        print("hello")
        
        
    @staticmethod
    def say_bye():
        print("bye")
        
#giving object
mina = Student()

#فراخوانی
mina.say_hello()     #تابع
mina.say_bye()       #تابع

#attribute
print(mina.country)
print(Student.country)

# print(mina) #executes str func. if we don't have it and we only have repr, it executes repr func






