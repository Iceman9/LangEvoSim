import random
import string

consonants = string.ascii_lowercase
vowels = "aeiou"

consonants = [char for char in consonants if not char in vowels]
vowels = [char for char in vowels]

class LanguageGenerator:

    def __init__(self):
        pass

    def generate_word(self, min=5, max=8, mutation = 0.1):
        word_length = random.randint(min, max)
        
        last_draw = random.randint(0, 1)

        if last_draw:
            current_draw = random.choice(consonants)
        else:
            current_draw = random.choice(vowels)
        word = current_draw
        i = 1
        while i < word_length:
            if last_draw:
                current_draw = random.choice(vowels)
                last_draw = 0
            else:
                if i < word_length - 1 and mutation > random.random():
                    word += random.choice(consonants)
                    i = i + 1
                current_draw = random.choice(consonants)
                last_draw = 1
            i += 1
            word += current_draw

        return word

if __name__ == '__main__':
    import time
    print('Consonants: ', consonants)
    print('Vowels: ', vowels)

    generator = LanguageGenerator()
    print('Random words')
    for i in range(20):
        print(generator.generate_word())
    words = []
    for i in range(10000):
        words.append(len(generator.generate_word()))
    print('Longest words: ', max(words), 'Shortest words: ', min(words))

    # Performance
    start = time.time()
    x = [] 
    for i in range(100000):
        x.append(generator.generate_word(8,8))
    print('Time: ', time.time() - start, len(x))