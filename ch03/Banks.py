class Blank():
    def __init__(self,cname):
        self.__name = cname
        self.__amount = 0
    def save_money(self,money):
        self.__amount= self.__amount+money
        print("存钱",money,"元，目前余额：",self.__amount)
    def get_money(self,money):
        self.__amount = self.__amount-money
        print("取钱", money, "元，目前余额：", self.__amount)

