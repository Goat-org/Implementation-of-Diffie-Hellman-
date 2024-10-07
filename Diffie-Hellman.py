# A simple example of Diffie-Hellman Key Exchange using small numbers.

class SimpleDiffieHellman:
    """
    This class demonstrates the Diffie-Hellman key exchange using small numbers.
    """

    def __init__(self, p, g, private_key):
        # Save prime, base (generator), and private key for each user
        self.p = p
        self.g = g
        self.private_key = private_key
        # Calculate the public key: (base ** private_key) % prime
        self.public_key = (g ** private_key) % p

    def generate_shared_secret(self, other_public_key):
        # Calculate the shared secret: (other_public_key ** private_key) % prime
        self.shared_secret = (other_public_key ** self.private_key) % self.p
        return self.shared_secret

def main():
    # We choose a small prime number and base for simplicity
    p = 23  # A small prime number
    g = 5    # Base (also known as generator)

    # Each person picks a private key (kept secret)
    alice_private_key = 6
    bob_private_key = 15

    # Create Alice's and Bob's objects for the key exchange
    alice = SimpleDiffieHellman(p, g, alice_private_key)
    bob = SimpleDiffieHellman(p, g, bob_private_key)

    # Alice and Bob exchange public keys and generate their shared secret
    alice_shared_secret = alice.generate_shared_secret(bob.public_key)
    bob_shared_secret = bob.generate_shared_secret(alice.public_key)

    # Print the public keys and shared secrets
    print("Alice's Public Key:", alice.public_key)
    print("Bob's Public Key:", bob.public_key)

    print("Alice's Shared Secret:", alice_shared_secret)
    print("Bob's Shared Secret:", bob_shared_secret)

    # Check if the shared secrets are the same
    if alice_shared_secret == bob_shared_secret:
        print("Shared secret match! The key exchange was successful.")
    else:
        print("Shared secrets don't match! Something went wrong.")

if __name__ == "__main__":
    main()
