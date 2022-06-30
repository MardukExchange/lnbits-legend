<h1>Swap Extension</h1>
<h2>Use any Boltz Compliant API to do Submarine Swaps on LNBits</h2>

i.e. [Marduk Exchange](https://marduk.exchange) to swap into RBTC, SOV or xUSD.

## end user usage
* connect your `non-bitcoin` wallet, select assets to send/receive and create swaps.

## development/test setup
* go to https://gitpod.io/#https://github.com/MardukExchange/lnsovbridge, deploy the contracts and make sure boltz API is running and available.
* run local gitpod companion to make sure boltz regtest container 8081 is reachable.
* update `BOLTZ_URL` in swap.py
* start lnbits and make sure it can connect to boltz regtest lnd + marduk exchange API on RSK testnet

## acknowledgements
* Parts of this extension is based on the work of `https://github.com/dni/lnbits-legend`  
