class RabinKarpMatcher:

    def __init__(self):
        self.base = 256
        self.prime = 101

    def search(self, text, pattern):

        n = len(text)
        m = len(pattern)

        if m > n:
            return []

        pattern_hash = 0
        text_hash = 0
        h = 1

        matches = []

        for i in range(m - 1):
            h = (h * self.base) % self.prime

        for i in range(m):
            pattern_hash = (
                self.base * pattern_hash + ord(pattern[i])
            ) % self.prime

            text_hash = (
                self.base * text_hash + ord(text[i])
            ) % self.prime

        for i in range(n - m + 1):

            if pattern_hash == text_hash:

                match = True

                for j in range(m):
                    if text[i + j] != pattern[j]:
                        match = False
                        break

                if match:
                    matches.append(i)

            if i < n - m:

                text_hash = (
                    self.base
                    * (text_hash - ord(text[i]) * h)
                    + ord(text[i + m])
                ) % self.prime

                if text_hash < 0:
                    text_hash += self.prime

        return matches