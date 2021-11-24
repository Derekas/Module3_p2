import re,Student
import ControladorStudents
class ControladorStudents():
    student_dic={}
    
    def __init__(self):
        self.__students={}

    def add_student(self,dni,name,surname,age,city,province,email):

        student= Student.Student(dni,name,age,city,province,email)
        self.__students[student.getDni()]= student
        '''if(dni in self.__students.keys()):
            return False
        else:
            self.__students[student.getDni()]=student'''


    def delstudent(self,dni):
        
        if dni in self.__students.keys():
            student=self.__students.pop(dni)
            return student
        else:
            return None        

    def modify(self,dni,properties):
        student=self.__students[dni]
        for prop,value in properties.items():
            if(prop=="Name"):
                student.setName(value)
            if(prop=="Surname"):
                student.setSurname(value)
            if(prop=="Age"):
                student.setAge(value)

        

    def searchstudent(self,dni):
        return self.__students.get(dni)   