from enum import Enum

bat=['bat','ba','at','a','t', 1]
bowl=['bowl','bo','ow','wl','bow','owl', 2]

class roles(Enum):
    def display(player):
        return 'Batting' if player.role==bat else 'Bowling' 

class player:
    def __init__(self, name:str, role, score:int=0):
        assert role in [bat,bowl], "Role should be from roles(Enum)"
        assert score>=0, "Score should greater than or equal to 0"

        self.name=name; self.role=role; self.score=score


bot=player('Bot', bat) 


def switch(self, other=bot):
    self.role, other.role = other.role, self.role


print(roles.display(bot))