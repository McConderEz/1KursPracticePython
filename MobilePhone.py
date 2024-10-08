from SIM import SIM

class MobilePhone(object):
    items = []
    sim = SIM()
    def __init__(self,Vendor = "undefined",Model = "undefined"):
        self.Vendor = Vendor
        self.Model = Model        
        MobilePhone.items.append(self)
    def Call(self,number):
        i = 1
        while i < SIM.subList.__len__():
            if SIM.subList[i][0] == number:
                print("Call made to subscriber...")
                print("disconnecting")
            i+=1
    def SendSMS(self,number,sms):
        i = 1
        while i < SIM.subList.__len__():
            if SIM.subList[i][0] == number:
                SIM.AddSMSToData(sms,number)
                print("SMS sent...")
            i+=1
    def GetSMS(self):
        i = 1
        while i < SIM.dataSMSList.__len__():
            if SIM.dataSMSList[i][1] == self.Sim.Number:
                print(SIM.dataSMSList[i][0])
                SIM.dataSMSList.pop(i)
            i+=1
    def InsertSIM(self,number,operator):
        self.Sim = SIM(number,operator)
        SIM.AddToSubList(self.Sim.Number,self.Sim.Operator)

    def PullOut(self):
        self.Sim = None
    
    def Show(self):
        print(f"Vendor: {self.Vendor}\nModel: {self.Model}")