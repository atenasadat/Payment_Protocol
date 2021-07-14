

class Bank():

    def __init__(self,key_pair):
        self.key_pair = key_pair
        self.account_numbers = dict()





    def create_acount(self,nationalID):
        account_num = hash(nationalID)
        self.account_numbers[nationalID]=({"account_number":account_num})
