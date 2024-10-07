# Overview

The Diffie-Hellman (DH) algorithm is a secure method for two parties to share a secret cryptographic key over an insecure communication channel. It is widely used in secure communication protocols, such as HTTPS, SSH, and VPNs, to enable secure key agreement between two parties who have never communicated before.

In this repository, we simulate the key exchange between two individuals, Alice and Bob, using a small prime number and a base. This allows both parties to generate a shared secret key, which can be used for encrypted communication.

The process of Diffie Hellman (Given Bob and Alice wanna share a secret key on an unscure network)

1. Select a Prime Number and a Generator:

    * Given Alice and Bob agree on a large prime number p (also called the modulus) and a generator g (also called the base/ generator prime), which is typically a small integer.
    * Both p and g are public values and can be shared openly without compromising security.

2. Generate Private Keys:

    * Alice and Bob each generate their own private keys. Let's say Alice picks a private key a, and Bob picks a private key b.
    * These private keys are large random numbers that are kept secret.

3. Compute Public Keys:

    * Alice computes her public key A = g**a mod p and sends it to Bob.
    * Bob computes his public key B = g**b mod p and sends it to Alice.

4. Compute Shared Secret:

    * Alice takes Bob's public key B and raises it to the power of her private key a: S1 = B**a mod p.
    * Bob takes Alice's public key A and raises it to the power of his private key b: S2 = A**b mod p.
    * Due to the properties of modular arithmetic, both Alice and Bob end up with the same shared secret.

In the Diffie-Hellman key exchange, the shared secret key is computed as:

## Alice’s Calculation: shared_secret = (Bob’s public key)**Alice’s private key % p

## Bob’s Calculation: shared_secret = (Alice’s public key)**Bob’s private key % p
