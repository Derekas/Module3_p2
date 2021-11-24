import Event
import SportsView,datetime
import SportsController

events={}
def readname():
    while True:
        name=input("Introduce un nombre")
        if len(name)>0:
            return name
        else:
            print("Nombre no valido")
def readDNI():
    while True:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dni = input("Introduzca el DNI: ")
        letter=dni[-1].upper()
        number=dni[:-1]
    
        if(len(dni)!=9 and number.isdigit()):
            number=int(dni[:-1])
            return dni
        else:
            print("Format Incorrect")

def readdate():
    fecha = input("Introduzca la fecha: ")
    try:
        datetime.datetime.strptime(fecha, '%Y/%m/%d')
    except:
        return "El formato debe ser  YYYY/MM/DD"
    return datetime.datetime.strptime(fecha, '%Y/%m/%d')

def readLocation():
    while True:
        location=input("Introduce una localizacion")
        if len(location)>0:
            return location
        else:
            print("Localizacion no valido")

def readProvince():
    while True:
        province=input("Introduce una provincia")
        if len(province)>0:
            return province
        else:
            print("Provincia no valido")


def readFinished():
    while True:
        print("Introducir false si no se ha finalizado")
        print("Introducir true si se ha realizado finalizado")
        finished=input("Introduce true o false")
        if(finished=="true"):
            finished=True
            return finished
        elif(finished=="false"):
            finished=False
            return finished
        else:
            print("Error")


def readPrice():
    while True:
        price=float(input("Introduce un precio"))
        if len(price)>0:
            return price
        else:
            print("Precio no valida")



def calcularTotal(base,Vat):
    total=base*Vat
    return total

def menu():
    print("1, Add Event")
    print("2, Add participant to an event")
    print("3. List pending events with participants")
    print("4. List events finished with podium")
    print("5. Finish an event (It will randomly choose 3 participants and generate the podium of the 1st, 2nd and 3rd)")
    print("6. Exit")
    print("Choose option: ")

controller=SportsController.SportsController()
while True:
    menu()

    opcion=input("")
    if(opcion=="1"):

        name=readname()
        
        date=readdate()
        location=readLocation()
        province=readProvince()
        price=readPrice()

        finished=readFinished()
        if (controller.add_event(name,date,location,province,price,finished)):
            
            print("El evento se ha añadido correctamente")
        else:
            print("El evento no se ha podido añadir")

    elif(opcion=="2"):
        nameevent=readname()

        dni=input("Paticipant dni")
        name=readname()
        age=int(input("Participant age"))
        email=input("Paticipant email")
        controller.addparticipant(nameevent,dni,name,age,email)
    elif(opcion=="3"):
        list=controller.listpendingEvent(False)
        participants= event.getParticipants()
        for event in list:
            print("Event ",event.getName())
            print("\t data ",event.getDate())
            print("\t location ",event.getLocation())
            print("\t province ",event.getProvinces())
            print("\t price ",event.getPrice())
            for participant in participants:
                print("\t DNI ",participant[0])
                print("\t Name ",participant[1])
                print("\t Age ",participant[2])
                print("\t Email ",participant[3])

                
        
    elif(opcion=="4"):
        list=controller.listpendingEvent(True)
        podium= event.getPodium()
        for event in list:
            print("Event ",event.getName())
            print("\t data ",event.getDate())
            print("\t location ",event.getLocation())
            print("\t province ",event.getProvinces())
            print("\t price ",event.getPrice())
            for pod in podium:
                valor=podium[pod]
                print("Podium ", valor)
    
    elif(opcion=="6"):
        print("Saliendo..")
        break