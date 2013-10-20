# -*- coding: utf-8 -*-

# try loading a specific replay to debug it

import sc2reader

replay_path = './Polar Night LE (26).SC2Replay'

replay = sc2reader.load_replay(replay_path)

# doing replay.players will fail

replay.players

# second player has special character "ó" in name

print "player's name"
print replay.players[1].detail_data['name']

# explicitly encoding with utf-8 works

print "print with UTF-8 specified: "
print replay.players[1].detail_data['name'].encode('utf-8')

# using str() throws the error
print "print with str(): "
try:
	print str(replay.players[1].detail_data['name'])
except Exception as err:
	print err.__class__.__name__ + ": " + str(err)

# calling replay.players will cause error because of this also

print "now try calling Replay.players with player name :"
print replay.players
