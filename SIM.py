class SIM(object):
    items = []
    subList = [(str,str)]
    dataSMSList = [(str,str)]
    def __init__(self,Number = "undefined",Operator = "undefined"):
        self.Number = Number
        self.Operator = Operator
        SIM.items.append(self)
    staticmethod
    def AddToSubList(Number,Operator):
        SIM.subList.append((Number,Operator))
    def AddSMSToData(sms,Number):
        SIM.dataSMSList.append((sms,Number))
    def Show(self):
        print(f"Number: {self.Number}\nOperator: {self.Operator}")
        


