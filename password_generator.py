"""inicio"""
import random
#diccionario ={"facebook":"12345678aA","Amazon": "12345678bB"}
class AplicationInformation:
    def __init__(self,page,password):
        self.page =page
        self.password =password
    def __str__(self):
        print ("transormando aplication information en string")
        return f"name:{self.page} password {self.password}"
class SaveInformation:
    """guardar informacion en el txt"""
    #diccionario[page]= pagepassword.generate_password() 
    @staticmethod
    def save_information(data):
        txt=open('register.txt','a')
        #a=f"nombre:{self.page} password {self.password} \n"
        txt.write(str(data))
        txt.close
class ReadInformation:
    def read_information(self):
        txt=open('register.txt','r')
        database= txt.read()
        print (database)


class PasswordGenerator:
    """clase passwordGenerador"""
    def generate_password(self):
        """generate an aleatory password"""
        password = []
        passw_leng = random.randint(9,16)
        num_of_capital_letters= random.randint(1,(passw_leng-2))
        num_of_lower_case_letters= random.randint(1,(passw_leng-num_of_capital_letters-1))
        num_of_numbers= passw_leng - num_of_lower_case_letters - num_of_capital_letters
        for _ in range(num_of_capital_letters):
            password.append(chr(random.randint(65,90)))
        for _ in range(num_of_lower_case_letters):
            password.append(chr(random.randint(97,122)))
        for _ in range(num_of_numbers):
            password.append(str(random.randint(0,9)))
        random.shuffle(password)
        password_str= ''.join(password)
        return password_str
