from CA import CA
from Bank import Bank
from Customer import Customer
from Merchant import Merchant
from EC import ExchangeCenter
from BC import BlockChain


def payment_protocle(ca, customer, bank, merchant, blockchain, cost):


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


    """
       Bank responce to Customer for payment
    """

    exchange_crypto_message = bank.send_payment_request_to_BC(payment_req_to_bank,customer.id)

    """
    exchange crypto
    """

    fiat_amount_and_verify_payment_message = blockchain.response_to_exchange_crypto(exchange_crypto_message,CA.get_pub_key("Bank"))

    """"
    Bank ( Semi-honest ) pay the payment
    """
    Bank.Pay_the_payment(fiat_amount_and_verify_payment_message)

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
    bank.create_acount(customer.id , '1300000','12-0821','as452')
    bank.create_acount(merchant.id,'120000000','13-123','fr54')

    blockchain = BlockChain()
    blockchain.create_wallet(customer.id,'760000')

    exch_center = ExchangeCenter(10)


    payment_protocle(ca, customer, bank, merchant, blockchain,cost=300)
