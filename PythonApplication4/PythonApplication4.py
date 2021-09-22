import pyautogui as x
import pydirectinput as p
import speech_recognition as sr
import time



qSes="q"
wSes="w"
eSes="e"
rSes="ultimate"
dSes="heal"
fSes="f"

def qAt(x):
    x=int(x)
    if x==12:
        a=869
        b=288
    elif x==1:
        a=1062
        b=241
    elif x==2:
        a=1090
        b=302
    elif x==3:
        a=1180
        b=435
    elif x==4:
        a=1104
        b=529
    elif x==5:
        a=1006
        b=594
    elif x==6:
        a=916
        b=575
    elif x==7:
        a=745
        b=563
    elif x==8:
        a=709
        b=528
    elif x==9:
        a=719
        b=443
    elif x==10:
        a=761
        b=345
    elif x==11:
        a=812
        b=309
    p.moveTo(a,b)
    p.typewrite("q")
def wAt():
    p.press("f2")
    p.moveTo(862,482)
    p.typewrite("w")
def eAt():
    p.typewrite("e")
def rAt(x):
    x=int(x)
    if x==12:
        a=869
        b=288
    elif x==1:
        a=1062
        b=241
    elif x==2:
        a=1090
        b=302
    elif x==3:
        a=1180
        b=435
    elif x==4:
        a=1104
        b=529
    elif x==5:
        a=1006
        b=594
    elif x==6:
        a=916
        b=575
    elif x==7:
        a=745
        b=563
    elif x==8:
        a=709
        b=528
    elif x==9:
        a=719
        b=443
    elif x==10:
        a=761
        b=345
    elif x==11:
        a=812
        b=309
    p.moveTo(a,b)
    p.typewrite("r")

def dAt():
    p.typewrite("d")
def fAt():
    p.typewrite("f")



def qGelistir():
    x.keyUp("ctrl")
    p.typewrite("q")
    x.keyDown("ctrl")
def wGelistir():
    x.keyUp("ctrl")
    p.typewrite("w")
    x.keyDown("ctrl")
def eGelistir():
    x.keyUp("ctrl")
    p.typewrite("e")
    x.keyDown("ctrl")
def rGelistir():
    x.keyUp("ctrl")
    p.typewrite("r")
    x.keyDown("ctrl")

def yap():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        print("konus dinliyorum")
        try:
            audio=rec.listen(source)
            print(rec.recognize_google(audio))
            if rec.recognize_google(audio)==wSes:
                wAt()
            elif rec.recognize_google(audio)==qSes:
                rec=sr.Recognizer()
                with sr.Microphone() as source:
                    rec.adjust_for_ambient_noise(source)
                    x=rec.listen(source)
                    qAt(rec.recognize_google(x))
            elif rec.recognize_google(audio)==eSes:
                eAt()
            elif rec.recognize_google(audio)==rSes:
                rec=sr.Recognizer()
                with sr.Microphone() as source:
                    rec.adjust_for_ambient_noise(source)
                    x=rec.listen(source)
                    rAt(rec.recognize_google(x))
            elif rec.recognize_google(audio)==dSes:
                dAt()
        except sr.UnknownValueError:
            yap()
while True:
    yap()