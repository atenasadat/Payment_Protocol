
from Utils import *

from CA import CA
class Bank():

    def __init__(self,key_pair):
        self.key_pair = key_pair
        self.account_numbers = dict()






    def create_acount(self,nationalID,balance,password):

        account_num = hash(nationalID)
        self.account_numbers[nationalID]=({"account_number":account_num} ,
                                          {"account_balance":balance},
                                          {"Password":password}
                                          )


    def send_transaction_to_BC(self,message,customer_ID):

        decrypted_msg = decrypt(message,CA.get_pub_key(customer_ID)).split(',')

        cryptoCurrency_money =  decrypted_msg[0]
        merchantID  = decrypted_msg[1]
        signed = decrypted_msg[2]

        ## verify signiture from customer

        if verify(cryptoCurrency_money+','+merchantID , signed ,CA.get_pub_key(customer_ID) ):

                message = cryptoCurrency_money+","+customer_ID+","+merchantID

        return message+','+sign(message,self.key_pair)



    def find_account_balance(self,account_num):

        if account_num in self.account_numbers.values():
            pos = list(self.account_numbers.values()).index(account_num)
            return list(self.account_numbers.keys())[pos]




    def repospose_to_payment_ver_from_BC(self,customerID,merchantID,fiat_money):



        self.account_numbers[merchantID] = {"account_balance":self.find_account_balance(merchantID)+fiat_money}

        self.account_numbers[customerID] = {"account_balance":self.find_account_balance(customerID)-fiat_money}
