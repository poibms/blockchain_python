blockchain = []


def get_last_blockchain_value():
    """Returns the last value of current blockchain."""

    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :transaction_amount: The amount that should be added
        :last_transaction: The last blockchain transaction (default [1])
    """
    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """Returns the input of the user (a new transaction amount as a float)"""
    return float(input("Your transaction ammount please: "))


def get_user_choise():
    user_input = input("Your choise: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print("Outputing block:")
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            # break
    return is_valid

waiting_for_input = True

while waiting_for_input:
    
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")

    user_choise = get_user_choise()

    if user_choise == "1":
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choise == "2":
        print_blockchain_elements()
    elif user_choise == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choise == "q":
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from a list")
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
else:
    print("User left!")


print("Done")
