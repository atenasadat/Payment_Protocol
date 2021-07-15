

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
    customer_keys= ca.response_to_pub_prv_key_request(message_from_customer_to_ca)

    #????
    customer.public_key=customer_keys.public_key()
    customer.private_key=customer_keys

    """
    customer send a delidation message for blockchain
    gets pkd , pkm 
    """

    policy = customer.policy(100,200,12,'01245')
    delidation_message_to_BC = customer.send_delegation_to_BC(ca.get_pub_key_of(customer.id),
                                                              ca.get_pub_key_of("Bank"),
                                                              policy,
                                                              ca.get_key_pairs(customer.id))

    """
    BlockChain sends verification message
    """

    blockchain.BC_response_to_deligation(delidation_message_to_BC,ca.get_pub_key_of(customer.id))

    """
    merchant sends request to CA to get pub key & prv key - pkm,skm
    Using CA pub_key
    """

    message_from_merchant_to_ca = merchant.pub_prv_key_request_to_ca(ca.get_pub_key_of("CA"))

    """
    CA responses to request, by checking credentials & generating prv pub key if it is a new registration
    """

    merchant_keys= ca.response_to_pub_prv_key_request(message_from_merchant_to_ca)
    merchant.public_key=merchant_keys.public_key()
    merchant.private_key=merchant_keys





if __name__ == '__main__':

    ca = CA()
    customer = Customer("12","a20")
    bank = ca.create_Bank()
    merchant = Merchant("01245","679")
    bank.create_acount(customer.id)
    bank.create_acount(merchant.id)

    blockchain = BlockChain()
    exch_center = ExchangeCenter(12)

    payment_protocle(ca,customer,bank,merchant,blockchain,exch_center)




