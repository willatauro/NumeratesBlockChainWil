blockchain = []

#to get last value
def get_last_blockchain_value():
    """ This is doc string comment style IDE will show the details.Get last value
    
    Arguments: 
        you can add arguments here and it will display while hoovering over the function
    
    """
    return blockchain[-1]
    
# you can use default 
def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction,transaction_amount])
    
# User input
def get_user_input():
    return float(input('Your transaction amount please: '))

#Scope of variable local and global, you can use the keyword global
tx_amount = get_user_input()
add_value(tx_amount)

#keyword argument
tx_amount = get_user_input()
add_value(transaction_amount=tx_amount,last_transaction=get_last_blockchain_value())

tx_amount = get_user_input()
add_value(tx_amount,get_last_blockchain_value())


print(blockchain)

