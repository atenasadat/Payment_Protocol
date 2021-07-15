


from Utils import *
from CA import CA
from EC import ExchangeCenter



class Block:

    def __init__(self,cust_pu_key,bank_pu_key,policy):
        self.cust_pu_key=cust_pu_key
        self.bank_pu_key=bank_pu_key
        self.range = policy.split('.')[0]
        self.time = policy.split('.')[1]
        self.count =policy.split('.')[2]
        self.rec = policy.split('.')[3]









class Wallet:

    def __init__(self,nationalID,wallet_address,wallent_balance):
        self.Id = nationalID
        self.wallet_address = wallet_address ## equal to pu_key of customer
        self.wallent_balance =wallent_balance


    def Withdrawal(self,amount):

        self.wallent_balance = self.wallent_balance - amount



class BlockChain:

    def __init__(self):
        self.listOfBlocks = []
        self.Crypto_wallets = []





    def create_wallet(self,ID,balance):
            w = Wallet(ID,CA.get_pub_key(ID) , balance)
            self.Crypto_wallets.append(w)


    def find_wallet_balance_of_customer_by_address(self,address):

        for w in self.Crypto_wallets:
            if w.wallet_address == address:
                return w.wallent_balance



    def check_policy(self,money,customer_ID,merchant_ID):

        customer_pu_key = CA.get_pub_key(customer_ID)

        for bl in self.listOfBlocks:
            if bl.cust_pu_key == customer_pu_key:
                if merchant_ID == bl.rec and bl.range > money:

                    return True


    def BC_response_to_deligation(self,message,pu_key):

      ## message = customer_pu_key + ',' + bank_pu_key + ',' + policy + signed


        message = decrypt(message,pu_key)

        data= message.split(',')

        digital_sign = data[3]
        dig_sig_ver = verify(message,digital_sign,pu_key)
        policy = data[2]

        ## step 1: sig verification
        if dig_sig_ver :
            ## step2 : check wallet balance
            if policy.split('.')[0] > self.find_wallet_balance_of_customer_by_address(pu_key):

                self.addNewBlock(data[1],data[2],policy)


            else:
             return "Not enough money for deligation"


    def response_to_exchange_crypto(self,message,Bank_pu_key):

        message_info = message.split(',')

        message = message_info[0]
        signed_message = message_info[1]

        ### verify bank digital signature

        if verify(message,signed_message,Bank_pu_key):

            payment_info = message.split(',')
            crypto_money = payment_info[0]
            customer_ID = payment_info[1]
            merchant_ID = payment_info[2]


            if self.check_policy(crypto_money,customer_ID,merchant_ID):
                fiat_equal_money = ExchangeCenter.Exchange(crypto_money)
                for wallet in self.Crypto_wallets:
                    if wallet.Id == customer_ID:
                        wallet.Withdrawal(crypto_money)

                mess = fiat_equal_money+','+merchant_ID+','+customer_ID
                return encrypt(mess , Bank_pu_key)
            else:
               return "payment is againt policy"









    def addNewBlock(self,cus_pu_key,bank_pu_key,policy):

            b= Block(cus_pu_key,bank_pu_key,policy)
            self.listOfBlocks.append(b)
            return self.listOfBlocks.index(b)






    def consession(self):

        return

