import Student,ControladorStudents
students={}
def readdni():
    while True:
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dni = input("Introduzca el DNI: ")
        letter=dni[-1].upper()
        number=dni[:-1]
    
        if(len(dni)!=9 and number.isdigit()):
            number=int(dni[:-1])
            return dni
            break
        else:
            print("Format Incorrect")


def readname():
    while True:
        name=input("Introduce un nombre")
        if len(name)>0:
            return name
            break
        else:
            print("Nombre no valido")

def readsurname():
    while True:
        surname=input("Introduce un nombre")
        if len(surname)>0:
            return surname
            break
        else:
            print("Nombre no valido")

def readage():
    while True:
        age=int(input("Introduce una edad"))
        if age>0:
            return age
            break
        else:
            print("Edad no valida")

def readcity():
    while True:
        city=input("Introduce una ciudad")
        if len(city)>0:
            return city
            break
        else:
            print("Ciudad no valida")

def readprovince():
    while True:
        province=input("Introduce una provincia")
        if len(province)>0:
            return province
            break

        else:
            print("Provincia no valida")

def reademail():
    while True:
        email=input("Introduce una provincia")
        if len(email)>0:
            return email
            break
        else:
            print("Correo no valido")
def menu():
    print("1, Add a student")
    print("2, Delete a student")
    print("3. Modify a student")
    print("4. Search a student")
    print("5. Exit")
    print("Choose option: ")

def remove(dni):
        if len((students))>0:
            if dni in students.keys():
                del student[dni]
                return 1
        return 0
def modify(dni):
        if len((students))>0:
            if dni in students.keys():
                
                return 1
        return 0
def liststudents():
    result=""

    for dni,studen in students.items():
        result+= dni+"\n"
        for rec in student:
            result+="\t"+ rec+ "\n"
    return result

controller=ControladorStudents.ControladorStudents()
while True:
    menu()

    opcion=input("")
    if(opcion=="1"):
        dni=readdni()
        name=readname()
        surname=readsurname()
        age=readage()
        city=readcity()
        provincia=readprovince()
        email=reademail()

        if controller.add_student():
            print("El usuario se ha añadido correctamente")
        else:
            print("El usuario no se ha podido añadir")

    elif(opcion=="2"):
        dni=readdni()
        student= controller.delstudent(dni)
        if (student!=None):
            print("El estudiante", student.getName(),"a sido eliminado")
        else:
            print("El dni no existe")
        
        
        '''if len((students))>0:
            if dni in students.keys():
                students.pop(dni)
            else:
                print("El usuario no existe")
        if controller.add_student(dni):
            print("The student has been deleted")
        else:
            print("False")'''

    elif(opcion=="3"):
        dni=readdni()
        student=controller.modify(dni)
        if (student!=None):
            print("El estudiante", student.getDni(),"a sido modificado")
            while True:
                print("1, Modify name")
                print("2, Modify surname")
                print("2, Modify age")
                
                op=input("Que quieres modificar")
                if (op=="1"):
                    newname=readname()
                    prop={'Name': newname}
                    controller.modify(dni,prop)
                if (op=="2"):
                    newSur=readsurname()
                    prop={'Surname': newSur}
                    controller.modify(dni,prop)
                if (op=="3"):
                    newAge=readage()
                    prop={'Age': newAge}
                    controller.modify(dni,prop)
        else:
            print("El dni no existe")
    elif(opcion=="4"):
        '''dni=readdni()
        if len((students))>0:
            if dni in students.keys():
                print(students[dni])
            else:
                print("El usuario no existe")'''

        dni=readdni()
        student= controller.searchstudent(dni)
        if (student!=None):
            print("Name", student.getName())
            print("Surame", student.getSurname())
            print("age", student.getAge())
            print("City", student.getCity())
            print("Province", student.getProvince())
            print("Email", student.getEmail())
        else:
            print("El dni no existe")
    elif(opcion=="5"):
        print("Saliendo..")
        break