# coin-machine
coin-machine program, by Usman Ahmad

Executions on how to run cmain.py in Anaconda Command prompt (tested in Python 3.8):

First, in Anaconda Command Prompt, go to the "coin-machine" folder

Now, you have 3 ways of computing the odd, even or all ways of summing £ or $
denominations to the input target amount expressed as e.g. £{pounds}-{pence}

<br>
<br>

1
-----------------------------------------------------------------------------------
--- Run Main Coin-Machine solutions and interpreter to run for specific amounts ---
-----------------------------------------------------------------------------------
To compute the number of odd ways to sum to £0-50, £2-, £10-, £100-
RUN: python cmain.py

After calculating the number of ways for these amounts, an interpreter will be

opened allowing the following types of executions:

e.g. <cmain> £123-45            # calculate odd number of ways

e.g. <cmain> £123-45 odd        # calculate odd number of ways

e.g. <cmain> £123-45 even       # calculate even number of ways

e.g. <cmain> £123-45 all        # calculate all number of ways

e.g. <cmain> help               # show this help screen

e.g. <cmain> quit               # exit the program

<br>
<br>

2
---------------------------------------------------
--- Run specific amounts directly from cmain.py ---
---------------------------------------------------
Generally, to compute the number of odd ways to sum £{pounds}-{pence}

RUN: python cmain.py £{pounds}-{pence}

e.g. python cmain.py £123-45

e.g. python cmain.py £123-

e.g. python cmain.py £123-45 odd

e.g. python cmain.py £123-45 even

e.g. python cmain.py £123-45 all

e.g. python cmain.py £1000-

<br>
<br>

3
-------------------------------------------------------------
--- Run specific amounts directly from Python interpreter ---
-------------------------------------------------------------
In Python 3.8 interpreter, the main function to run is called dispense_odd_count
residing in src/coin_machine.py:

From coin-machine folder, run Anaconda Python 3.8

> from src.coin_machine import dispense_odd_count
> dispense_odd_count("£1-00")
> 
>> 2281
 
> dispense_odd_count("£100-00")
>>566936652323775

> dispense_odd_count("$100-00")
>>69973044750

<br>


NOTEs:
- for "£1000-" elapsed time is ~15 secs on a 32GB RAM i7 2.60Ghz SSD machine
- all upper and lower case strings are handled on the "odd", "even", "all" params
- US Dollar denominations are handled via $ symbol e.g. $123-45 (see denominations.py)
