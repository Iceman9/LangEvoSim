import random
import string
consonants = string.ascii_lowercase
vowels = "aeiou"

consonants = [char for char in consonants if char not in vowels]
vowels = [char for char in vowels]

vowel_mut = 0.1
conso_mut = 0.1
compo_mut = 0.1

conflict_chance = 0.0001


class Agent:
    def __init__(self, population=None):
        self.population = population

        self.pos = None
        self.dictionary = []
        self.used_consonants = []
        # It could be arbtrary:
        # self.traits = {}

    def add_to_vocabulary(self, word):
        for char in word:
            if char in consonants and char not in self.get_used_consonants():
                self.add_consonant(char)
        if word not in self.get_dictionary():
            self.dictionary.append(word)

    def get_dictionary(self):
        return self.dictionary

    def set_dictionary(self, dictionary, size=0.7):
        individual_dictionary = []
        dictionary_size = int(size * len(dictionary))
        while len(individual_dictionary) < dictionary_size:
            word = random.choice(dictionary)
            if word not in individual_dictionary:
                individual_dictionary.append(word)

        self.dictionary = individual_dictionary

    def get_used_consonants(self):
        return self.used_consonants

    def add_consonant(self, char):
        self.used_consonants.append(char)

    def get_population(self):
        return self.population

    def set_population(self, new_population):
        """Sets the population the agent belongs to.
        """
        self.population = new_population

    def get_position(self):
        """Get's the current location of the agent in a place.
        Example of position:
            self.pos = (1, 2)
        Returns:
            self.pos (touple): A set of N-dim coordinate
        """
        return self.pos

    def set_position(self, new_pos):
        self.pos = new_pos

    def bump_into_agent(self, other_agent):
        word = random.choice(self.dictionary)
        return word

    def got_bumped_by_agent(self, other_agent, word):
        # Do something with word
        # Mutate consonants and vowels or something
        word = self.mutate(word)
        self.add_to_vocabulary(word)
        return word

    def mutate(self, word):
        # Mutating one of the vowels
        if random.random() < vowel_mut:
            while 1:
                index = random.randint(0, len(word)-1)
                char = word[index]
                if char in vowels:
                    new_vowel = random.choice(vowels)
                    word = word[:index] + new_vowel + word[index + 1:]
                    break

        # TODO native consonant
        # conso_mut mutation should be higher than 10%
        if random.random() < conso_mut:
            while 1:
                index = random.randint(0, len(word)-1)
                char = word[index]
                if not char in vowels:
                    new_consonant = random.choice(consonants)
                    word = word[:index] + new_consonant + word[index + 1:]

                    break

        if random.random() < compo_mut:
            dict_word = random.choice(self.dictionary)
            if random.randint(0,1):
                word = word[:len(word)//2] + dict_word[len(dict_word)//2:]

        return word


if __name__ == '__main__':

    from lang_gen import LanguageGenerator

    generator = LanguageGenerator()

    x1 = Agent()
    x1.set_dictionary([generator.generate_word() for i in range(1000)])
    x2 = Agent()
    x2.set_dictionary([generator.generate_word() for i in range(1000)])
    import time
    print(x1.get_dictionary())
    print(x2.get_dictionary())
    for i in range(20):
        word = x1.bump_into_agent(x2)
        print('Word that first agent told to second agent: ', word)
        time.sleep(0.1)
        print('After bump: ', x2.got_bumped_by_agent(x1, word))
        print('\n')
