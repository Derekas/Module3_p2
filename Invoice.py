class Invoice():
    '''def __init__(self,id,date,nif,paid,base,vat,total,invoice_lines):
        self.__id=id
        self.__date=date
        self.__nif=nif
        self.__paid=paid
        self.__base=base
        self.__vat=vat
        self.__total=total
        self.__invoice_lines=invoice_lines'''

    def __init__(self,id,date,nif,vat,lines):
        self.__id=id
        self.__date=date
        self.__nif=nif
        self.__vat=vat
        self.__paid=False
        self.__base=0
        self.__total=1
        self.__invoice_lines=[]

    def getId(self):
        return self.__id
    def getDate(self):
        return self.__date
    def getNif(self):
        return self.__nif
    def getPaid(self):
        return self.__paid
    def getBase(self):
        return self.__base
    def getVat(self):
        return self.__vat
    def getTotal(self):
        return self.__total
    def getInvoice_lines(self):
        return self.__invoice_lines
    

    def setId(self,id):
        self.__id=id
    def setDate(self,date):
        self.__date=date
    def setNif(self,nif):
        self.__nif=nif
    def setPaid(self,paid):
        self.__paid=paid
    def setBase(self,base):
        self.__base=base
    def setVat(self,vat):
        self.__vat=vat
    def setTotal(self,total):
        self.__total=total
    def setInvoices_lines(self,invoice_lines):
        self.__invoice_lines=invoice_lines
        for line in invoice_lines:
            self.__base+=line[2]
        self.__total*=(1+self.__vat)
    def paid(self):
        self.__paid=True

