from Banks import Blank

if __name__ == '__main__':
    bank = Blank("张三")
    bank.save_money(500)
    bank.get_money(150)