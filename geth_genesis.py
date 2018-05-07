import pandas as pd

from web3 import Web3

genesis_header = """
{
  "config": {
    "chainId": 7,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0
  },
  "nonce": "0x0000000000000042",
  "timestamp": "0x00",
  "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "gasLimit": "0x09eb100",
  "difficulty": "0x400",
  "mixhash": "0x0000000000000000000000000000000000000000000000000000000000000000",
  "coinbase": "0x0000000000000000000000000000000000000000",
  "alloc": {
    "0000000000000000000000000000000000000001": {
      "balance": "0x1"
    },
    "0000000000000000000000000000000000000002": {
      "balance": "0x1"
    },
    "0000000000000000000000000000000000000003": {
      "balance": "0x1"
    },
    "0000000000000000000000000000000000000004": {
      "balance": "0x1"
    },
    "0000000000000000000000000000000000000005": {
      "balance": "0x1"
    },
    "0000000000000000000000000000000000000006": {
      "balance": "0x1"
    },
    "0000000000000000000000000000000000000007": {
      "balance": "0x1"
    },
    "0000000000000000000000000000000000000008": {
      "balance": "0x1"
    }"""

addresses_df = pd.read_csv(
    'snapshot/eth-snapshot.txt',
    header=None, names=['id', 'address', 'balance']
)

account_format = ',\n"{0}": {{"balance": "{1}"}}'

total_balance = 0

with open('geth_genesis.json', 'a') as genesis_file:
    genesis_file.write(genesis_header)
    for row in addresses_df.itertuples():
        total_balance += int(row.balance)
    genesis_file.write(account_format.format('0x155c49ADBA5002D5226E81749be607F922e24553', total_balance))
    genesis_file.write("""
  }
}
    """)
