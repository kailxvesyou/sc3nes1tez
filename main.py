import random
import string
user={}
status=""
while True :
    status=input("New user push"+" N"+"\t"+"Login push"+" L "+"Exit push Q : ").upper()
    if status == "Q":
        break
    def newuser():
     username=input("Username : ")
     if username in user:
          print("ชื่อซ้ำ")
          return
     question=input("Do you want generate password y/n : ")
     if question=="y":
          password=""
          all=string.punctuation+string.digits+string.ascii_letters
          for x in range(10):
              password_gen=random.choice(all)  
              password+=password_gen
          print("yours password is : ",password)
          user["username"] = username
          user["password"] = password
          print("Created")
          chars = string.punctuation+string.digits+string.ascii_letters
          chars = list(chars)
          key = chars.copy()
          random.shuffle(key)
          encript = ""
          for letter in user["password"]:
            index = chars.index(letter)
            encript += key[index]
          print("ถูกเข้ารหัสเป็น",encript)
     elif question=="n":
        password=input("Password : ")
        user["username"] = username
        user["password"] = password
        print("Created")
        chars = string.punctuation+string.digits+string.ascii_letters
        chars = list(chars)
        key = chars.copy()
        random.shuffle(key)
        encript = ""
        for letter in user["password"]:
            index = chars.index(letter)
            encript += key[index]
        print("ถูกเข้ารหัสเป็น",encript)
    if status == "N":
         newuser()
    def Olduser():        
     username=input("Username : ")
     password=input("Password : ")
     if KeyError:
          print("ยังไม่มีการสร้าง Username และ Password")
          return
     if username in user["username"] and password in user["password"]:
          print("Welcome")
     else:
          print("กรอกผิด")
    if status == "L":
         Olduser()
