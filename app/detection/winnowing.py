import hashlib


class Winnowing:

    def __init__(self, k=5):
        self.k = k

    def create_shingles(self, text):

        words = text.split()

        shingles = []

        for i in range(len(words) - self.k + 1):
            shingle = " ".join(words[i:i+self.k])
            shingles.append(shingle)

        return shingles

    def hash_shingles(self, shingles):

        hashes = []

        for shingle in shingles:

            hash_value = int(
                hashlib.md5(
                    shingle.encode()
                ).hexdigest(),
                16
            )

            hashes.append(hash_value)

        return hashes

    def generate_fingerprints(self, text):

        shingles = self.create_shingles(text)

        hashes = self.hash_shingles(shingles)

        return set(hashes)

    def similarity_score(self, text1, text2):

        fp1 = self.generate_fingerprints(text1)
        fp2 = self.generate_fingerprints(text2)

        intersection = len(fp1.intersection(fp2))
        union = len(fp1.union(fp2))

        if union == 0:
            return 0

        return round((intersection / union) * 100, 2)