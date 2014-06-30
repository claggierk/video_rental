##########################
### Requirements ##########
##########################
In order to run, you must become a member of themoviedb
visit https://www.themoviedb.org/account/signup
Ultimately they will provide an API key

replace my key with YOUR key in Video.py (line 3):
{code}
tmdb = TMDB('3b2ff402b6a924b6caaa56f801fdb2e6') # API key given to me (had to register)
{code}

##########################
### commands to run ######
### see sample-run.txt ###
##########################

./lines.sh
python videoTests.py
python customerTests.py       
python videoRentalTests.py 
python main.py
