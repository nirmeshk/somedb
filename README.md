# somedb: Fault-tolerent Key/Value store with Shard support
### Inspired by [MIT 6.824: Distributed Systems](https://pdos.csail.mit.edu/6.824/) course

## Introduction
This is my attempt to create a fault-tolerent Key/value store that supports sharding.
To achieve fault-tolerence, I will be implementing [Raft](https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf). From the [Raft website](https://raft.github.io/), "Raft is a consensus algorithm that is designed to be easy to understand. It’s equivalent to Paxos in fault-tolerance and performance."

This exercise is intended for getting deeper understanding of distributed system protocals.
NOT INTENDED FOR ANY PRODUCTION USE.

## References:
1. MIT 6.824 Distributed systems course: https://pdos.csail.mit.edu/6.824/. 
1. Raft extended paper: https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf
1. Visualization explaining Raft: http://thesecretlivesofdata.com/raft/
