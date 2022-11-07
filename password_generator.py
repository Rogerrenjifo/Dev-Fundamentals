"""password_generator"""
import random
class PasswordGenerator:
    """genera"""
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
a=PasswordGenerator()
print (a.generate_password())
