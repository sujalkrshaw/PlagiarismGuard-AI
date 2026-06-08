class SimilarityEngine:

    def __init__(self):
        pass

    def calculate_similarity(self, text1_tokens, text2_tokens):

        set1 = set(text1_tokens)
        set2 = set(text2_tokens)

        common_words = set1.intersection(set2)

        similarity = (
            len(common_words)
            / max(len(set1), len(set2))
        ) * 100

        return {
            "common_words": list(common_words),
            "matching_count": len(common_words),
            "similarity_percentage": round(similarity, 2)
        }