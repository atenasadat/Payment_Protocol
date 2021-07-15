class ExchangeCenter:

    def __init__(self,exchange_rate):

        self.exchange_rate= exchange_rate


    def Exchange(self,amount):

        return amount * self.exchange_rate
