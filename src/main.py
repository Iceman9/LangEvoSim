from lang_gen import LanguageGenerator
from population import Population
from agent import Agent
from land import Realm

class Main:

    def __init__(self):
        self.populations = []
        self.world = []
        self.settings = {
            'size': 20,
            'num_of_words': 100,
            'number_of_agents': 20,
            'land_size': (20, 20),
            'frame': 100,
            #TODO advanced settings
        }

    def create_population(self):
        pop = Population(self.settings['number_of_agents'])
        # First the population needs a dictionary
        pop.create_dict()
        pop.populate(self.settings['size'])
        self.populations.append(pop)
        return pop

    def create_x_populations(self, N):
        for i in range(N):
            self.create_population()
        return

    def set_setting(self, **kwargs):
        for key in kwargs:
            if key in self.settings:
                self.settings[key] = kwargs[key]
            else:
                print('Key: ', key, ' not in settings.')

    def set_default_settings(self):
        self.settings = {
            'size': 20,
            'num_of_words': 100,
            'number_of_agents': 20,
            'frame': 100,
            #TODO advanced settings
        }

    def get_populations(self):
        return self.populations

    def plant_populations(self):
        populations = self.get_populations()

        for population in populations:
            land = Realm()
            land.construct_basic_map()
            self.world.append(land)
            agents = population.get_agents()
            for agent in agents:
                land.plant_agent(agent)


    def get_world(self):
        return self.world

    def step(self):
        populations = self.get_populations()

        for population in populations:

            agents = population.get_agents()

            for agent in agents:
                land = agent.get_land()
                map = land.get_map()
                pos = agent.get_position()

                # Move agent
                # Get all possible movements for current agent.
                # Randomly choose a move.
                moves = land.get_possible_moves(pos)

                if moves:
                    new_pos, residence, vektor = random.choice(moves)

                    if residence:
                        # residence is an other angent
                        other_agent = residence
                        bump_word = agent.bump_into_agent(other_agent)
                        received_word = other_agent.got_bumped_by_agent(agent,
                                                                    bump_word)
                        print(bump_word, received_word)

                    else:
                        # This is an empty space
                        land.move_agent_to_pos(agent, new_pos)
                else:
                    raise RuntimeError

    def start(self, frame=None):
        if frame is None:
            frame = self.settings['frame']

        counter = 0
        while counter < frame:
            self.step()
            counter += 1

if __name__ == '__main__':
    sim = Main()
    # First lets create a special snowflake population
    sim.set_setting(size=5)
    special_pop = sim.create_population()
    special_agent = special_pop.create_agent()

    sim.set_default_settings()
    sim.create_x_populations(2)

    print('Special population:', special_pop)
    print('All populations:', sim.get_populations())


    #land = Realm()
    # land.construct_basic_map()

    sim.plant_populations()

    world = sim.get_world()
    import random
    selected_map = random.choice(world)
    print(selected_map)

    # SIM TIMEEEEE

    sim.start()
