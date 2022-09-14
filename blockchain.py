genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [],
}
blockchain = [genesis_block]
open_transaction = []
owner = "Max"


def get_last_blockchain_value():
    """Returns the last value of current blockchain."""

    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :senser: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {"sender": sender, "recipient": recipient, "amount": amount}
    open_transaction.append(transaction)


def get_transaction_value():
    """Returns the input of the user (a new transaction amount as a float)"""

    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your transaction ammount please: "))
    return (tx_recipient, tx_amount)


def get_user_choise():
    user_input = input("Your choise: ")
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print("Outputing block:")
        print(block)
    else:
        print("-" * 20)


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


def mine_block():
    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block])
    print(hashed_block)

    block = {
        "previous_hash": "XYZ",
        "index": len(blockchain),
        "transactions": open_transaction,
    }
    blockchain.append(block)


waiting_for_input = True

while waiting_for_input:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")

    user_choise = get_user_choise()

    if user_choise == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choise == "2":
        mine_block()
    elif user_choise == "h":
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choise == "q":
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from a list")
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print("Invalid blockchain!")
    #     break
else:
    print("User left!")


print("Done")
