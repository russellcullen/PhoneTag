PhoneTag
========

User object 
{
	_id : ObjectID
	phoneID : String
	name : String
	location : Location (lat, long)
	friends : ObjectID[]
	games : ObjectID[]
}

Game object
{
	_id : ObjectID
	users : ObjectID[]
	isIt : ObjectID
}

GCM Message
{

}

Database Functions (JON)
-----
newUser(user);
updateUser(user, something);
newGame();
updateGame();
deleteGame();
addUserToGame(user, game);
removeUser(user);


Server Functions (VSAI, NORBS)
-----
registerPhone(name);
updateLocs(lat, long);
joinGame();
updatePhone(whosIt, location{});


Android
-----
