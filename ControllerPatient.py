import re,Patient
import ControllerPatient
class ControllerPatient():
    patient_dic={}
    
    def __init__(self):
        self.__patients={}

    def add_patient(self,dni,name,surname,year_of_birth,telefone,email):

        patient= Patient.Patient(dni,name,surname,year_of_birth,telefone,email)
        self.__patients[patient.getDni()]= patient


    def delpatient(self,dni):
        
        if dni in self.__patients.keys():
            patient=self.__patients.pop(dni)
            return patient
        else:
            return None        

        

    def searchpatient(self,dni):
        return self.__patients.get(dni)

    def listPatient(self):
        list=[]
        for dni,patient in self.__patients.items():
            list.append(patient)
        return list
    
    def addapointment(self,patient):
        from datetime import datetime
        now = datetime.now()
        format_date = now.strftime("%d/%m/%Y %H:%M")
