import re,Event
import SportsView,SportsController,random
class SportsController():
    events={}
    
    def __init__(self):
        self.__events={}

    def add_event(self,name,date,location,province,price,finished):
        if(self.__events.get(name)==None):
            event= Event.Event(name,date,location,province,price,finished)
            self.__events[name] = event
            return True
        return False

    def addparticipant(self,nameevent,dni,name,age,email):
        event = (Event.Event) (self.__events.get(nameevent))
        if(event!=None):
            event.addParticipant(dni,name,age,email)
            return True
        return False
        
    def listpendingEvent(self,finished):
        list=[]
        for name,event in self.__events.items():
            if(event.getFinished()==finished):
                list.append(event)
        return list

    def finishrandom(self,name):
        
        event = (Event.Event) (self.__events.get(name))
        list=event.getParticipants()
        if(event!=None):
            if(event.getFinished==False):
                event.finished()
                random.choice([list])
            return True
        return False



                
            