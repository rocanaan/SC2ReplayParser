	
import sc2reader

replay = sc2reader.load_replay('/Users/rodrigocanaan/Dev/sc2reader/test_replays/1.0.0.16117/1.SC2Replay', load_map=True)

print(replay.players[0])
print(replay.players[1])
print(replay.map.name)
print(replay.map.hash)
for e in replay.events:
	print(e)


p1 = replay.players[0]
p2 = replay.players[1]


# for unit in p1.units:
# 	print (unit)