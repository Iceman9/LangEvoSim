
class Realm:

    def __init__(self):
        self.map = []

    def construct_basic_map(self, size_in_x=20, size_in_y=20):
        temp_map = [None for i in range(11, size_in_x * size_in_y + 11)]
        self.map = []
        for i in range(size_in_x):
            self.map.append(temp_map[size_in_y * i: size_in_y * (i + 1)])

    def get_map(self):
        return self.map

    def check_if_pos_is_taken(self, pos):
        x = pos[0]
        y = pos[1]
        try:
            return self.map[x][y]
        except IndexError:
            return True

    def move_agent_to_pos(self, agent, new_pos):
        map = self.get_map()
        new_x, new_y = new_pos
        map[new_x, new_y] = agent

if __name__ == '__main__':
    realm = Realm()
    realm.construct_basic_map()
    [print(i) for i in realm.get_map()]


    x = 5
    y = 5
    position_is_taken = realm.check_if_pos_is_taken((x, y))
    print(position_is_taken)

    x = 599999
    y = 509000
    position_is_taken = realm.check_if_pos_is_taken((x, y))
    print(position_is_taken)

    from agent import Agent
    map = realm.get_map()
    map[10][10] = Agent()
    x = 10
    y = 10
    position_is_taken = realm.check_if_pos_is_taken((x, y))
    print(position_is_taken)