from Utils import encrypt



class Merchant :

    def __init__(self,ID,certificate_num):
        #self.account_balance = 0
        self.id = ID # account number
        self.certificate_num=certificate_num
        self.public_key=None
        self.private_key=None



    def pub_prv_key_request_to_ca(self, ca_pub_key):

        message = str(self.id) + ", " + str(self.certificate_num)
        return encrypt(message=message, key=ca_pub_key)


    def payment_request(self, customer_id, cost):

        message= self.id+','+ cost+','+ encrypt(self.id +','+ cost,self.private_key)

        return



