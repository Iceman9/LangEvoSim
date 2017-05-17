from lang_gen import LanguageGenerator
from population import Population
from agent import Agent
from land import Realm

class Main:

    def __init__(self, num_of_populations=5):
        self.populations = []
        for i in range(num_of_populations):
            self.create_population()
        pass

    def create_population(self, size=20, num_of_words=100):
        pop = Population(num_of_words)
        # First the population needs a dictionary
        pop.create_dict()
        pop.populate(size)
        self.populations.append(pop)
        return pop

    def get_populations(self):
        return self.populations

if __name__ == '__main__':
    x = Main()
    list_of_populations = x.get_populations()
    print(list_of_populations)
    pop = list_of_populations[0]
    print(pop)
    agents_of_pop = pop.get_agents()
    print(agents_of_pop)
