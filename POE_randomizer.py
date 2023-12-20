import random

skill_file = open("./skils.txt", "r")
skill_data = skill_file.readlines()

class_file = open("./classes.txt", "r")
class_data = class_file.readlines()

print( '\n' + random.choice(class_data) + ' \n'+ random.choice(skill_data))




    