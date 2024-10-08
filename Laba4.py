
from numbers import Number
from SIM import SIM
from MobilePhone import MobilePhone

def isNumber(str):
    try:
        float(str)
        return True
    except:
        print("Incorrect input")
        return False


while True:
    print("Choose:\n1)Create SIM\n2)Create Phone\n3)Choose Phone\n4)Check Inform SIM and Phones\n5)Exit")    
    checkDigit = False
    while not checkDigit:
        key = (input("Enter the act:"))
        checkDigit = isNumber(key)
    key = float(key)
    if key == 5:
        break
    elif key == 1:
        createNumber = input("Enter the number:")
        createOperator = input("Enter the operator:")
        sim = SIM(createNumber,createOperator)
    elif key == 2:
        createVendor = input("Enter the vendor:")
        createModel = input("Enter the model:")
        mob = MobilePhone(createVendor,createModel)
    elif key == 3:
        checkDigit = False
        while not checkDigit:
            index = (input("Enter the index:"))
            if int(index) < 0 or int(index) >= MobilePhone.items.__len__():
                print("Out of range")
            else:
                checkDigit = isNumber(index)
            index = int(index)
        while True:
            print("Choose:\n1)Call\n2)Send SMS\n3)Get SMS\n4)Insert SIM\n5)Pull Out SIM\n6)Exit")
            checkDigit = False
            while not checkDigit:
                key = (input("Enter the act:"))
                checkDigit = isNumber(key)
            key = int(key)
            if key == 1:
                numb = input("Enter the number to call:")
                MobilePhone.items[index].Call(numb)
            elif key == 2:
                numb = input("Enter the number to call:")
                sms = input("Enter the sms:")
                MobilePhone.items[index].SendSMS(numb,sms)
            elif key == 3:
                MobilePhone.items[index].GetSMS()
            elif key == 4:
                 indexSim = -1
                 checkDigit = False
                 while not checkDigit:
                    indexSim = (input("Enter the index:"))
                    if int(indexSim) < 0 or int(indexSim) >= SIM.items.__len__():
                        print("Out of range")
                    else:
                        checkDigit = isNumber(indexSim)
                    indexSim = int(indexSim)
                 MobilePhone.items[index].InsertSIM(SIM.items[indexSim].Number,SIM.items[indexSim].Operator)
            elif key == 5:
                MobilePhone.items[index].PullOut()
            elif key == 6:
                break
    elif key == 4:
        print("Phones:\n")
        i = 0
        while i < MobilePhone.items.__len__():
            MobilePhone.items[i].Show()
            i+=1
        i = 0
        print("SIMs:\n")
        while i < SIM.items.__len__():
            SIM.items[i].Show()
            i+=1
                    

       

