from pathlib import Path


class FileLoader:

    @staticmethod
    def load_text_file(filepath):

        try:

            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()

        except Exception as e:

            print(f"Error: {e}")
            return ""