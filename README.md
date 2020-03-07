# My-Blockchain
<<<<<<< HEAD
My blockchain project; creating my own cryptocurrency.

## Usage

Open two terminals and run:

```python
runfile('node.py')
runfile('node.py', args='-p=5001')
```

This will create two webservers, on localhost:5000 and localhost:5001, respectively.

## How does it work?

Each wallet belonging to a node is assigned a public and private key. 
To ensure communication between the nodes, for both nodes, add the other node as its peer node.

Any changes to the blockchain will then be broadcasted to both nodes. 

### Mine Block

A block is mined whenever "Mine Block" is submitted. 
This will append a new block to the blockchain and fund the hosting wallet. 

### Transactions

A new transaction is added by sending an amount (float) to the public key of the peer node. "Open Transactions" will show all transactions entered into, but not yet cleared. A transaction is part of the blockchain when a new block is mined.

