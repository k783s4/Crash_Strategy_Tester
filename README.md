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
  <a style="padding: 0 10px;" href="#what-is-it">What it is</a> •
  <a style="padding: 0 10px;" href="#usage">What it's not</a> •
  <a style="padding: 0 10px;" href="#getting-started">Getting Started</a>
</p>

<p align="center"><b>Made by Leonardo Puzzuoli</b><p>

<p align="center"><h4 align="left">Background</h4>
<a href="https://roobet.com/"> Roobet </a> is a popular online casino where you can bet using cryptocurrencies. Crash is it's most well-known gamemode. In it a spaceship races up, taking with it a "multiplier value". Eventually the ship explodes. If a better has cashed out before then they will receive the multiplier value times their initial bet. If the ship explodes anybody still in the game will loose their bet. There is a chance for everyone to instantly loose their bet. This happens if the multiplier stop at 1.0x, in other words if the spaceship "explodes on the launch pad". This ensures that the game is in favour of the casino regardless of player behaviour.

<p align="center"><h4 align = "left"> What it is</h4></p>
<p> Before you can / should try you hand at gambling your should at least better understand your odds and the game you are playing. Unfortunately Crash is a very slow game. With only one round played every approximately seven seconds. This makes it impractical to test out strategies and inspect outcome data. Luckily in the interest of fairness the casino offers a way to calculate the outcome of the previous round programmatically, given the state data of the current round. With this we can iteratively collect all previous rounds that have been played in a certain session. A session lasts about 2 million games, spanning over multiple months. This program allows you to collect that data, program your trading strategies in a simple manner and replay a piece of the game's history in a matter of seconds, viewing the results and allowing for iterative design of the bots. After a few days of designing test strategies you should come to the conclusion that maximizing the odds of winning is possible, but requires large amounts of funds and is never guaranteed.</p>

![The tabulated result data](https://raw.githubusercontent.com/k783s4/Crash_Strategy_tester/master/results.png)
<small>Left shows simulation information, right is the amount of money each bot has left after every round. Not all bots make it to the end</small>

<p align="center"><h4 align = "left"> What it's not</h4></p>
This is not production-grade code. It is the result of four days of tinkering around, editing code and adding features as we went along. This is not an inivation to loose your money on an online betting site.</br></br>

<p align="center"><h4 align = "left"> Getting started</h4></p>
1.Download Project</br>
2.install required dependencies in pipfile</br>
3.Write your bots in the main.py file.</br>
> Each function is a different bot. Different bots receive different parameters. Bots need to return the exit multiplier followed by the bet
</br>
4. Run python ./test.py
</br></br>
