import os
import random
import time
import tkinter
import qrcode

from string import digits
from tkinter import messagebox
from tkinter import filedialog
from pystrich.ean13 import EAN13Encoder     # barcode generator


number = "1234567890"
letter = "ABCDEFGHIJKLMNPQRSTUVWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
i = 0
randstr = []


root = tkinter.Tk()


# generate 6-digit anti-counterfeiting code (type 213563)
def scode1(choice):
    codes = []
    count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)     # only digits, no digit limits
    while count == "0":
        count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)  # only digits, no digit limits

    print(f'{count} 6-digit code is generating ...')
    while len(codes) != int(count):
        code = ''
        for i in range(6):
            code = code + random.choice(number)
        code = code + '\n'
        if code not in codes:
            codes.append(code)

    wfile(codes, "scodes" + str(choice) + ".txt", "", f"{count} number of 6-digit codes has been generated", "codepath")


# Generate 9-bit series of digital anti-counterfeiting code (879-335439 type)
def scode2(choice):
    codes = []
    series = input_box("\033[1;32m     Please enter the first three digits of your product series: \33[0m", 3, 3)
    while series == "0":
        series = input_box("\033[1;32m     Please enter the first three digits of your product series: \33[0m", 3, 3)

    count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)
    while count == "0":
        count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)

    while len(codes) != int(count):
        part = series + "-"
        for i in range(6):
            part = part + random.choice(number)
        part += "\n"
        if part not in codes:
            codes.append(part)

    wfile(codes, "scodes" + str(choice) + ".txt", "", f"{count} number of 9-digit series number has been generated", "codepath")


# Generate 25-bit hybrid serial number (B2R12-N7TE8-9IET2-FE35O-DW2K4)
def scode3(choice):
    codes = []
    count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)
    while count == "0":
        count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)

    while len(codes) != int(count):
        parts = []      # save five parts of hybrid serial code separately

        for i in range(5):
            part = ""
            for j in range(5):
                part = part + random.choice(letter)
            parts.append(part)

        code = ""
        for i in range(len(parts)):
            if i != 0:
                code = code + "-" + parts[i]
            else:
                code = code + parts[i]
        code += '\n'
        if code not in codes:
            codes.append(code)

    wfile(codes, "scodes" + str(choice) + ".txt", "", f"{count} number of 25-bit hybrid serial number has been generated", "codepath")


# Generate anti-counterfeiting code with data analysis function (5A61M0583D2)
def scode4(param, choice):
    type = input_box("\033[1;32m     Please enter three letters for data analysis: \33[0m", 2, 3)
    while not type.isalpha() or len(type) != 3:
        type = input_box("\033[1;32m     Please enter three letters for data analysis: \33[0m", 2, 3)

    count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)
    while count == "0":
        count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)

    ffcode(count, type, "", choice, "codepath")


# Intelligent batch generation with data analysis function of anti-counterfeiting code
def scode5(choice):
    default_dir = r"codeauto.znc"       # default filename to open
    file_path = tkinter.filedialog.askopenfilename(initialdir=(os.path.expanduser(default_dir)),
                                                   title="Open file",
                                                   filetypes=[("Text file", "*.znc")])
    codelist = open_file(file_path)
    if codelist is not None:
        codelist = codelist.split('\n')
        print(codelist)
        for item in codelist:
            codea = item.split(',')[0]      # three letters
            codeb = item.split(',')[1]      # number of codes to generate
            ffcode(codeb, codea, "no", choice, "codebatch")

    root.withdraw()


# Subsequent supplement spawning anti-counterfeiting code (5A61M0583D2)
def scode6(choice):
    default_dir = "default.txt"
    file_path = tkinter.filedialog.askopenfilename(initialdir=(os.path.expanduser(default_dir)),
                                                   title="Open file")

    codelist = open_file(file_path)
    codelist = codelist.split('\n')
    codelist.remove("")
    strset = codelist[0]
    print(strset)
    remove_digits = strset.maketrans("", "", digits)
    print(remove_digits)

    root.withdraw()


