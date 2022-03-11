from rich.progress import track
import main
from rich.console import Console
from rich.table import Table
import time
import csv
import matplotlib.pyplot as plt

result = []
LINE_COUNT = 0
#open past games file
csvfile = open("multipliers.csv", "r")
datareader = csv.reader(csvfile)
for n in datareader:
    LINE_COUNT += 1

print(LINE_COUNT)

csvfile.close()
csvfile = open("multipliers.csv", "r")
datareader = csv.reader(csvfile)

#for bot one
#-------------------------------------------------------------------------------

balance_history = []

#full range
balance_history_this = []
test_cases = LINE_COUNT
successes = 0
failures = 0
balance = 500
bank = 0
prev_out = [0,0]
prev = True
MAX_LOSS = 0.7
remainder = balance * MAX_LOSS

for test_cases in track(range(test_cases), description="[green]Testing bot [bold]one[/bold] using [bold white]full range[/bold white]..."):
    balance_history_this.append(balance)
    #calculate bot [cutoff, size]
    botout = main.bot(balance, prev, prev_out, remainder)
    #actual cutoff
    actual = next(datareader)
    #if cutoff is a success
    #if(test_cases < 2000):
        #temp = ""
        #if(botout[0] < float(actual[0])):
        #    temp = str((float(botout[0]) * botout[1]) - float(botout[1]))
        #else:
        #    temp = "-" + str(botout[1])
        #print("bot: " + str(botout[0]) + " actual: " + str(actual[0]) + " size: " + str(botout[1]) + " res: " + temp)
    if(botout[0] < float(actual[0])):
        #successful prediction
        successes += 1
        prev = True
        balance += (float(botout[0]) * botout[1]) - float(botout[1])
        prev_out = botout
        remainder = balance * MAX_LOSS
    else:
        #failed prediction
        failures += 1
        balance -= botout[1]
        remainder -= botout[1]
        if(balance <= 0):
            break
        prev_out = botout
        prev = False

    #if bot wants to cash out
    if(botout[2]):
        bank = balance - 500
        balance = 500
        remainder = balance * MAX_LOSS

    if(balance < 500 and bank > 500):
        bank += balance
        balance = 500
        bank -= 500

#save results
res = []
res.append("One")
res.append("0 - " + str(test_cases))
res.append("$500")
res.append("$" + str(bank + balance))
res.append("$" + str(bank + balance - 500))
if(bank + balance - 500 > 0):
    res.append("[green]PASSED")
else:
    res.append("[red]FAILED")
result.append(res)
balance_history.append(balance_history_this)
#select random range

#test bot on range

#for bot two
#-------------------------------------------------------------------------------
csvfile.close()
csvfile = open("multipliers.csv", "r")
datareader = csv.reader(csvfile)

#full range
balance_history_this = []
test_cases = LINE_COUNT
successes = 0
failures = 0
balance = 500
prev_out = [0,0]
prev = True
remainder = 0
prev_high = 500

for test_cases in track(range(test_cases), description="[green]Testing bot [bold]two[/bold] using [bold white]full range[/bold white]..."):
    balance_history_this.append(balance)
    #calculate bot [cutoff, size]
    botout = main.two(balance, prev, prev_out,remainder)
    if(botout[1]>balance):
        botout[1] = balance
    #actual cutoff
    actual = next(datareader)
    #if cutoff is a success
    temp = ""
    #if(botout[0] < float(actual[0])):
    #    temp = str((float(botout[0]) * botout[1]) - float(botout[1]))
    #else:
    #    temp = "-" + str(botout[1])
    #print("bot: " + str(botout[0]) + " actual: " + str(actual[0]) + " size: " + str(botout[1]) + " res: " + temp)
    if(botout[0] < float(actual[0]) and botout[0] > 1):
        #successful prediction
        successes += 1
        prev = True
        balance += (float(botout[0]) * botout[1]) - float(botout[1])
        prev_out = botout
        remainder = balance - prev_high
    else:
        #failed prediction
        failures += 1
        balance -= botout[1]
        if(balance <= 0):
            break
        prev_out = botout
        prev = False
        remainder = 0

#save results
res = []
res.append("Two")
res.append("0 - " + str(test_cases))
res.append("$500")
res.append("$" + str(balance))
res.append("$" + str(balance - 500))
if(balance - 500 > 0):
    res.append("[green]PASSED")
else:
    res.append("[red]FAILED")
result.append(res)
balance_history.append(balance_history_this)

#for bot three
#-------------------------------------------------------------------------------
csvfile.close()
csvfile = open("multipliers.csv", "r")
datareader = csv.reader(csvfile)

#full range
balance_history_this = []
test_cases = LINE_COUNT
successes = 0
failures = 0
balance = 21000
prev_out = [0,0]
prev = True
losstreak = 0

for test_cases in track(range(test_cases), description="[green]Testing bot [bold]three[/bold] using [bold white]full range[/bold white]..."):
    balance_history_this.append(balance)
    #calculate bot [cutoff, size]
    botout = main.three(balance, prev, prev_out, losstreak)
    if(botout[1]>balance):
        botout[1] = balance
    #actual cutoff
    actual = next(datareader)
    #if cutoff is a success
    temp = ""
    #if(botout[0] < float(actual[0])):
    #    temp = str((float(botout[0]) * botout[1]) - float(botout[1]))
    #else:
    #    temp = "-" + str(botout[1])
    #print("bot: " + str(botout[0]) + " actual: " + str(actual[0]) + " size: " + str(botout[1]) + " res: " + temp)
    if(botout[0] < float(actual[0]) and botout[0] > 1):
        #successful prediction
        losstreak = 0
        successes += 1
        prev = True
        balance += (float(botout[0]) * botout[1]) - float(botout[1])
        prev_out = botout
    else:
        #failed prediction
        losstreak += 1
        if(botout[1] == 0.04):
            losstreak = 0
        failures += 1
        balance -= botout[1]
        if(balance <= 0):
            break
        prev_out = botout
        prev = False

