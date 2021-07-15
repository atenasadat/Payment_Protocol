from CA import CA
from Bank import Bank
from Customer import Customer
from Merchant import Merchant
from EC import ExchangeCenter
from BC import BlockChain


def payment_protocle(ca, customer, bank, merchant, blockchain, exch_center, cost):
    """
    customer sends request to CA to get pub key & prv key - pkm,skm
    Using CA pub_key
    """

    message_from_customer_to_ca = customer.pub_prv_key_request_to_ca(ca.get_pub_key_of("CA"))

    """
    CA responses to request, by checking credentials & generating prv pub key if it is a new registration
    """
    customer_keys = ca.response_to_pub_prv_key_request(message_from_customer_to_ca)
    customer.public_key = customer_keys.public_key()
    customer.private_key = customer_keys

    """
    customer send a delidation message for blockchain
    gets pkd , pkm 
    """
    policy = customer.policy(100, 231, 113, merchant.id)
    delidation_message_to_BC = customer.send_delegation_to_BC(ca.get_pub_key_of(customer.id),
                                                              ca.get_pub_key_of("Bank"),
                                                              policy,
                                                              ca.get_key_pairs(customer.id))

    """
    BlockChain sends verification message
    """

    blockchain.BC_response_to_deligation(delidation_message_to_BC, ca.get_pub_key_of(customer.id))

    """
    merchant sends request to CA to get pub key & prv key - pkm,skm
    Using CA pub_key
    """

    message_from_merchant_to_ca = merchant.pub_prv_key_request_to_ca(ca.get_pub_key_of("CA"))

    """
    CA responses to request, by checking credentials & generating prv pub key if it is a new registration
    """

    merchant_keys = ca.response_to_pub_prv_key_request(message_from_merchant_to_ca)
    merchant.public_key = merchant_keys.public_key()
    merchant.private_key = merchant_keys

    """
    merchant sends payment request to customer
    """

    merchant_payment_request_message= merchant.payment_request(customer.id, cost=cost)

    """"
    customer receive merchants payment request and check it
    """
    if not customer.check_merchant_reqest(merchant_payment_request_message,ca=ca):

        print("payment request is not valid")
        exit()

    """
    Athenticating payment : customer sends payment request to bank
    """
    payment_req_to_bank= customer.payment_request_to_bank(200, merchant.id)
    # bank responses

    """
    exchange crypto
    """


    """"
    Bank ( Semi-honest ) pay the payment
    """


    """
    merchant confirmed the payment
    """

    if merchant.confirm(cost):
        print("payment was successfull")



if __name__ == '__main__':
    ca = CA()
    customer = Customer("12", "a20")
    bank = ca.create_Bank()
    merchant = Merchant("01245", "679")
    bank.create_acount(customer.id)
    bank.create_acount(merchant.id)

    blockchain = BlockChain()
    exch_center = ExchangeCenter(10)

    payment_protocle(ca, customer, bank, merchant, blockchain, exch_center)
