# Marmots vs Multisignatures
**Category:** Crypto
**Difficulty:** Hard

## Description
The Marmot Intelligence, Informatics, Intervention, Investigation & Interception Institute (MI6) intercepted network traffic between members of Coati Intelligence Agency (CIA) using a multi-signature scheme to sign important messages. What the coatis don't know is that their implementation of the algorithm includes a backdoor planted by an agent of MI6. Now, as part of the Operation Marmots vs Multisignatures (Operation MVM), the marmots want to recover the private key of coati agent with ID `5e547334-68c1-4ca2-9748-57f560372648`. Help them perform this task so that they can impersonate the coati agents later!

## Solution
The application implements a scheme described in [https://eprint.iacr.org/2023/155.pdf](https://eprint.iacr.org/2023/155.pdf). However, here the values of z and r are relatively small, making it possible to reduce the problem of recovering the secret key to the hidden number problem.