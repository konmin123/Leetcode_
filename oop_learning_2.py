from oop_learning import Purse


class P2(Purse):
    pass


if __name__ == '__main__':

    x = P2('USD')
    y = P2('USD')

    x.top_up_balance(100)

    x.info()
    y.info()

    P2.send_money(x, y, 50)

    x.info()
    y.info()