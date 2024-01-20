import requests
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import BitcoinMainnet
from hdwallet.derivations import BIP44Derivation

def get_btc_balance(address):
    url = "https://blockchain.info/rawaddr/" + address
    response = requests.get(url)
    if response.text:
        try:
            balance_btc = response.json()['final_balance'] / 1e8  # Convert from Satoshi to BTC
            return balance_btc
        except ValueError:
            return None
    else:
        print(f"Error: Empty response from {url}")
        return None

# Read the seed phrases from a text file
with open('./Telegram Desktop/seed 6.txt', 'r') as file:
    seed_phrases = [line.strip() for line in file]

for seed_phrase in seed_phrases:
    try:
        # Generate a Bitcoin address from the seed phrase
        bip44_hdwallet = BIP44HDWallet(cryptocurrency=BitcoinMainnet)
        bip44_hdwallet.from_mnemonic(mnemonic=seed_phrase, language="english")
        bip44_hdwallet.from_path(BIP44Derivation(cryptocurrency=BitcoinMainnet, account=0, change=False, address=0))
        address = bip44_hdwallet.address()
        # Get the Bitcoin balance
        balance = get_btc_balance(address)
        if balance is not None and balance >= 0.00012:
            print(f"Address: {address}, Balance: {balance} BTC")
            print(f"Seed phrase: {seed_phrase}")
    except ValueError:
        print(f"Invalid seed phrase: {seed_phrase}")
