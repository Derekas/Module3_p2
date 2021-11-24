import Invoice
import ControllerInvoice,datetime
import matplotlib.pyplot as plt
students={}
def readId():
    while True:
        id = int(input("Introduzca el Id: "))
        if len(id)>0:
            return id
        else:
            print("Id no valido")


def readdate():
    fecha = input("Introduzca la fecha: ")
    try:
        datetime.datetime.strptime(fecha, '%Y/%m/%d')
    except:
        return "El formato debe ser  YYYY/MM/DD"
    return datetime.datetime.strptime(fecha, '%Y/%m/%d')

def readNif():
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    while True:
        
        nif = input("Introduzca el Nif: ")
        letter=nif[-1].upper()
        number=nif[:-1]
    
        if(len(nif)!=9 and number.isdigit()):
            number=int(nif[:-1])
            return nif
        else:
            print("Format Incorrect")

def readPaid():
    while True:
        print("Introducir false si no se ha realizado el pago")
        print("Introducir true si se ha realizado el pago")
        paid=input("Introduce true o false")
        if(paid=="true"):
            paid=True
            return paid
        elif(paid=="false"):
            paid=False
            return paid
        else:
            print("Error")


def readBase():
    while True:
        base=float(input("Introduce una base"))
        if len(base)>0:
            return base
        else:
            print("Base no valida")

def readVat():
    while True:
        vat=float(input("Introduce una base"))
        if len(vat)>0:
            return vat
        else:
            print("VAT no valido")

def calcularTotal(base,Vat):
    total=base*Vat
    return total

def menu():
    print("1, Add Invoice")
    print("2, List not paid invoices: All and by Customer NIF")
    print("3. List paid invoices: All and by Customer NIF")
    print("4. Pay invoice ")
    print("5. Exit")
    print("Choose option: ")

controller=ControllerInvoice.ControllerInvoice()
while True:
    menu()

    opcion=input("")
    if(opcion=="1"):

        id=readId()
        
        now=datetime.now()
        date=now.strftime("%d/%m/%Y")
        nif=readNif
        print("Add the lines of the invoices: ")
        lines=[]
        while True:
            product=input("Product name")
            quantity=int(input("Product quantity"))
            total=input("Total product cost")
            lines.append((product,quantity,total))
            optionline=input("Do you want to add another line? (1-Yes)(0-No)")
            if(optionline=="0"):
                break
        if (controller.add_invoices(id,date,nif,0.21,lines)):
            
            print("El invoice se ha añadido correctamente")
        else:
            print("El invoice no se ha podido añadir")

    elif(opcion=="2"):
        list=controller.listInvoices(False)
        invoicesids=[]
        invoicestotal=[]
        for invoice in list:
            print("Invoice ",invoice.getId())
            print("\t data ",invoice.getDate())
            print("\t total ",invoice.getTotal())
            print("\t\t ",invoice.getLines())
            invoicesids.append(invoice.getId())
            invoicestotal.append(invoice.getTotal())

        plt.bar(x=invoicesids,height=invoicestotal)
        plt.xlabel("Invoices ids")
        plt.ylabel("€")
        plt.show()
    elif(opcion=="3"):
        list=controller.listInvoices(True)
        for invoice in list:
            print("Invoice ",invoice.getId())
            print("\t data ",invoice.getDate())
            print("\t total ",invoice.getTotal())
            print("\t\t ",invoice.getLines())

        
    elif(opcion=="4"):
        id=readId()
        invoice=controller.pay_invoice(id)
        if (invoice):
            print("El invoice", id," ha sido modificado")   
        else:
            print("El id no existe")
    
    elif(opcion=="5"):
        print("Saliendo..")
        break