#save results
res = []
res.append("Three")
res.append("0 - " + str(test_cases))
res.append("$21000")
res.append("$" + str(balance))
res.append("$" + str(balance - 21000))
if(balance - 21000 > 0):
    res.append("[green]PASSED")
else:
    res.append("[red]FAILED")
result.append(res)
balance_history.append(balance_history_this)

#for bot four
#-------------------------------------------------------------------------------
csvfile.close()
csvfile = open("multipliers.csv", "r")
datareader = csv.reader(csvfile)

#full range
balance_history_this = []
test_cases = LINE_COUNT
successes = 0
failures = 0
balance = 1000
prev_out = [0,0]
prev = True

for test_cases in track(range(test_cases), description="[green]Testing bot [bold]four[/bold] using [bold white]full range[/bold white]..."):
    balance_history_this.append(balance)
    #calculate bot [cutoff, size]
    botout = main.four(balance, prev, prev_out)
    if(botout[1]>balance):
        botout[1] = balance
    #actual cutoff
    actual = next(datareader)
    #if cutoff is a success
    temp = ""
    #if(botout[0] < float(actual[0])):
    #    temp = str((float(botout[0]) * botout[1]) - float(botout[1]))
    #else:
    #    temp = "-" + str(botout[1])
    #print("bot: " + str(botout[0]) + " actual: " + str(actual[0]) + " size: " + str(botout[1]) + " res: " + temp)
    if(botout[0] < float(actual[0]) and botout[0] > 1):
        #successful prediction
        successes += 1
        prev = True
        balance += (float(botout[0]) * botout[1]) - float(botout[1])
        prev_out = botout
    else:
        #failed prediction
        failures += 1
        balance -= botout[1]
        if(balance <= 0):
            break
        prev_out = botout
        prev = False

#save results
res = []
res.append("Four")
res.append("0 - " + str(test_cases))
res.append("$1000")
res.append("$" + str(balance))
res.append("$" + str(balance - 1000))
if(balance - 1000 > 0):
    res.append("[green]PASSED")
else:
    res.append("[red]FAILED")
result.append(res)
balance_history.append(balance_history_this)

#for bot five
#-------------------------------------------------------------------------------
csvfile.close()
csvfile = open("multipliers.csv", "r")
datareader = csv.reader(csvfile)

#full range
balance_history_this = []
test_cases = LINE_COUNT
successes = 0
failures = 0
balance = 500
topvalue = balance
prev_out = [0,0]
prev = True

for test_cases in track(range(test_cases), description="[green]Testing bot [bold]five[/bold] using [bold white]full range[/bold white]..."):
    balance_history_this.append(balance)
    #calculate bot [cutoff, size]
    botout = main.five(balance, prev, topvalue, prev_out)
    if(botout[1]>balance):
        botout[1] = balance
    #actual cutoff
    actual = next(datareader)
    #if cutoff is a success
    temp = ""
    #if(botout[0] < float(actual[0])):
    #    temp = str((float(botout[0]) * botout[1]) - float(botout[1]))
    #else:
    #    temp = "-" + str(botout[1])
    #print("bot: " + str(botout[0]) + " actual: " + str(actual[0]) + " size: " + str(botout[1]) + " res: " + temp)
    if(botout[0] < float(actual[0]) and botout[0] > 1):
        #successful prediction
        successes += 1
        prev = True
        balance += (float(botout[0]) * botout[1]) - float(botout[1])
        topvalue = balance
        prev_out = botout
    else:
        #failed prediction
        failures += 1
        balance -= botout[1]
        if(balance <= 0):
            break
        prev_out = botout
        prev = False

#save results
res = []
res.append("Five")
res.append("0 - " + str(test_cases))
res.append("$500")
res.append("$" + str(balance))
res.append("$" + str(balance - 500))
if(balance - 500 > 0):
    res.append("[green]PASSED")
else:
    res.append("[red]FAILED")
result.append(res)
balance_history.append(balance_history_this)


#overall
#-------------------------------------------------------------------------------

#print results
table = Table(title="Simulation Results")

table.add_column("Graph", justify="right")
table.add_column("Bot", style="blue", no_wrap=True)
table.add_column("Data", style="magenta")
table.add_column("Given")
table.add_column("Result")
table.add_column("Delta")
table.add_column("Verdict")

table.add_row("1", result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5])
table.add_row("2", result[1][0], result[1][1], result[1][2], result[1][3], result[1][4], result[1][5])
table.add_row("3", result[2][0], result[2][1], result[2][2], result[2][3], result[2][4], result[2][5])
table.add_row("4", result[3][0], result[3][1], result[3][2], result[3][3], result[3][4], result[3][5])
table.add_row("5", result[4][0], result[4][1], result[4][2], result[4][3], result[4][4], result[4][5])
#table.add_row("5", "One", "12-1000", "$500", "$600", "$100", "[green]PASSED")
table.add_row("6", "One", "12-1000", "$500", "$600", "$100", "[green]PASSED")

console = Console()
console.print(table)

#show graph
plt.plot(balance_history[0])
plt.plot(balance_history[1])
plt.plot(balance_history[2])
plt.plot(balance_history[3])
#plt.plot(balance_history[4])
plt.show()
