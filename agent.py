import random

consonants = string.ascii_lowercase
vowels = "aeiou"

consonants = [char for char in consonants if not char in vowels]
vowels = [char for char in vowels]

vowel_mut = 0.1
conso_mut = 0.9
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

    def set_dictionary(self, dictionary):
        self.dictionary = dictionary

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
        other_agent.got_bumped_by_agent(self, word)

    def got_bumped_by_agent(self, other_agent, word):
        # Do something with word
        # Mutate consonants and vowels or something
        word = self.mutate(word)
        self.add_to_vocabulary(word)

    def mutate(self, word):
        # Mutating one of the vowels
        if random.random() < vowel_mut:
            while 1:
                index = random.randint(0, len(word)-1)
                char = word[index]
                if char in vowels:
                    new_vowel = random.choice(vowels)
                    word = word[:i] + new_vowel + word[i+1:]
                    break

        # TODO native consonant
        # conso_mut mutation should be higher than 10%
        if random.random() < conso_mut:
            while 1:
                index = random.randint(0, len(word)-1)
                if not char in vowels:
                    new_consonant = random.choice(consonants)
                    word = word[:i] + new_consonant + word[i+1:]
                    break

        if random.random() < compo_mut:
            dict_word = random.choice(self.dictionary)
            word = word + dict_word

        return word
