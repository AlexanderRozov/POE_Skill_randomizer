result = ""
with open("./skils.txt", "r+") as file:
    for line in file:
        if not line.isspace():
            result += line
 
    file.seek(0)  
    file.write(result)