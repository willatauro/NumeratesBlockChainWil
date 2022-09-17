#https://docs.python.org/3/library/

## Object oriented programming 
import functools
from bdb import Breakpoint
import hashlib
import json
from collections import OrderedDict
from hash_util import hash_block, hash_string_256

MINING_REWARD = 10


blockchain = []
open_transactions = []
owner='Wil'
# Particiapant is a set as it will store unique values, other way of declaring set is a = set(['Max'], if you dont put it as list it will take
# individual elements like M, A, X)
participants ={'Wil'}



def valid_proof(transactions, last_hash, proof):
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    #guess_hash = hashlib.sha256(guess).hexdigest()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'

def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions,last_hash,proof):
        proof +=1
    return proof 

def load_data():
    global blockchain
    global open_transactions
    try:
        with open('blockchain.txt', mode='r') as f:

            filecontent = f.readlines()
            #blockchain = filecontent[0] it wont work are you need to convert to python object
            #open_transactions = filecontent[1]
            blockchain = json.loads(filecontent[0][:-1])
            updated_blockchain =[]
            for block in blockchain:
                updated_block ={
                    'previous_hash':block['previous_hash'],
                    'index':block['index'],
                    'proof':block['proof'],
                    'transactions':[OrderedDict([('sender',tx['sender']), ('recipient',tx['recipient']),('amount',tx['amount'])]) for tx in block['transactions']]
                }
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = json.loads(filecontent[1])
            updated_transactions =[]
            for tx in open_transactions:
                updated_transact =OrderedDict(
                    [('sender',tx['sender']), ('recipient',tx['recipient']),('amount',tx['amount'])])


                
                updated_transactions.append(updated_transact)
            open_transactions = updated_transactions


    except IOError:
        genesis_block={

        'previous_hash':'',
        'index':0,
        'transactions':[],
        'proof':100

}
        blockchain = [genesis_block]
load_data()

def save_data():
    try :
        with open('blockchain.txt', mode='w') as f:
            # f.write(str(blockchain))
            # f.write('\n')
            # f.write(str(open_transactions))
            f.write(json.dumps(blockchain))
            f.write('\n')
            f.write(json.dumps(open_transactions))
    except IOError:
        print('Saving Failed!')

def get_balance(participants):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender']==participants] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender']==participants]
    tx_sender.append(open_tx_sender)
    #amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum+ tx_amt[0] if len(tx_amt) >0 else 0 , tx_sender,0)
    amount_sent = functools.reduce(lambda tx_sum, tx_amt: tx_sum+ sum(tx_amt) if len(tx_amt) >0 else tx_sum + 0 , tx_sender,0)
    # amount_sent = 0
    # for tx in tx_sender:
    #     if len(tx)>0:
    #         amount_sent += tx[0]
    
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient']==participants]for block in blockchain]
    #amount_received = functools.reduce(lambda tx_sum, tx_amt :tx_sum + tx_amt[0] if len(tx_amt)>0 else 0, tx_recipient,0)
    amount_received = functools.reduce(lambda tx_sum, tx_amt :tx_sum + sum(tx_amt) if len(tx_amt)>0 else tx_sum + 0 , tx_recipient,0)
    # amount_received =0
    # for tx in tx_recipient:
    #     if len(tx)>0:
    #         amount_received  += tx[0]
    return amount_received - amount_sent

#to get last value
def get_last_blockchain_value():
    """ This is doc string comment style IDE will show the details.Get last value
    
    Arguments: 
        you can add arguments here and it will display while hoovering over the function
    
    """
    if len(blockchain)<1:
        ## Return nothing 
        return None 
    
    return blockchain[-1]
    

def verify_transaction(transaction):
    
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


# you can use default 
def add_transaction (recipient,sender = owner,  amount=1.0):
    # receiving the values as dictionary
    # transaction = {
    #     'sender':sender,
    #     'recipient':recipient,
    #     'amount':amount

    # }
    transaction = OrderedDict([('sender',sender), ('recipient',recipient),('amount',amount)])
        
# we are allowing to check verify transations function, add Not
    if verify_transaction(transaction):
    #adding the dictionary value to list
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        save_data()
        return True
    return False


def mine_block():
    
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)

    proof = proof_of_work()

    # reward_transation = {

    #     'sender': 'MINING',
    #     'recipient': owner,
    #     'amount':MINING_REWARD
    # }
    reward_transation = OrderedDict([('sender','MINING'), ('recipient',owner),('amount',MINING_REWARD)])
# List is copied by reference, that is it refers the address of original list. For strings, numbers and booleans are copied by value/


    copied_transactions = open_transactions [:]

    copied_transactions.append(reward_transation)
    
    # # without list comprehension
    # for key in last_block:
    #     value=last_block[key]
    #     hashed_block = hashed_block + str(value)
    
    # with list comprehension

    #hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    
    #print (hashed_block) 
    block = {
        'previous_hash':hashed_block,
        'index':len(blockchain),
        'transactions':copied_transactions,
        'proof' : proof 


    }
    blockchain.append(block)
    #save_data()
    return True
    
# User transation
def get_transaction_value():

    tx_recipient = input('Enter the recipeint: ')
    tx_amount=float(input('Your transaction amount please: '))


    #returning as a tuple 
    return (tx_recipient,tx_amount)

def get_user_choice():
    user_input = input('Enter your choice: ')
    return user_input
 
def print_blockchain_elements():

        for block in blockchain:
            print(block)
        
        else:
            print('-'*20)


def verify_chain():

 # enumerates converts dict to tuple
    for (index,block) in enumerate(blockchain):
        if index==0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
        if not valid_proof(block['transactions'][:-1],block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
    return True
    
def verify_transactions():

    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid
    return all([verify_transaction(tx) for tx in open_transactions])


#while loop
waiting_for_input = True

while waiting_for_input:

    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine the block blocks')
    print('3: Output the transation blocks')
    print('4: Output Participants')
    print('5: check transation validity')
    print('h: Manipulate a block chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice =='1':
        
        
        tx_data = get_transaction_value()

        #tuple unpacking
        recipient, amount = tx_data
        if add_transaction(recipient,amount=amount):
            print('Added transation!')
        else:
            print('Transation failed!')
        print(open_transactions)
    
    elif user_choice =='2':
        if mine_block():
            open_transactions = []
            save_data()

    elif user_choice =='3':
        print_blockchain_elements()

    elif user_choice =='4':
        print(participants)
    
    elif user_choice =='h':
        if len(blockchain)>=1:
            blockchain[0] ={
                'previous_hash':'',
                'index':0,
                'transations':[{'sender':'Chris', 'recipient':'Max','amount':20}]

            }
 
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print ('There are invalid transactions')

    elif user_choice == 'q':
        waiting_for_input =False 
    else:
        print ('Invalid Choice, pick value from list')

    if not verify_chain():
        print_blockchain_elements()
        print('Invalid Blockchain')
        break
    #print(get_balance('Wil'))
    print('Balance of {}: {:6.2f}'.format('Wil',get_balance('Wil')))

# even while and for loops have else    it executes after 
#the loop is done
else :
    print('User left')



print('Done!')