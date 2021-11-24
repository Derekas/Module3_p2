import datetime
import Patient,ControllerPatient
patients={}
def readdni():
    while True:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dni = input("Introduzca el DNI: ")
        letter=dni[-1].upper()
        number=dni[:-1]
    
        if(len(dni)!=9 and number.isdigit()):
            number=int(dni[:-1])
            break
        else:
            print("Format Incorrect")


def readname():
    while True:
        name=input("Introduce un nombre")
        if len(name)>0:
            break
        else:
            print("Nombre no valido")

def readsurname():
    while True:
        surname=input("Introduce un nombre")
        if len(surname)>0:
            break
        else:
            print("Nombre no valido")

def readYear_of_birth():

    date=input("Read date: dd/mm/yyyy")
    dateparse=date.split("/")
    day=int(dateparse[0])
    month=int(dateparse[1])
    year=int(dateparse[2])
    print(day,month,year)
    print(datetime(year,month,day))

def readTelephone():
    while True:
        telephone=input("Introduce el numero de telefono")
        if len(telephone)>0:
            break
        else:
            print("Telefono no valido")

def reademail():
    while True:
        email=input("Introduce una provincia")
        if len(email)>0:
            break
        else:
            print("Correo no valido")
def menu():
    print("1, Add patient")
    print("2, Delete patient")
    print("3. Get Patient Hitory")
    print("4. List Patients")
    print("5. Add appointment")
    print("Choose option: ")


controller=ControllerPatient.ControllerPatient()
while True:
    menu()

    opcion=input("")
    if(opcion=="1"):

        dni=readdni()
        name=readname()
        surname=readsurname()
        yearofbirth=readYear_of_birth()
        telefono=readTelephone()
        email=reademail()
        
        if controller.add_patient(dni,name,surname,yearofbirth,telefono,email):
            print("El paciente se ha añadido correctamente")
        else:
            print("El paciente no se ha podido añadir")

    elif(opcion=="2"):
        dni=readdni()
        patient= controller.delpatient(dni)
        if (patient!=None):
            print("El paciente", patient.getName(),"a sido eliminado")
        else:
            print("El dni no existe")


    elif(opcion=="3"):
        dni=readdni()
        patient= controller.searchpatient(dni)
        if (patient!=None):
            print("History ", patient.gethistoryofvisits())
        else:
            print("El dni no existe")
    elif(opcion=="4"):
        print=("introduce el dni")
        dni=readdni()
        patient=controller.searchpatient(dni)
        list=controller.listPatient()
        for patient in list:
            print("Patient ",patient.getDni())
            print("\t Name ",patient.getName())
            print("\t Surname ",patient.getSurname())
            print("\t Year ",patient.getYear_of_birth())
            print("\t Telephone ",patient.getTelefone())
            print("\t Email ",patient.getEmail())
            print("\t Hisstory visits ",patient.gethistoryofvisits())
            print("\t Number visits ",patient.getNumber_visits())

        
    elif(opcion=="5"):
        from datetime import datetime
        now = datetime.now()
        format_date = now.strftime("%d/%m/%Y %H:%M")

        print=("Introduce el dni")
        dni=readdni()

        patient=controller.searchpatient(dni)

        print("\t Name ",patient.getName())
        print("\t Surname ",patient.getSurname())
        print("\t Telephone ",patient.getTelefone())
        print("\t Email ",patient.getEmail())
        print("\t Number visits ",patient.getNumber_visits())
        print("\t History visits ",patient.gethistoryofvisits())

        
        history=input("Introduce el history")
        histo=format_date+""+history
        controller.addapointment(patient,histo)
        
    elif(opcion=="5"):
        print("Saliendo..")
        break