from Utils import *
from CA import CA


class Customer:
    def __init__(self, Id, certificate_num):
        self.id = Id # account number
        self.certificate_num = certificate_num
        #self.wallet_balance = 0
        ##############

        self.public_key = None
        self.private_key = None

    def pub_prv_key_request_to_ca(self, ca_pub_key):
        message = str(self.id) + ", " + str(self.certificate_num)

        packet = encrypt(message=message, key=ca_pub_key)
        # send packet to ca and asign keys
        return packet

    def policy(self, range, count, time, receiver):
        return range + ','+count+','+time+','+receiver


    # create message
    def send_delegation_to_BC(self, customer_pu_key, bank_pu_key, policy):

        m = (customer_pu_key) + ',' + policy

        signed = sign(m, self.private_key)
        message = customer_pu_key + ',' + bank_pu_key + ',' + policy + signed

        return encrypt(message,self.private_key)

    def check_merchant_reqest(self,message,ca):

        separed= message.split(',')
        decrypted_digi_sign = decrypt(separed[2],ca.get_pub_key_of(separed[0]))
        decrypted_digi_sign_seperated=decrypted_digi_sign.split(',')
        if separed[0]== decrypted_digi_sign_seperated[0] and separed[1]== decrypted_digi_sign_seperated[1]:
            return True
        return False

    def payment_request_to_bank(self,bitcoin_amount,merchant_id):

        message= bitcoin_amount+", "+ merchant_id

        return encrypt(message,self.private_key)
