#!/usr/bin/env python3
from pathlib import Path

class MyException(Exception):
    pass

def Dane():
    name, surname, date_of_birth = input("Enter name, surname and date of birth: ").split(" ")
    print(f"Your name: {name}, surname: {surname}, date of birth: {date_of_birth}")

def Szyfr():
    szyfr = 1234

    while True:
        try:
            podany_szyfr = int(input("Podaj szyfr: "))
            break
        except ValueError:
            print("Musisz podac liczbe!")
            continue

    if szyfr == podany_szyfr:
        print("Podales poprawny szyfr")
    else:
        print("Podales nieprawidlowy szyfr")


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
    #Dane()
    Szyfr()