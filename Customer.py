

from Utils import *
from CA import CA

class Customer:
    def __init__(self,nationalId,certificate_num):
        self.national_id = nationalId
        self.certificate_num=certificate_num
        self.wallet_balance = 0






    def pub_prv_key_request_to_ca(self, ca_pub_key):
        message = str(self.national_id) + ", " + str(self.certificate_num)
        return encrypt(message=message, key=ca_pub_key)


    def send_delegation_to_BC(self,customer_pu_key,bank_pu_key , policy,key_pairs):

            # policy = range + ','+count+','+time+','+receiver
            self.key_pairs = key_pairs

            m = (customer_pu_key)+','+policy
            signed = sign(m ,self.key_pairs)
            message =customer_pu_key +',' +bank_pu_key+','+policy+signed
            return message