# EAN-13 barcode batch generation
def scode7(choice):
    codes = []
    country_id = input_box("\033[1;32m     Please enter the 3-digit country id: \33[0m", 1, 0)
    while len(country_id) != 3 or int(country_id) < 1:
        country_id = input_box("\033[1;32m     Please enter the 3-digit country id: \33[0m", 1, 0)

    company_id = input_box("\033[1;32m     Please enter the 4-digit company id: \33[0m", 1, 0)
    while len(company_id) != 4 or int(country_id) < 1:
        company_id = input_box("\033[1;32m     Please enter the 4-digit company id: \33[0m", 1, 0)

    count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)
    while count == "0":
        count = input_box("\033[1;32m     Please enter the number of codes you want to generate: \33[0m", 1, 0)

    mkdir("barcode")
    while len(codes) != int(count):
        code = country_id + company_id
        part = ""
        for i in range(5):
            part = part + random.choice(number)
        code = code + part
        # calc the last digit of code
        even_sum = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7]) + int(code[9]) + int(code[11])
        odd_sum = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]) + int(code[8]) + int(code[10])
        check_bit = (even_sum * 3 + odd_sum) % 10
        check_bit = (10 - check_bit) % 10
        code = code + str(check_bit)

        if code not in codes:
            codes.append(code)

    # generate barcode
    for code in codes:
        encoder = EAN13Encoder(code)
        encoder.save("barcode\\" + code + ".jpg")


# 2-dimensional barcode generation - QR code
def scode8(choice):
    count = input_box("\033[1;32m     Please enter the number of QR codes you want to generate: \33[0m", 1, 0)
    while count == "0":
        count = input_box("\033[1;32m     Please enter the number of QR codes you want to generate: \33[0m", 1, 0)

    mkdir("qrcode")
    for i in range(int(count)):
        code = ""
        for j in range(12):         # 12 digits for each qr code
            code = code + random.choice(number)

        encoder = qrcode.make(code)
        encoder.save("qrcode\\" + code + ".jpg")


# draw a lottery
def scode9(choice):
    default_dir = r"lottery.ini"
    file_path = tkinter.filedialog.askopenfilename(initialdir=(os.path.expanduser(default_dir)),
                                                   title="Open file",
                                                   filetypes=[("Ini file", "*.ini")])
    codelist = open_file(file_path)
    root.withdraw()         # withdraw the filedialog

    codelist.split("\n")

    count = input_box("\033[1;32m     Please enter the number of lotteries you want to generate: \33[0m", 1, 0)
    while count == "0" or len(codelist) < int(count):
        count = input_box("\033[1;32m     Please enter the number of lotteries you want to generate: \33[0m", 1, 0)

    lottery = random.sample(codelist, int(count))

    print("\n\n\033[1;38m     Lottery information shown as follows: \33[0m")

    for i in range(int(count)):
        wdata = str(lottery[i].replace('[', '')).replace(']', '')
        wdata = wdata.replace(''''', '').replace(''''', '')
        print("\033[1;32m     "+ wdata +" \33[0m")


def ffcode(count, type, ismessage, choice, path):
    codes = []
    while len(codes) != int(count):
        # generate 6-digit anti-counterfeiting code (type 213563)
        part1 = ""
        for i in range(6):
            part1 = part1 + random.choice(number)
        # separate type in three letters
        region = type[0].upper()
        color = type[1].upper()
        time = type[2].upper()

        pos_region = 0
        pos_color = 0
        pos_time = 0
        while not pos_region < pos_color < pos_time:
            pos_region = random.randint(0, 6)
            pos_color = random.randint(0, 6)
            pos_time = random.randint(0, 6)

        code = part1[0:pos_region] + region + part1[pos_region:pos_color] + \
               color + part1[pos_color:pos_time] + time + part1[pos_time:] + '\n'

        if code not in codes:
            codes.append(code)

    wfile(codes, type + str(choice) + ".txt", ismessage, f"{count} number of anti-counterfeiting code with data "
                                                             f"analysis function has been generated", path)


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
                    print("\033[1;31;40m" + str(length) + " letters is required, please try again!!!\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print_err()
                return "0"
        elif showorder == 3:        # check if digits with limits
            if instr.isdigit():
                if len(instr) != length:
                    print("\033[1;31;40m" + str(length) + " letters is required, please try again!!!\033[0m")
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
          2. Generate 9-bit series of digital anti-counterfeiting code (879-335439 type)
          3. Generate 25-bit hybrid serial number (B2R12-N7TE8-9IET2-FE35O-DW2K4)
          4. Generate anti-counterfeiting code with data analysis function (5A61M0583D2)
          5. Intelligent batch generation with data analysis function of anti-counterfeiting code
          6. Subsequent supplement spawning anti-counterfeiting code (5A61M0583D2)
          7. EAN-13 barcode batch generation
          8. 2-dimensional barcode generation - QR Code         
          9. Draw a lottery
          0. Exit the system
      ==============================================================================================
          Description: Select a menu with a number
      ==============================================================================================
    \033[0m""")


def validate(choice):
    if choice.isdigit():
        return int(choice)
    else:
        print_err()
        return 0


if __name__ == '__main__':
    while True:
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
                print("Exiting the program ...")
                time.sleep(2)
                exit(0)
        else:
            print_err()
            time.sleep(2)
