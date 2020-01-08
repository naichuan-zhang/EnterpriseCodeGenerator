import os
import random
import string
import time

import qrcode
import tkinter
from tkinter import messagebox
from tkinter import filedialog

number = "1234567890"
letter = "ABCDEFGHIJKLMNPQRSTUVWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i = 0

randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""

root = tkinter.Tk()


def scode1(choice):
    count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)     # only digits, no digit limits
    pass


def scode2(choice):
    pass


def scode3(choice):
    pass


def scode4(param, choice):
    pass


def scode5(choice):
    pass


def scode6(choice):
    pass


def scode7(choice):
    pass


def scode8(choice):
    pass


def scode9(choice):
    pass


def wfile(sstr, sfile, typeis, smsg, datapath):
    """
    read code information that has been generated, and print generated code
    on to screen and print to the file

    sstr - content generated code
    sfile - filename to save code
    typeis - whether to show an info box. Either "" or no.
    smsg - content of info box
    datapath - path to save code
    """
    mkdir(datapath)
    datafile = datapath + "\\" + sfile      # set file to save code
    file = open(datafile, 'w')
    wrlist = sstr
    pdata = ""
    wdata = ""
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[', '')).replace(']','')    # remove "[" and "]"
        wdata = wdata.replace(''''', '').replace(''''', '')
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print("\033[1;31;40m" + pdata + "\033[0m")
    if typeis != "no":
        tkinter.messagebox.showinfo("Alert", smsg + str(len(randstr)) + "\n Security code file storage location: " + datafile)
        root.withdraw()


# check validity
def input_box(showstr, showorder, length):
    """
    Three ways to validate:
    1. only digits, no digit limit
    2. only latin letters
    3. only digits, has digit limit
    """
    instr = input(showstr)
    if instr is not "":
        if showorder == 1:
            if instr.isdigit():     # check if only digits
                if instr == "0":    # if input is 0
                    print("\033[1;31;40mInput is zero, please try again!!!\033[0m")
                    return "0"      # return "0" when invalid
                else:
                    return instr
            else:
                print_err()
                return "0"
        elif showorder == 2:
            if instr.isalpha():     # check if only letters
                if len(instr) != length:
                    print("\033[1;31;40m" + length + " letters is required, please try again!!!\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print_err()
                return "0"
        elif showorder == 3:        # check if digits with limits
            if instr.isdigit():
                if len(instr) != length:
                    print("\033[1;31;40m" + length + " letters is required, please try again!!!\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print_err()
                return "0"
        else:
            print_err()
            return "0"
    else:
        print_err()
        return "0"


# open file with given filename
def open_file(filename):
    if os.path.exists(filename):
        with open(filename) as file:
            content = file.read()
        return content
    else:
        print('ERROR: file not found!')
        return None


# create dir
def mkdir(path):
    exist = os.path.exists(path=path)
    if not exist:
        os.mkdir(path)
        print(os.path.realpath)
    else:
        print(f'PATH: {path} already exists')


# error message
def print_err():
    print("\033[1;31;40mInvalid Input!!!\033[0m")


def mainmenu():
    print("""\033[1;35m
      *********************************************************************************************
                                    Enterprise coding generation system
      *********************************************************************************************
          1. Generate 6-digit anti-counterfeiting code (type 213563)
          2. Generating 9-bit series of digital anti-counterfeiting code (879-335439 type)
          3. Generating 25-bit hybrid serial number (B2R12-N7TE8-9IET2-FE35O-DW2K4)
          4. Generate anti-counterfeiting code with data analysis function (5A61M0583D2)
          5.Intelligent batch generation with data analysis function of anti-counterfeiting code
          6. Subsequent supplement spawning anti-counterfeiting code (5A61M0583D2)
          7.EAN-13 barcode batch generation
          8. 2D Code Bulk Output          
          9. Corporate Fan Anti-counterfeiting Code Sweepstakes
          0. Exit the system
      ==============================================================================================
      Description: Select a menu with a number key
      ==============================================================================================
    \033[0m""")


def validate(choice):
    if choice.isdigit():
        if choice == 0:
            print_err()
            return 0
        else:
            return choice
    else:
        print_err()
        return 0


if __name__ == '__main__':
    while i < 9:
        mainmenu()
        choice = input("\033[1;32m     Please enter a number between 0 to 9: \33[0m")
        if choice is not "":
            choice = validate(choice)
            if choice == 1:
                scode1(choice)
            if choice == 2:
                scode2(choice)
            if choice == 3:
                scode3(choice)
            if choice == 4:
                scode4("", choice)
            if choice == 5:
                scode5(choice)
            if choice == 6:
                scode6(choice)
            if choice == 7:
                scode7(choice)
            if choice == 8:
                scode8(choice)
            if choice == 9:
                scode9(choice)
            if choice == 0:       # exit the program
                i = 0
                print("Exiting the program ...")
        else:
            print_err()
            time.sleep(2)
