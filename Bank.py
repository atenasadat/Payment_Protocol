
from Utils import *

from CA import CA


class Acount:
    def __init__(self,nationalID,balance,account_number,password):
        self.Id= nationalID
        self.account_balance = balance
        self.account_number = account_number
        self.password = password
class Bank():

    def __init__(self,key_pair):
        self.key_pair = key_pair
        self.accounts = []






    def create_acount(self,nationalID,balance,num,password):

        self.accounts.append(Acount(nationalID,balance,account_number=num,password=password))


    def send_payment_request_to_BC(self,message,customer_ID):

        decrypted_msg = decrypt(message,CA.get_pub_key(customer_ID)).split(',')

        cryptoCurrency_money =  decrypted_msg[0]
        merchantID  = decrypted_msg[1]
        # signed = decrypted_msg[2]

        ## verify signiture from customer

        # if verify(cryptoCurrency_money+','+merchantID , signed ,CA.get_pub_key(customer_ID) ):

        message = cryptoCurrency_money+","+customer_ID+","+merchantID

        return message+','+sign(message,self.key_pair)



    def find_account_balance(self,account_num):

        if account_num in self.accounts:
            if account_num.account_number == account_num:
                return account_num.account_balance



    def Pay_the_payment(self,messagee):

        decrypted_msg = decrypt(messagee,CA.get_key_pairs("Bank"))

        fiat = decrypted_msg.split(',')[0]
        customer_ID = decrypted_msg.split(',')[1]
        merchant_ID = decrypted_msg.split(',')[2]

        for ac in self.accounts:
            if ac.Id == customer_ID:
                ac.account_balance -= fiat

            if ac.Id == merchant_ID:
                ac.account_balance += fiat


        return fiat

