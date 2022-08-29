<h1 align="center">📈 Crash Strategy Tester 🌎</h1>
<p align="center">A machine to simulate bot betting strategies on a popular online casino</p>

<p align="center">

<a>
<a style="margin: 0 5px" href="https://opensource.org/licenses/Apache"><img src="https://img.shields.io/badge/license-Apache-%23feca57" alt="GitHub license"></a>
</a>

<a>
<a style="margin: 0 5px" href="https://opensource.org/licenses/Apache"><img src="https://img.shields.io/badge/status-release-%51AB75" alt="GitHub license"></a>
</a>

</p>

<p align="center">
<a style="padding: 0 10px;" href="#background">Background</a> •
<a style="padding: 0 10px;" href="#what-it-is">What it is</a> •
<a style="padding: 0 10px;" href="#what-its-not">What it's not</a> •
<a style="padding: 0 10px;" href="#getting-started">Getting Started</a>
</p>

<p id = "background" align="center"><b>Made by Leonardo Puzzuoli</b><p>

<p align="center"><h4 align="left">Background</h4>
<a href="https://roobet.com/"> Roobet </a> is a popular online casino where you can bet using cryptocurrencies. "Crash" is its most well-known game mode. In it, a spaceship races upward, taking with it a "multiplier value" until the ship randomly explodes. If a better has cashed out beforehand, they will receive the multiplier value at the time of cashing out times their initial bet. Anybody left in the game when the ship explodes will lose their bet. There is a chance for everyone to lose their bet instantly. This happens if the multiplier stops at 1.0x, in other words, if the spaceship "explodes on the launch pad". This ensures the game is in favor of the casino regardless of player behavior.

<p id="what-it-is" align="center"><h4 align = "left"> What it is</h4></p>
<p> Before you can / should try your hand at gambling you should at least better understand your odds and the game you are playing. Unfortunately Crash is a very slow game, with only one round played every approximately seven seconds. This makes live testing of betting strategies and outcome data on the website impractical. Luckily, in the interest of fairness, the casino offers a way to calculate the outcome of the previous round programmatically, given the state data of the current round. With this we can iteratively collect all previous rounds that have been played in a certain session. A session lasts about 2 million games, spanning over multiple months. This program allows you to collect that data, program your trading strategies in a simple manner and replay a piece of the game's history in a matter of seconds, viewing the results and allowing for iterative design of the betting bots. After a few days of designing test strategies you should come to the conclusion that maximizing the odds of winning is possible, but requires large amounts of funds and is never guaranteed.</p>

![The tabulated result data](https://raw.githubusercontent.com/k783s4/Crash_Strategy_tester/master/results.png)
<small>Left shows simulation information, right is the amount of money each bot has left after every round. Not all bots make it to the end</small>

<p id="what-its-not" align="center"><h4 align = "left"> What it's not</h4></p>
This is not production-grade code. It is the result of four days of tinkering around, editing code and adding features as we went along. This is not an invitation to lose your money on an online betting site.</br></br>

<p id="getting-started" align="center"><h4 align = "left"> Getting started</h4></p>
1.Download Project</br>
2.install required dependencies in pipfile</br>
3.Write your bots in the main.py file.</br>
> Each function is a different bot. Different bots receive different parameters. Bots need to return the exit multiplier followed by the bet
</br>
4.Get the game data using get_file.py by pasting the current and first game hash into the file (can be found by clicking on past games in the timeline in Crash)
 and renaming the file multipliers.csv</br>
 Alternatively just use old real game data and rename multipliers_old.csv to multipliers.csv</br>
 5. Run python ./test.py
</br></br>
