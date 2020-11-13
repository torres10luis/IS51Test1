""" 
Structured-English branch

Starting with this problem we can see that we have 2 salary options which consists of 10 days worked. as it explains with option 1 is given a $100 dollars per day for the 10 days of work. As for the second option we are given with a choice of receiving $1 the first day and then it doubles until you reach the 10th day of work. With this program we will be able to determine with of these options is better and we will also be calculating in 2 different functions to determine which option is better at the 10th day.

if option 1 is better it will print in the console that option 1 is better.
if option 2 is better it will print in the console that option 2 is better.
but if both options pay the same amount of money in the 10th day it will print out in the console that both option 1 and option 2 will pay the same amount of money at the 10th day

function one is simpler because it will consist of $100 *  10 which is what is said in the description.
function two will be a more complex because it will have to loop 10 times to represent the 10 days in total and doubling the amount each day till end of 10th day then it will sum everything up


"""

""" 
    for option 1 it will be: $100 * 10 (days)
        return 100 * 10

    for option 2 it will be:
        amount = 1 
        list1 = []
        then loop the 10 times for the days
            add the amount to the list1
            amount = 2
        sum = the sum of all items in the loop
        return sum

    main:
    var1 = option1
    var2 = option2

    if var1= var2
        options 1 and 2 will pay the same at the 10th day
    if var 1 < var2 
        the option 2 will pay more than option1
    else: 
        option1 pays more

main
    
"""

def option1():
    return 100 * 10

def option2():

    amount = 1 
    list1 = []

    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total

def main():
    answer = " "
    
    var1 = option1()
    var2 = option2()

    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same"
    elif var1 < var2:
        answer = "Option 2 is better"
    else:
        answer = "Option 1 is better"
    print(answer)

main()
    
