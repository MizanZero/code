from enum import Enum

players=[]

class Role(Enum):
    bat=['batting','bat','ba','at','a','t', 1]
    bowl=['bowling','bowl','bo','ow','wl','bow','owl','o','w', 2]
    field=['fielding','field','f','i','e','d','fi','ie','el','fiel','ield', 3]


class player:
    def __init__(self, name:str, role:Role, score:int=0): 
        assert type(role)==Role, "Role should be from roles(Enum)"
        assert score>=0, "Score should greater than or equal to 0"

        self.name=name; self.role=role; self.score=score; self.history=[]
        players.append(self); self.index=len(players)

    def decorated(self):
        return [self.type.capitalize(),self.name.capitalize(), self.role.value[0].capitalize(), self.score]


class human(player):
    def __init__(self, *args):
        super().__init__(*args)
        self.type='human'
        
        assert self.name[:3].lower()!='bot', "Name should not be Bot"
        assert self.name not in [p.name for p in players[:-1]], "This name is already taken"


class bot(player):
    def __init__(self, *args):
        super().__init__(*args)
        self.type='bot'
        
        self.name='Bot'+str(len([p for p in players if p.type=='bot'])+1) # Bot1, Bot2, Bot3, ...


def deployBots(*roles:Role):
    for r in roles: players.append(bot('Bot', r)) 


p1=player('Player 1', Role.bat)

