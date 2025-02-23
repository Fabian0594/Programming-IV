from io import *

#Realice un programa que recorra una lista llena de los objetos usuario que quieran, luego van a contar la cantidad que un usuario aparezca en la lista y luego debe decir si aparece una cantidad par o impar de veces. al diseñar las clases usted debe considerar los atrobutos que crea necesarios.

class user:
    
    profession = ""
    name = ""
    age = 0
    
    def insertData(self):
        self.profession = input("Enter your profession: ")
        self.name = input("Enter your name: ")
        self.age = int(input("Enter yor age: "))
        
    def returnData(self):
        return f"User(\nName: {self.name}\nProfession: {self.profession}\nAge: {self.age}\n )"
    
    def compareByName(self, other):
        return self.name == other.name
        
    def compareByProfession(self, other):
        return self.profession == other.profession
    
    def compareByAge(self, other):
        return self.age == other.age
        
        
        
def fillTheList():
        usersList = []
        while True:
            userTemp = user()
            userTemp.insertData()
            usersList.append(userTemp)
            if int(input("Enter 0 to exit or another number to continuo adding users: \n")) == 0:
                break;
        return usersList
    

          
          
users = fillTheList()

for i in range(len(users) - 1):
    print(users[i].compareByAge(users[i + 1]))   
    