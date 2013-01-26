from game import *
from database_api import *
from user import *
from database_api import *


databaseName = 'heroku_app11283429'

def changeScoreOnTag(gameID, time, lastIt):
	db = DatabaseApi(databaseName)
	game = db.getGameByName(gameID)
	#print game
	period = time - game.lastItTime
	#assert(lastIt in game.negativeboard)
	game.negativeboard[lastIt] += period
	game.lastItTime = time

	db.updateGame(game.__dict__)
	
def updateScores(game, time):
	db = DatabaseApi(databaseName)
	startTime = game.startTime
	leaderboard = game.leaderboard
	for k,v in leaderboard.iteritems():
		if k != game.it:
			new_score = time - startTime - game.negativeboard[k]
			leaderboard[k] = new_score
			#if (new_score >= game.scoreLimit):
				#game.finished = True
	game.leaderboard = leaderboard
	db.updateGame(game.__dict__)
	
def updateScoresAll(time):
	db = DatabaseApi(databaseName)
	games = db.getAllUnfinishedGames()
	for x in games:
		updateScores(x, time)
		

def checkFinishedAll(time):
	db = DatabaseApi(databaseName)
	games = db.getAllUnfinishedGames()
	for x in games:
		if (time > (x.startTime + x.timeLimit)):
			x.finished = True
			db.updateGame(x.__dict__)