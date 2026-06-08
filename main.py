from app.utils.file_loader import FileLoader
from app.preprocessing.preprocess import TextPreprocessor
from app.detection.similarity import SimilarityEngine
from app.detection.minhash_lsh import MinHash, LSH

processor = TextPreprocessor()
similarity_engine = SimilarityEngine()

original_text = FileLoader.load_text_file(
    "data/originals/original.txt"
)

submission_text = FileLoader.load_text_file(
    "data/submissions/submission.txt"
)

original = processor.preprocess(original_text)
submission = processor.preprocess(submission_text)

result = similarity_engine.calculate_similarity(
    original["tokens"],
    submission["tokens"]
)

print("\n========== DOCUMENT ANALYSIS REPORT ==========")

print("\nOriginal Document Words:")
print(original["word_count"])

print("\nSubmission Document Words:")
print(submission["word_count"])

print("\nSimilarity Percentage:")
print(result["similarity_percentage"], "%")

print("\nMatching Words:")
print(result["matching_count"])

print("\nCommon Words:")
print(result["common_words"])

from app.detection.winnowing import Winnowing

winnowing = Winnowing()

winnow_score = winnowing.similarity_score(
    original["clean_text"],
    submission["clean_text"]
)

print("\n========== WINNOWING REPORT ==========")

print("\nFingerprint Similarity:")
print(winnow_score, "%")

print("\n========== MINHASH REPORT ==========")

minhash = MinHash()

sig1 = minhash.get_signature(
    original["tokens"]
)

sig2 = minhash.get_signature(
    submission["tokens"]
)

lsh = LSH()

minhash_score = lsh.similarity(
    sig1,
    sig2
)

print("\nMinHash Similarity:")
print(minhash_score, "%")