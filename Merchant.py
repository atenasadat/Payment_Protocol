

from Utils import encrypt



class Merchant :

    def __init__(self,nationalID,certificate_num):
        self.account_balance = 0
        self.nationalID = nationalID
        self.certificate_num=certificate_num



    def pub_prv_key_request_to_ca(self, ca_pub_key):
        message = str(self.national_id) + ", " + str(self.certificate_num)
        return encrypt(message=message, key=ca_pub_key)
