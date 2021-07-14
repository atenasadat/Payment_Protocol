


from Utils import *


class BlockChain:

    def __init__(self):
        self.listOfBlocks = []




    def BC_response_to_deligation(self,message,pu_key):

        separed= message.split(',')

        digital_sign = separed[3]
        decrypted_digi_sign = decrypt(digital_sign,pu_key)

    def addNewBlock(self,data):


        return


    def consession(self):

        return

