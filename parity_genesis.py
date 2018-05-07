import pandas as pd

genesis_header = """
{
  "name": "Eastbeta",
  "dataDir": "eastbeta",
  "engine": {
    "Ethash": {
      "params": {
        "minimumDifficulty": "0x020000",
        "difficultyBoundDivisor": "0x0800",
        "durationLimit": "0x0d",
        "blockReward": "0x4563918244F40000",
        "homesteadTransition": 0,
        "eip150Transition": 0,
        "eip160Transition": 0,
        "eip161abcTransition": 0,
        "eip161dTransition": 0,
        "eip100bTransition": 0,
        "eip649Transition": 0,
        "eip649Reward": "0x29A2241AF62C0000"
      }
    }
  },
  "params": {
    "gasLimitBoundDivisor": "0x0400",
    "registrar": "0x0000000000000000000000000000000000000000",
    "accountStartNonce": "0x00",
    "maximumExtraDataSize": "0x20",
    "minGasLimit": "0x1388",
    "networkID": "0x7",
    "maxCodeSize": 24576,
    "eip86Transition": "0x7fffffffffffff",
    "eip98Transition": "0x7fffffffffffff",
    "eip155Transition": 0,
    "eip140Transition": 0,
    "eip211Transition": 0,
    "eip214Transition": 0,
    "eip658Transition": 0
  },
  "genesis": {
    "seal": {
      "ethereum": {
        "nonce": "0x0000000000000000",
        "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000"
      }
    },
    "difficulty": "0x400",
    "author": "0x0000000000000000000000000000000000000000",
    "timestamp": "0x0",
    "parentHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "extraData": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "gasLimit": "0x09eb100"
  },
  "nodes": [
    "enode://a56ba92bf34da673dfaa756b58f497abc90b4bb1c1b29d5a0e4fb98a8a2f50c683aeb16464e60482478def72273faccc7a4f6093b598bee82a77a677c4550baa@192.99.99.18:30303"
  ],
  "accounts": {
    "0000000000000000000000000000000000000001": { "balance": "1", "builtin": { "name": "ecrecover", "pricing": { "linear": { "base": 3000, "word": 0 } } } },
    "0000000000000000000000000000000000000002": { "balance": "1", "builtin": { "name": "sha256", "pricing": { "linear": { "base": 60, "word": 12 } } } },
    "0000000000000000000000000000000000000003": { "balance": "1", "builtin": { "name": "ripemd160", "pricing": { "linear": { "base": 600, "word": 120 } } } },
    "0000000000000000000000000000000000000004": { "balance": "1", "builtin": { "name": "identity", "pricing": { "linear": { "base": 15, "word": 3 } } } },
    "0000000000000000000000000000000000000005": {
	  "balance": "1",
      "builtin": {
        "name": "modexp",
        "activate_at": "0x00",
        "pricing": {
          "modexp": {
            "divisor": 20
          }
        }
      }
    },
    "0000000000000000000000000000000000000006": {
	  "balance": "1",
      "builtin": {
        "name": "alt_bn128_add",
        "activate_at": "0x00",
        "pricing": {
          "linear": {
            "base": 500,
            "word": 0
          }
        }
      }
    },
    "0000000000000000000000000000000000000007": {
	  "balance": "1",
      "builtin": {
        "name": "alt_bn128_mul",
        "activate_at": "0x00",
        "pricing": {
          "linear": {
            "base": 40000,
            "word": 0
          }
        }
      }
    },
    "0000000000000000000000000000000000000008": {
	  "balance": "1",
      "builtin": {
        "name": "alt_bn128_pairing",
        "activate_at": "0x00",
        "pricing": {
          "alt_bn128_pairing": {
            "base": 100000,
            "pair": 80000
          }
        }
      }
    }"""

addresses_df = pd.read_csv(
    'snapshot/eth-snapshot.txt',
    header=None, names=['id', 'address', 'balance']
)

addresses_df = addresses_df.drop_duplicates(subset=['address'], keep='first')

account_format = ',\n"{0}": {{"balance": "{1}"}}'

total_balance = 0

with open('parity_genesis.json', 'a') as genesis_file:
    genesis_file.write(genesis_header)
    for row in addresses_df.itertuples():
        total_balance += int(row.balance)
    genesis_file.write(account_format.format('0x155c49ADBA5002D5226E81749be607F922e24553', total_balance))
    genesis_file.write("""
  }
}
    """)
