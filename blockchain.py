from functools import reduce
import hashlib as hl
from typing import OrderedDict

from hash_util import hash_string_256, hash_block


MINIG_REWARD = 10

genesis_block = {"previous_hash": "", "index": 0, "transactions": [], "proof": 100}
blockchain = [genesis_block]
open_transaction = []
owner = "Max"
participants = {"Max"}


def valid_proof(transaction, last_hash, proof):
    guess = (str(transaction) + str(last_hash) + str(proof)).encode()
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == "00"


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block
    proof = 0
    while not valid_proof(last_block, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    tx_sender = [
        [tx["amount"] for tx in block["transactions"] if tx["sender"] == participant]
        for block in blockchain
    ]
    open_tx_sender = [
        tx["amount"] for tx in open_transaction if tx["sender"] == participant
    ]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
        tx_sender,
        0,
    )
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         amount_sent += tx[0]

    tx_recipient = [
        [tx["amount"] for tx in block["transactions"] if tx["recipient"] == participant]
        for block in blockchain
    ]
    amount_received = reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
        tx_recipient,
        0,
    )
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         amount_received += tx[0]
    return amount_received - amount_sent


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
    # transaction = {"sender": sender, "recipient": recipient, "amount": amount}
    transaction = OrderedDict(
        [("sender", sender), ("recipient", recipient), ("amount", amount)]
    )
    if verify_transaction(transaction):
        open_transaction.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
        print(block["transactions"][:-1])
        print(block["previous_hash"])
        print(block["proof"])
        if valid_proof(
            block["transactions"][:-1], block["previous_hash"], block["proof"]
        ):
            print("Proof of work is invalid")
            return False
    return True


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    if sender_balance > transaction["amount"]:
        return True
    else:
        return False


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transaction])


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()

    # reward_transaction = {
    #     "sender": "SYSTEM",
    #     "recipient": owner,
    #     "amount": MINIG_REWARD,
    # }
    reward_transaction = OrderedDict([("sender", 'SYSTEM'), ("recipient", owner), ("amount", MINIG_REWARD)])
    copied_transactions = open_transaction[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_block,
        "index": len(blockchain),
        "transactions": copied_transactions,
        "proof": proof,
    }
    blockchain.append(block)
    return True


waiting_for_input = True

while waiting_for_input:
    print("Please choose:")
    print("1: Add a new transaction value")
    print("2: Mine a new block")
    print("3: Output the blockchain blocks")
    print("4: Output participants")
    print("5: Check transaction validity")
    print("h: Manipulate the chain")
    print("q: Quit")

    user_choise = get_user_choise()

    if user_choise == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print("Added transaction!")
        else:
            print("Transaction failed!")
        print(open_transaction)
    elif user_choise == "2":
        if mine_block():
            open_transaction = []
    elif user_choise == "3":
        print_blockchain_elements()
    elif user_choise == "4":
        print(participants)
    elif user_choise == "5":
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("There are invalid transactions")
    elif user_choise == "h":
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [
                    {"sende": "Chris", "recipient": "Max", "amount": 100.0}
                ],
            }
    elif user_choise == "q":
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from a list")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid blockchain!")
        break
    print("Balance of {}: {:6.2f}".format("Max", get_balance("Max")))
else:
    print("User left!")


print("Done")
