import os
import time
import argparse

def onLights():
    os.system("sudo ~/hub-ctrl -h 0 -P 2 -p 1")

def offLights():
    os.system("sudo ~/hub-ctrl -h 0 -P 2 -p 0")
    
def dot():
    offLights()
    time.sleep(1)
    onLights()
    

def dash():
    onLights()
    time.sleep(3)

def mapper(str):
    strlst = str.split()
    for ch in strlst:
        time.sleep(1)
        if ch == ".":
            dot()
        elif ch == "-":
            dash()
            
morse_code = {"A":". -",
              "B":"- . . .",
              "C":"- . - .",
              "D":"- . .",
              "E":".",
              "F":". . - .",
              "G":"- - .",
              "H":". . . .",
              "I":". .",
              "J":". - - -",
              "K":"- . -",
              "L":". - . .",
              "M":"- -",
              "N":"- .",
              "O":"- - -",
              "P":". - - .",
              "Q":"- - . -",
              "R":". - .",
              "S":". . .",
              "T":"-",
              "U":". . _",
              "V":". . . -",
              "W":". - -",
              "X":"- . . -",
              "Y":"- . - -",
              "Z":"- - . .",
              "1":". - - - -",
              "2":". . - - -",
              "3":". . . - -",
              "4":". . . . -",
              "5":". . . . .",
              "6":"- . . . .",
              "7":"- - . . .",
              "8":"- - - . .",
              "9":"- - - - .",
              "0":"- - - - -",
              " ":". . . . . . ."}
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Morse messages")
    parser.add_argument("--m", metavar='N',type=str, help="Enter the message you want to give to the world")
    args = parser.parse_args()
    msglst = args.m.upper().split()
    wlen = len(msglst)
    onLights()
    for words in msglst:
        for ch in words:
            time.sleep(3)
            print(ch, "morse_code:",morse_code[ch])
            mapper(morse_code[ch])
        if wlen > 1:
            print("Blank", "morse_code:",morse_code[" "])
            mapper(morse_code[" "])
            wlen -= 1
    onLights()
