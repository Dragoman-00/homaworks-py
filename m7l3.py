class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                words = []
                for line in f:
                    line = line.strip().lower()
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        found_words = {}
        for file_name, words in all_words.items():
            if word in words:
                found_words[file_name] = words.index(word)
        return found_words

    def count(self, word):
        all_words = self.get_all_words()
        counted_words = {}
        for file_name, words in all_words.items():
            counted_words[file_name] = words.count(word)
        return counted_words


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('text')) # 3 слово по счёту
print(finder2.count('text')) # 4 слова teXT в тексте всего