from web3 import Web3, HTTPProvider
from eth_account import Account  # Import the Account module
from eth_utils.exceptions import ValidationError

# Enable Mnemonic features
Account.enable_unaudited_hdwallet_features()

# Connect to an Ethereum node (you can use an Infura API key)
#infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY"
infura_url = "https://polygon-mainnet.infura.io/v3/0ae73be5c9e84a42a68e503009fa210f"
web3 = Web3(HTTPProvider(infura_url))

# List of seed phrases
# Read the seed phrases from a text file
with open('./Telegram Desktop/seed 6.txt', 'r') as file:
    seed_phrases = [line.strip() for line in file]
        
# seed_phrases = [
#     "pull express rabbit romance dice bid royal token they news pole cycle",
#     "slush identify skill chair sniff black story cheese unaware faculty raven music",
#     # Add more seed phrases as needed
# ]

def get_balance(seed_phrase):
    try:
        account = web3.eth.account.from_mnemonic(seed_phrase)
        address = account.address
        balance_wei = web3.eth.get_balance(address)
        balance_eth = web3.from_wei(balance_wei, 'ether')
        balance_eth = format(balance_eth, '.3f')
        return address, float(balance_eth)
    except ValidationError:
        print(f"Invalid seed phrase: {seed_phrase}")
        return None, None
for seed_phrase in seed_phrases:
    address, balance = get_balance(seed_phrase)
    if address is not None and balance is not None and balance >= 0.001:
        print(f"Address: {address}, Balance: {balance} ETH")
        print(f"Seed phrase: {seed_phrase}")

