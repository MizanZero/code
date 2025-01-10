from enum import Enum


class role(Enum):
    bat=['bat','ba','at','a','t', 1]
    bowl=['bowl','bo','ow','wl','bow','owl', 2]


class player:
    def __init__(self, name:str, role:Enum, score:int=0):
        assert role in ['bat','bowl'], "Role should be 'bat' or 'bowl'"
        assert score>=0, "Score should greater than or equal to 0"

        self.name=name; self.role=role; self.score=score


com=player('Bot','bat')


def switch(self, other=com):
    self.role, other.role = other.role, self.role


