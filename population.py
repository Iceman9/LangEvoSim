from lang_gen import LanguageGenerator
from agent import Agent

import string

consonants = string.ascii_lowercase
vowels = "aeiou"

conson = [char for char in consonants if char not in vowels]
vowels = [char for char in vowels]


class Population:

    def __init__(self, max_words=100):
        self.max_words = max_words
        self.dictionary = []
        self.agents = []
        self.properties = {}

    def create_dict(self, vows=vowels, cons=conson, min=5, max=8, mut=0.1):
        generator = LanguageGenerator(vows, cons)

        counter = 0
        while counter < self.max_words:
            word = generator.generate_word(min, max, mut)
            if word not in self.dictionary:
                self.dictionary.append(word)
                counter += 1

    def get_dictionary(self):
        return self.dictionary

    def populate(self, number_of_agents=20):
        for i in range(number_of_agents):
            a = Agent(self)
            a.set_dictionary(self.get_dictionary())
            self.agents.append(a)

    def get_agents(self):
        return self.agents

    def remove_agent(self, agent):
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