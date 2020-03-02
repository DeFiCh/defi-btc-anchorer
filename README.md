# Anchorer script
Anchript (ANCHorer scIPT) is a tool for periodic submiting of DeFi anchors into BTC blockchain.

It's configurable to check minimum profit conditions and detect other competing anchor transactions in BTC mempool.

# Deps
Install python3 using your favorite package manager. Once python3 is isntalled, install the following python packages:
```shell
pip3 install python-bitcoinrpc
pip3 install toml
```

# Running
First things first - create your configuration file. Check out example configs `mainnet.example.toml` and `testnet.example.toml`. `mainnet.example.toml` should be used
with DeFi and BTC mainnet, and `testnet.example.toml` with DeFi and BTC testnet.

You'll have to change at least the following fields in an example config file:
- RewardAddress - User's P2PKH address (in DeFi chain) for anchoring reward
- [DFI.RPC] - set your DeFi daemon RPC credentials
- [BTC.RPC] - set your Bitcoin daemon RPC credentials

Once configuration file is created, use the following command to test your setup:
```shell
./anchript.py --conifg /path/to/config.toml --sendanchor no
```
The command above will run all the checks, create the anchor transaction, but won't send it into BTC mempool.

Once you've ensured everything is working as you assumed, run the following command to create an anchor:
```shell
./anchript.py --conifg /path/to/config.toml
```

You may add the `--repeat 30` flag to repeat the routine every 30 seconds:
```shell
./anchript.py --conifg /path/to/config.toml --repeat 30
```