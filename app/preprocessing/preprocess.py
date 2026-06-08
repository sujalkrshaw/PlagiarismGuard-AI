import re
import string
from pathlib import Path


class TextPreprocessor:

    def __init__(self):
        pass

    def read_file(self, filepath):
        """
        Read text file
        """
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return ""

    def to_lowercase(self, text):
        """
        Convert text to lowercase
        """
        return text.lower()

    def remove_punctuation(self, text):
        """
        Remove punctuation
        """
        return text.translate(
            str.maketrans("", "", string.punctuation)
        )

    def remove_extra_spaces(self, text):
        """
        Remove multiple spaces
        """
        return re.sub(r"\s+", " ", text).strip()

    def tokenize(self, text):
        """
        Split into words
        """
        return text.split()

    def sentence_split(self, text):
        """
        Split into sentences
        """
        sentences = re.split(r"[.!?]+", text)
        return [s.strip() for s in sentences if s.strip()]

    def preprocess(self, text):

        original_length = len(text)

        text = self.to_lowercase(text)
        text = self.remove_punctuation(text)
        text = self.remove_extra_spaces(text)

        words = self.tokenize(text)
        sentences = self.sentence_split(text)

        return {
            "clean_text": text,
            "tokens": words,
            "sentences": sentences,
            "word_count": len(words),
            "sentence_count": len(sentences),
            "character_count": len(text),
            "original_length": original_length
        }


if __name__ == "__main__":

    processor = TextPreprocessor()

    sample_text = """
    Artificial Intelligence is transforming industries.
    AI helps automate tasks and improve productivity!
    """

    result = processor.preprocess(sample_text)

    print("\nClean Text:")
    print(result["clean_text"])

    print("\nTokens:")
    print(result["tokens"])

    print("\nSentences:")
    print(result["sentences"])

    print("\nStatistics:")
    print(f"Words: {result['word_count']}")
    print(f"Sentences: {result['sentence_count']}")