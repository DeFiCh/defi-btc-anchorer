# defi-btc-anchorer

A simple python script for periodic submission of DFI (DeFi Blockchain) anchors into the BTC (Bitcoin) blockchain.

It's configurable to check minimum profit conditions and detect other competing anchor transactions in BTC mempool.

# Docker

- Make sure have a config file as given below
- `docker-compose up`

# Running

- In a system with python3 and pip3 installed, install dependencies: `pip install -r requirements.txt`
- Create your configuration file.
- Create config file to say, `./config.toml` (See `config.example.toml` for example)
- Run `main.py`

You'll have to change at least the following fields in an example config file:
- RewardAddress - User's P2PKH address (in DeFi chain) for anchoring reward
- [DFI.RPC] - set your DeFi daemon RPC credentials
- [BTC.RPC] - set your Bitcoin daemon RPC credentials

Once configuration file is created, use the following command to test your setup:
```shell
./main.py --config ./config.toml --sendanchor no
```
The command above will run all the checks, create the anchor transaction, but won't send it into BTC mempool.

Once you've ensured everything is working as you assumed, run the following command to create an anchor:
```shell
./main.py --config ./config.toml
```

You may add the `--repeat 30` flag to repeat the routine every 30 seconds:
```shell
./main.py --config ./config.toml --repeat 30
```