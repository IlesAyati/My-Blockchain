# My-Blockchain

My blockchain project; A blockchain node network.

## Usage

Open two terminals and run:

```python
runfile('node.py')
runfile('node.py', args='-p=5001')
```

This will create two webservers, on localhost:5000 and localhost:5001, respectively.

## How does it work?

Each node can load wallets, each assigned a public key and a private key. 
To ensure communication between the nodes: 
For both nodes, on the network tab, add the other webserver as its peer node.

Any changes to the blockchain will then be broadcasted to both nodes. 

### Wallet
Each node can create wallet, or load one if it has already been created. Each wallet has a unique id, or public key. 

### Mine Block

A block is mined whenever "Mine Block" is submitted. 
This will append a new block to the blockchain and fund the hosting wallet. 

### Transactions

A new transaction is made by sending an amount (float) to the public key of a wallet on the peer node. "Open Transactions" will show all transactions entered into, but not yet cleared. A transaction is part of the blockchain once a new block is mined.

