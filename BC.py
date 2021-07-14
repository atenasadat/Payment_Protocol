


from Utils import *
from CA import CA

class BlockChain:

    def __init__(self):
        self.listOfBlocks = []
        self.Crypto_wallets = dict()





    def create_acount(self,ID,balance):

        self.Crypto_wallets[ID] =[
            {"wallet_address":CA.get_pub_key(ID)},
            {"wallent_balance":balance}]






    # def BC_response_to_deligation(self,message,pu_key):
    #
    #
    #     ### data = pkd, pkm, policy, sig(pkd || policy)
    #     ### policy = range.count.time.receiver
    #
    #
    #     data= message.split(',')
    #
    #     digital_sign = data[3]
    #     decrypted_digi_sign = decrypt(digital_sign,pu_key)
    #
    #     policy_parts = data[2].split(".")
    #
    #
    #     range= policy_parts[0]
    #     count  = policy_parts[1]
    #     time =policy_parts[2]
    #     receiver = policy_parts[3]
    #
    #
    #     if verify(message,digital_sign,pu_key):
    #
    #         if self.check_balance(adr,range):
    #              self.addNewBlock(data[:2])





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

            policy = self.find_block_policy(customer_ID)

            policy = policy.split('.')

            range  =policy[0]
            count= policy[1]
            time = policy[2]
            receiver = policy[3]

            # if range<crypto_money and receiver == merchant_ID:










    def find_block_policy(self,ID):

        for bl in self.listOfBlocks:
            info= bl["ID"].split('/')
            if info[0] == ID:
                return info[3]


    def addNewBlock(self,data,ID):

        customer_pukey= data[0]
        bank_pubkey=data[1]
        policy = data[2]
        block = {"ID" :ID+'/'+customer_pukey +'/'+bank_pubkey+'/'+policy}

        self.listOfBlocks.append(block)

        return self.listOfBlocks.index(block)


    def consession(self):

        return

