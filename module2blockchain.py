from bdb import Breakpoint


blockchain = []

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
    
# you can use default 
def add_transaction_value(transaction_amount, last_transaction=[1]):

    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction,transaction_amount])
    
# User transation
def get_transaction_value():
    return float(input('Your transaction amount please: '))

def get_user_choice():
    user_input = input('Enter your choice: ')
    return user_input
 
def print_blockchain_elements():
        #output the blockchain list
        #print(blockchain)
        for block in blockchain:
            print(block)
        
        else:
            print('-'*20)


def verify_chain():
    #block_index = 0
    is_valid = True
    #for block in blockchain:
    for block_index in range(len(blockchain)):
        if block_index ==0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid = True

   
        else:
            is_valid=False
   
            break


        # print ('the block is :',block)
        # print ('the blockchain is :',blockchain[block_index-1])
        # if block_index ==0:
        #     block_index +=1
        #     continue
        # elif block[0] == blockchain[block_index-1]:
        #     is_valid = True

        #     print('Since equal', is_valid)
        # else:
        #     is_valid=False
        #     print('break causing', is_valid)
        #     break

        # block_index +=1
    print ('final is_valid', is_valid)
    return is_valid 



#while loop
waiting_for_input = True

while waiting_for_input:

    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the transation blocks')
    print('h: Manipulate a block chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice =='1':
        tx_amount = get_transaction_value()
        add_transaction_value(tx_amount,get_last_blockchain_value())

    elif user_choice =='2':
        print_blockchain_elements()
    
    elif user_choice =='h':
        if len(blockchain)>=1:
            blockchain[0]=2

    elif user_choice == 'q':
        waiting_for_input =False 
    else:
        print ('Invalid Choice, pick value from list')

    if not verify_chain():

        print('Invalid Blockchain')
        break

# even while and for loops have else    it executes after 
#the loop is done
else :
    print('User left')



print('Done!')