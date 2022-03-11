def bot(balance, prev_outcome,prev_out_arr, remainder):
    flag = False
    #Every 3000 set the money aside
    if(balance >= 5000):
        flag = True
    #If we win
    if(prev_outcome):
        betsize = balance / 200000
        return [2.0,betsize, flag]
    #If we loose
    else:
        if((prev_out_arr[1] * 2.0) <= remainder):
            return [2.0,prev_out_arr[1] * 2, flag]
        else:
            if(remainder < balance / 100000):
                return [2.0,balance / 100000, flag]
            return [2.0, remainder, flag]

def two(balance, prev_outcome,prev_out_arr, remainder):
    if((remainder * 0.5) <= 0.04):
        return [1.3,0.04]
    if(prev_outcome):
        return [1.3,remainder * 0.5]
    else:
        return [1.3, 0.04]

def three(balance, prev_outcome,prev_out_arr,losstreak):
    if(prev_outcome):
        #betsize = balance / 2100000
        return [2.0,0.01]
    else:
        if((prev_out_arr[1] * 2.0) <= balance):
            return [2.0,prev_out_arr[1] * 2]
        else:
            return [2.0, balance]

def four(balance, prev_outcome, prev_out_arr):
    #If we win
    if(prev_outcome):
        betsize = 0.01
        #check bet size
        if(balance > 2000):
            betsize = 0.02
        if(balance > 3000):
            betsize = 0.03
        if(balance > 4000):
            betsize = 0.04
        if(balance > 5000):
            betsize = 0.05
        if(balance > 6000):
            betsize = 0.06
        return [2.0,betsize]
    #If we loose
    else:
        if((prev_out_arr[1] * 2.0) <= balance):
            return [2.0,prev_out_arr[1] * 2]
        else:
            return [2.0, balance]

def five(balance, prev_outcome, topvalue, prev_out_arr):
    #If we win
    if(prev_outcome):
        betsize = balance / 100000
        return [2.0,betsize]
    #If we loose
    else:
        if((prev_out_arr[1] * 2.0) <= balance):
            return [2.0,prev_out_arr[1] * 2]
        else:
            return [2.0, balance]
