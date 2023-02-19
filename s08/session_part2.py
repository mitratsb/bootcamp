class Person:
    contact_list=[]
    
    
    def __init__(self,full_name,number,network):
        self.full_name=full_name
        self.number=number
        self.network=network
        print(f'{self.full_name} was added in phonebook.')
        # contact_list.update({self.full_name:self.number})
        
    def calling(self):
        return f'calling {self.full_name}...\nnumber:{self.number}'
    
    def texting(self):
        print(f'texting {self.full_name}')
        text=input("Enter text here: ")
        print(f'Message sent to {self.full_name}')
        
contact1=Person("Mahtab rezayi","09126567456","irancel")
contact2=Person("Mina sari","09387656789","MCI")

#فراخوانی

# print(contact1.full_name)

# print(contact1.calling())
# print(contact2.calling())

# print(contact1.texting())
# print(contact2.texting())

# print(Person.contact_list)


    
class Phonebook:
    
    def __init__(self,phonebook_name) -> None:
        self.phone