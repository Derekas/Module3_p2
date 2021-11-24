class Patient():
    def __init__(self,dni,name,surname,year_of_birth,telefone,email):
        self.__dni=dni
        self.__name=name
        self.__surname=surname
        self.__year_of_birth=year_of_birth
        self.__telefone=telefone
        self.__email=email
        self.__historyOfVisits = []
        self.__number_visits=0
        
    def __str__(self):
        return self.name
    
    def getDni(self):
        return self.__dni
    def getName(self):
        return self.__name
    def getSurname(self):
        return self.__surname
    def getYear_of_birth(self):
        return self.__year_of_birth
    def getTelefone(self):
        return self.__telefone
    def getEmail(self):
        return self.__email
    def gethistoryofvisits(self):
        return self.__historyOfVisits

    def getNumber_visits(self):
        return self.__number_visits

    def setDni(self,dni):
        self.__dni=dni
    def setName(self,name):
        self.__name=name
    def setName(self,surname):
        self.__surname=surname
    def setYear_of_birth(self,year_birth):
        self.__year_of_birth=year_birth
    def setTelefone(self,telefone):
        self.__telefone=telefone
    def setEmail(self,email):
        self.__email=email

    def setNumber_visits(self,number_visits):
        self.__number_visits=number_visits