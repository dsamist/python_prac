from web3 import Web3, HTTPProvider
from eth_account import Account
from eth_utils.exceptions import ValidationError

# Enable Mnemonic features
Account.enable_unaudited_hdwallet_features()

# Connect to an Ethereum node
infura_url = "https://mainnet.infura.io/v3/0ae73be5c9e84a42a68e503009fa210f"
web3 = Web3(HTTPProvider(infura_url))

# Read the seed phrases from a text file
with open('./Telegram Desktop/mnemonic.txt', 'r') as file:
    seed_phrases = [line.strip() for line in file]

# ERC20 Token Contract ABI
# This is a standard ERC20 contract ABI
abi = """[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"}]"""

# Token contract address
# Replace this with the contract address of the token you're interested in
token_contract_address = '0x...'

def get_token_balance(seed_phrase, contract_address):
    try:
        account = web3.eth.account.from_mnemonic(seed_phrase)
        address = account.address
        contract = web3.eth.contract(address=contract_address, abi=abi)
        balance = contract.functions.balanceOf(address).call()
        return address, balance
    except ValidationError:
        print(f"Invalid seed phrase: {seed_phrase}")
        return None, None

for seed_phrase in seed_phrases:
    address, balance = get_token_balance(seed_phrase, token_contract_address)
    if address is not None and balance is not None and balance >= 0.001:
        print(f"Address: {address}, Balance: {balance} Tokens")
        print(f"Seed phrase: {seed_phrase}")
