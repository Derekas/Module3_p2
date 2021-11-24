class Event():
    
    def __init__(self,nameevent,date,location,province,price):
        self.__nameevent=nameevent
        self.__date=date
        self.__location=location
        self.__province=province
        self.__price=price
        self.__total=0
        self.__participants=[]
        self.__finished=False
        self.__podium={}

    def getNameevent(self):
        return self.__nameevent
    def getDate(self):
        return self.__date
    def getLocation(self):
        return self.__location
    def getProvince(self):
        return self.__province
    def getPrice(self):
        return self.__price
    def getTotal(self):
        return self.__total
    def getParticipants(self):
        return self.__participants
    def getFinished(self):
        return self.__finished
    def getPodium(self):
        return self.__podium
    

    def setName(self,name):
        self.__nameevent=name
    def setDate(self,date):
        self.__date=date
    def setLocation(self,location):
        self.__location=location
    def setProvince(self,province):
        self.__province=province
    def setPrice(self,price):
        self.__price=price

    def addParticipant(self,dni, name,age, email):
        self.__participants.append((dni,name,age,email))
        self.__total += self.__price
        
    def finished(self):
        self.__finished=True