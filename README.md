# Whitelist Voting on Snapshot.org

This repository consist of the code used to produce the whitelist for the whitelist strategy on [Zesty Market Snapshot Page](https://snapshot.org/#/zestymarket.eth)

Zesty is currently experimenting with voting strategies for governance

## Current process
1. We obtain the addresses in # Auctions Per Creators and Campaigns Created By Buyers [https://dune.xyz/limbofeather/zestymarket](https://dune.xyz/limbofeather/zestymarket)

1. Each address is assigned 1 VOTE to vote on proposals on the snapshot page

1. This list is populated on a bi-weekly basis

1. Current challenges: We note that it is easy to Sybil this list. However, Sybiling this means participation in the market which increases the KPI and is a net win for the product. Do create an issue if you do think of a better approach with regards to voting. 