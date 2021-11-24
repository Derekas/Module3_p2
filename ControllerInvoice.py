import re,Invoice
import InvoiceView
class ControllerInvoice():
    invoices={}
    
    def __init__(self):
        self.__invoices={}

    def add_invoices(self,id,date,nif,vat,lines):
        if(self.__invoices.get(id)==None):
            invoice= Invoice.Invoice(id,date,nif,vat)
            invoice.setInvoices_lines(lines)
            self.__invoices[id]= invoice
            return True
        return False

    def pay_invoice(self,id,properties):
        invoice=self.__invoices.get(id)

        if invoice != None:
            invoice.setPaid(True)
            return True

        return False
        """
        for prop,value in properties.items():
            if(prop=="paid"):
                invoice.setPaid(value)
        """
    def listInvoices(self,ispaid):
        list=[]
        for id,invoice in self.__invoices.items():
            if(invoice.getPaid()==ispaid):
                list.append(invoice)
        return list


    def searchnotpaidinvoices(self):
         
         for elem in self.__invoices.values:
             if elem.getPaid()=="False":
                 return self.__invoices.get(elem)

    def searchpaidinvoices(self):
         for elem in self.__invoices.values:
             if elem.getPaid()=="True":
                 return self.__invoices.get(elem)

                
            