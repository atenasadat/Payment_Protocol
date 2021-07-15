import math
from Crypto.PublicKey import RSA
from Utils import decrypt, verify, encrypt, sign, encrypt_multi_packet, sign_multi_packet
from Bank import Bank
from EC import ExchangeCenter

class CA:

    def __init__(self):
        self.key_pair = RSA.generate(4096)
        self.pub_keys = dict()
        self.pub_keys[hash("CA")] = self.get_pub_key()
        self.key_pair_dict = dict()
        self.key_pair_dict[hash("CA")] = (
            {"national_code": hash("CA"), "certificate_num": hash(""), "key_pair": self.key_pair})

    def get_pub_key(self):
        self.pub_key = self.key_pair.publickey()
        return self.pub_key

    def create_Bank(self):
        key = RSA.generate(1024)
        self.key_pair_dict[hash("Bank")] = ({"national_code": hash("Bank"), "certificate_num": hash(""), "key_pair": key})

        bank_ = Bank(key)
        self.pub_keys[hash("Bank")] = key.publickey()
        return bank_



    def get_pub_key_of(self, item):
        if hash(item) in self.pub_keys.keys():
            return self.pub_keys[hash(item)]
        else:
            return None

    def get_key_pairs(self,item):
        if hash(item) in self.key_pair_dict.keys():
            return self.key_pair_dict[hash(item)]
        else:
            return None

    def response_to_pub_prv_key_request(self, message):
        decrypted_message = str(decrypt(message=message, key_pair=self.key_pair))
        voter_identifications = decrypted_message.split(", ")
        #         considering national code and certificate num mach!
        i_code = str(voter_identifications[0])[2:]
        c_num = str(voter_identifications[1])[:-1]
        if i_code not in self.key_pair_dict.keys():

            key = RSA.generate(1024)
            self.key_pair_dict[hash(i_code)] = (
                {"national_code": hash(i_code),
                 "certificate_num": hash(c_num),
                 "key_pair": key})
            self.pub_keys[hash(i_code)] = key.publickey()


            return key
