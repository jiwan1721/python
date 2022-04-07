#case study
# Bike speedometer - model pulsor 220

#response message
def responseMessange(code):
    if code == "KS":
        print("key Matched")
    elif code =="KF":
        print("key failed. Check key")
    elif code == "WC":
        print("Welcome to pulsor220")
    elif code == "TY":
        print("Thank you. closing....")
    elif code == "BT":
        print("SELECT BUTTONS")
        print("1. MD - change mode")
        print("2.sp - check speedometer")
        print("3. KM - check kilometer")
        print("4.lp -change to lap mode")
        print("5.CL- close BIke")

def changeMode(mode):
    if mode == "RC":
        return "your at RACER MODE"
    elif mode == "EC":
        return "you are at ECONOMY mode"
    elif mode == "ST":
        return "you are at street mode"
    else:
        return "You are at normal mode"

def selectButton(button):
    if button == "MD":
        changeMode()
        selectButton()
    elif button == "SP":
        speedMeter()
    elif button == "KM":
        kilometers()
    elif button == "LP":
        lap()
    elif button == "CL":
        responseMessage("TY")
#PROGRAM START

def startBike():
    key = str(input("Enter key: "))
    if key == "PULSOR220":
        responseMessage("KS")
        responseMessage("WC")
        responseMessage("BT")
        selectButton()
        
































