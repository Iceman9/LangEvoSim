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
    """Class Agent initializes an object that represents one linguistic agent in
    a population.

    Attributes:
        population (Population): The population the Agent belongs to.
        pos (touble): The position of the Agent on a map.
        dictionary (list): Agents list of vocabulary.
        used_consonants (list): List of used consonants, these can be modified
            to expand it's vocabulary through mutation.
    """
    def __init__(self, population=None):
        """
        Parameters:
            population (Population): The population that the agent belongs to.
        """

        self.population = population

        self.pos = None
        self.land = None
        self.dictionary = []
        self.used_consonants = []
        # It could be arbitrary:
        # self.traits = {}

    def __repr__(self):
        return 'Agent'

    def add_to_vocabulary(self, word):
        """Adds a new, unfamiliar word from another Agent object into its own
        vocabulary when another Agent object bumps into it. Adds a new,
        unfamiliar consonant into its own dictionary of consonants if such a
        consonant is present in the word.

        Parameters:
            word (str): an input argument word is received when Agent object
                gets bumped into by another Agent object
        """

        for char in word:
            if char in consonants and char not in self.get_used_consonants():
                self.add_consonant(char)
        if word not in self.get_dictionary():
            self.dictionary.append(word)

    def get_dictionary(self):
        """Returns Agent object's dictionary/vocabulary (list).
        """

        return self.dictionary

    def set_dictionary(self, dictionary, size=0.7):
        """Sets Agent object's self.dictionary (vocabulary) from Agent's
        population's language.

        Parameters:
            dictionary (list): an input argument dictionary is the Agent's
                population's language
            size (float): default=0.7 (min=0.0, max=1.0); denotes random
                portion of the Agent's population's language the Agent object
                gets
        """
        individual_dictionary = []
        dictionary_size = int(size * len(dictionary))
        while len(individual_dictionary) < dictionary_size:
            word = random.choice(dictionary)
            if word not in individual_dictionary:
                individual_dictionary.append(word)

        self.dictionary = individual_dictionary

    def get_used_consonants(self):
        """Returns consonants (list) in the Agent object's vocabulary.
        """
        return self.used_consonants

    def add_consonant(self, char):
        """Adds a new, unfamiliar consonant into Agent object's dictionary of
        consonants.

        Parameters:
            char (string): an input argument char is the consonant to be added
        """
        self.used_consonants.append(char)

    def get_population(self):
        """Returns the population (string) the Agent object belongs to.
        """
        return self.population

    def set_population(self, new_population):
        """Sets the population the agent belongs to.
        """
        self.population = new_population

    def get_land(self):
        return self.land

    def set_land(self, new_land):
        self.land = new_land

    def get_position(self):
        """Gets the current location of the agent in a place.
        Example of position: *self.pos = (1, 2)*

        Returns:
            self.pos (touple): A set of N-dim coordinate
        """
        return self.pos

    def set_position(self, new_pos):
        """Sets Agent object to its new position (touple).

        Parameters:
            new_pos (touple): an input argument new_pos is the new Agent
                object's position on the map
        """
        self.pos = new_pos

    def bump_into_agent(self, other_agent):
        """Returns a random word from the dictionary of the Agent object bumps
        into another Agent object.

        Parameters:
            other_agent (string): an input argument other_agent represents some
                other Agent object that is being bumped

        """
        word = random.choice(self.dictionary)
        return word

    def got_bumped_by_agent(self, other_agent, word):
        """Returns a random word with possible mutation that the Agent object
        receives from another Agent object that bumped into it. It is added to
        the Agent object's vocabulary.

        Parameters:

            other_agent (Agent): an input argument other_agent represents some
                other Agent object that is bumping into object Agent
            word (string): an input argument word is a random word from the
                other Agent object's dictionary

        """
        # Do something with word

        # Mutate consonants and vowels or something

        # TODO add to vocabulary after mutation only if not in vocabulary yet,
        # this ensures that existing words from vocabulary can mutate
        word = self.mutate(word)
        self.add_to_vocabulary(word)
        return word

    def mutate(self, word):
        """Returns possibly mutated new, unfamiliar word the Agent object learns
        through bumping.

        The word undergoes possible mutation with globally specified
        possibility. The word's vowel can bu mutated into another vowel and the
        word's consonant can be mutated into another consonant. Both mutations
        source from the Agent object's vowel and consonant dictionary. This
        assures possibility that new, unfamiliar consonants can become a part
        of words. The final word is added into Agent object's vocabulary.

        Parameters:
            word (string): an input argument word is a random word from bumping
                Agent object's vocabulary that undergoes possible mutation
        """
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
