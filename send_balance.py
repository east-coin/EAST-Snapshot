import os
import time
import pandas as pd

from pathlib import Path

from web3 import Web3, IPCProvider
from pathlib import Path

ipc_file = os.path.join(Path.home(), '.eastcoin/beta/geth.ipc')

web3 = Web3(IPCProvider(ipc_file))

addresses_df = pd.read_csv(
    'snapshot/eth-snapshot.txt',
    header=None, names=['id', 'address', 'balance']
)

total_balance = 0
transactions_count = 0


with open('geth_genesis.json', 'a') as genesis_file:
    for row in addresses_df.itertuples():
        transactions_count += 1
        web3.eth.sendTransaction({
            'from': '0x155c49ADBA5002D5226E81749be607F922e24553',
            'to': row.address,
            'value': int(row.balance),
            'gas': 21000,
            'gasPrice': 1800000000000,
        })
        total_balance += int(row.balance)

        if transactions_count == 8000:
            print('Last Transaction Address: {}'.format(row.address))
            time.sleep(20)
            transaction_count = 0

print(total_balance)
