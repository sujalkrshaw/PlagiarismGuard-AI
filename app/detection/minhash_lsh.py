import random
import mmh3


class MinHash:

    def __init__(self, num_hashes=100):

        self.num_hashes = num_hashes

        random.seed(42)

        self.hash_seeds = [
            random.randint(1, 100000)
            for _ in range(num_hashes)
        ]

    def get_signature(self, tokens):

        signature = []

        for seed in self.hash_seeds:

            min_hash = float("inf")

            for token in tokens:

                hash_value = mmh3.hash(
                    token,
                    seed,
                    signed=False
                )

                min_hash = min(
                    min_hash,
                    hash_value
                )

            signature.append(min_hash)

        return signature


class LSH:

    def __init__(self, bands=20):

        self.bands = bands

    def similarity(self, sig1, sig2):

        matches = sum(
            1
            for a, b in zip(sig1, sig2)
            if a == b
        )

        return round(
            (matches / len(sig1)) * 100,
            2
        )