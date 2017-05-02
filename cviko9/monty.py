from random import choice 

def play_game(strategy):
	_list = [0,1,2]
	treasure_door = choice(_list) #there is a treasure behind one door
	chosen_door = choice(_list) #player chooses one door
	_list.remove(treasure_door)
	if treasure_door != chosen_door: _list.remove(chosen_door)
	remaining_door = _list[0] #game master opens unchosen door without treasure	
	_list = [0,1,2]
	_list.remove(remaining_door)
	if strategy == 'stay':
		if chosen_door == treasure_door: return 1
		else: return 0
	if strategy == 'change':
		if chosen_door != treasure_door: return 1
		else: return 0

_list = []
for i in range(0,10000):
	_list.append(play_game('stay'))
print _list.count(1)


_list = []
for i in range(0,10000):
	_list.append(play_game('change'))
print _list.count(1)



