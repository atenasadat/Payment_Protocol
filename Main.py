

from CA import CA
from Bank import Bank
from Customer import Customer
from Merchant import Merchant
from EC import ExchangeCenter
from BC import BlockChain

def  payment_protocle(ca,customer,bank,merchant,blockchain,exch_center):

    """
    customer sends request to CA to get pub key & prv key - pkm,skm
    Using CA pub_key
    """

    message_from_customer_to_ca = customer.pub_prv_key_request_to_ca(ca.get_pub_key_of("CA"))




    """
    CA responses to request, by checking credentials & generating prv pub key if it is a new registration
    """
    ca.response_to_pub_prv_key_request(message_from_customer_to_ca)



    """
    customer send a delidation message for blockchain
    gets pkd , pkm 
    """
    policy = "100/3/120/111"
    delidation_message_to_BC = customer.send_delegation_to_BC(ca.get_pub_key_of(customer.national_id),
                                                              ca.get_pub_key_of("Bank"),
                                                              policy,
                                                              ca.get_key_pairs(customer.national_id))

    """
    BlockChain sends verification message
    """

    blockchain.BC_response_to_deligation(delidation_message_to_BC,ca.get_pub_key_of(customer.national_id))

    """
    merchant sends request to CA to get pub key & prv key - pkm,skm
    Using CA pub_key
    """

    message_from_merchant_to_ca = merchant.pub_prv_key_request_to_ca(ca.get_pub_key_of("CA"))

    """
    CA responses to request, by checking credentials & generating prv pub key if it is a new registration
    """

    ca.response_to_pub_prv_key_request(message_from_merchant_to_ca)






if __name__ == '__main__':

    ca = CA()
    customer = Customer("12","a20")
    bank = ca.create_Bank()
    merchant = Merchant("01245","679")
    bank.create_acount(customer.national_id)
    bank.create_acount(merchant.nationalID)

    blockchain = BlockChain()
    exch_center = ExchangeCenter()

    payment_protocle(ca,customer,bank,merchant,blockchain,exch_center)




