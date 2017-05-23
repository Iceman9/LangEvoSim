from lang_gen import LanguageGenerator
from agent import Agent

import string

consonants = string.ascii_lowercase
vowels = "aeiou"

conson = [char for char in consonants if char not in vowels]
vowels = [char for char in vowels]


class Population:
    """Class Population creates a population of agents and assigns them a
    newly generated language.

    Longer description

    __init__ parameters:
    :param max_words: default=100; an input argument max_words sets the number of words in a generated language
    :type max_words: int

    __init__ variables:
    :var self.max_words: number of words in a language
    :var self.dictionary: dictionary of generated words for a population that forms a language
    :var agents: agents of a population
    :var properties: TODO

    """
    def __init__(self, max_words=100):
        self.max_words = max_words
        self.dictionary = []
        self.agents = []
        self.properties = {}

    def create_dict(self, vows=vowels, cons=conson, min=5, max=8, mut=0.1):
        """Creates a new language and assigns is to a population in the making.

        Longer description

        :param vows: vowels from which the language for the population is created
        :type vows: list
        :param cons: consonants from which the language for the population is created
        :type cons: list
        :param min: minimally long word in the population's language
        :type min: int
        :param max: maximally long word in the population's language
        :type max: int
        :param mut: possibility of a mutation occuring in a word of the population's language
        :type mut: float
        """
        generator = LanguageGenerator(vows, cons)

        counter = 0
        while counter < self.max_words:
            word = generator.generate_word(min, max, mut)
            if word not in self.dictionary:
                self.dictionary.append(word)
                counter += 1

    def get_dictionary(self):
        """Returns Population object's language/dictionary (list).
        """
        return self.dictionary

    def populate(self, number_of_agents=20):
        """Generates a number of agents in the population.

        :param number_of_agents: default=20; sets the number of agents in the population
        :type number_of_agents: int
        """
        for i in range(number_of_agents):
            a = Agent(self)
            a.set_dictionary(self.get_dictionary())
            self.agents.append(a)

    def get_agents(self):
        """Returns a list of agents in the population.
        """
        return self.agents

    def remove_agent(self, agent):
        """Removes an Agent object from the population.

        :param agent: name of the agent that is to be removed
        :type agent: string
        """
        agents = self.get_agents()
        index = agents.index(agent)
        agents.pop(index)
        del agent

if __name__ == '__main__':
    import random
    pop = Population()
    pop.create_dict()
    print(pop.get_dictionary())
    pop.populate(100)
    agents = pop.get_agents()

    for agent in agents:
        print(agent.get_dictionary())

    random_agent = random.choice(pop.get_agents())
    pop.remove_agent(random_agent)
    print(len(pop.get_agents()))
