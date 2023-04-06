# East Blue :ocean:

This was my first repo and is now where I dump various smaller scripts I decide to work on. 


## Games :video_game:

This repo was initially just Python scripts for games and is currently mainly that too. I made these games with the intention of making them as smooth an experience as I could think up at the time, giving the ability to stop the game whenever reasonable and minimize the possibility of user input creating errors that would break the script.


### Hangman :standing_person:

The first game I worked on as part of a bootcamp as the final Python challenge. I made some changes and chucked it in here along with the required file that I was provided.

This script uses random to select a random word from the file and plays like you'd expect.


### Naughts and Crosses :radio_button: :heavy_multiplication_x: 

This exists in the xo directory, when you run the script, it will give you the option of which symbol you want to use. The script will always go first, use coordinates(a1 to c3) to place your symbol on various positions on the grid.

This uses random to select a random position on the grid, this means you'll have an easy time against the script in almost all cases.


### Rock Paper Scissors :gem: :page_facing_up: :scissors:
Random is used to select Rock, Paper, or Scissors and as you play, the script keeps track. I tried to make this script pace itself more so the experience is more interesting.


## Other scripts

### Exponential squaring :infinity: :weight_lifting:

This script also exists in my Golden Age repo, but it's just a random script that I made as a POC in my spare time to add weighting to numbers. The use case was to add a recency bias for alerting based on certain criteria within the past 30 days, so I needed a sharp increase in weight per number. 

I'd normally get the maximum weighting and alert based on a certain percentage of the total. The number that needs to be compared would usually be gathered by a for loop that would add the current counter total to a list when certain requirements are met.

VERY specific use case, but I'm throwing it here in case it comes handy somewhere else. The original POC bash script, the fit for purpose Python version of the script, and the recreated Go package are here. 
