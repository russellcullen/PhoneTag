from game import *
from database_api import *
from user import *
from database_api import *


def changeScoreOnTag(gameID, time, lastIt):
	db = DatabaseApi('test')
	game = db.getGameByName(gameID)
	period = time - game.lastItTime
	assert(lastIt in game.negativeboard)
	game.negativeboard[lastIt] += period
	
def updateScores(game, time):
	db = DatabaseApi('test')
	#game = db.getGameByname(gameID)
	startTime = game.startTime
	leaderboard = game.leaderboard
	for (k,v) in leaderboard:
		if ( k != it):
			new_score = time - startTime - game.negativeboard[k]
			leaderboard[k] = new_score
			if (new_score >= game.scoreLimit):
				game.finished = True
	game.leaderboard = leaderboard
	db.updateGame(game.__dict__)
	
def updateScoresAll(time):
	db = DatabaseApi('test')
	games = db.getAllUnfinishedGames()
	for x in games:
		updateScores(x, time)
		

def checkFinishedAll(time):
	db = DatabaseApi('test')
	games = db.getAllUnfinishedGames()
	for x in games:
		if (time > (x.startTime + x.timeLimit)):
			x.finished = True
			db.updateGame(x.__dict__)