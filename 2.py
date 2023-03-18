import getpass
import hashlib


#Считывание хеша логина и пароля из файла конфигураций
LogPass = []
with open("Config2.txt", "r") as file1:
    # итерация по строкам
    for line in file1:
        LogPass.append(line.strip())

#Ввод логина и пароля пользователя
login = input("ВВедите вашь логин: ")
password = getpass.getpass("ВВедите вашь пароль: ")

#Расчёт хеш функции MD5 логина и пароля 
login = hashlib.sha512(login.encode())
password = hashlib.sha512(password.encode())

#Проверка значения хеш функции MD5 логина и пароля 
if LogPass[0] == login.hexdigest() and LogPass[1] == password.hexdigest():
	print ("Успешная аутенефикация")
else:
	print("Неверный логин или пароль")
