# -*- coding: utf-8 -*-
import getpass


#Считывание логина и пароля из файла  конфигураций
LogPass = []
with open("Config1.txt", "r") as file1:
    # итерация по строкам
    for line in file1:
        LogPass.append(line.strip())


#Ввод логина и пароля пользователя
login = input("ВВедите вашь логин: ")
password = getpass.getpass("ВВедите вашь пароль: ")


#Проверка логина и пароля 
if LogPass[0] == login and LogPass[1] == password:
	print ("Успешная аутоинтефикация")
else:
	print("Неверный логин или пароль")