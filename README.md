# About
Sho-simulator, simulates the tradition of playing sho when you visit Lhakhangs. You can choose the number of times you want to simulate the sho
and it will give you a result of the number of sho zangmi and sho mazangmi. 

The numbers for sho zangmi and mazangmi are from Dechenphug Lhakhang. Personally requested from the koenyer, the lucky set of numbers are:
{3,5,7,8,9,11,13,14,17,18}. So yes this is actually a legit source, go ask the koenyer if you dont believe me.

The program simulates three dice rolls for three times until you get a sho zangmi. And if after even three tries you still end up
getting a the unlucky set of numbers then you officially get a sho mazangmi. 

For the simulation users can run how many ever your computer can handle but it is interesting to note that as the number of simulation increases, the number of sho zangmi and mazagnmi move closer to the expected value(LLN).

# Installation and Running
Clone the repo or you can just copy and paste the run.py code.
To run the code just navigate to the directory that has the run.py file and then:
```python
python3 run.py
```
# To Dos
- [x] Code the Simulation
- [ ] Make python graphics for the dice roll
- [ ] Let users be able to phuesheling nyendar
- [ ] Write out the math in a proper latex document
# The Math

The math in this is relatively simple and even though I'm pretty shit at math I think it was relatively easy for me to grasp the concepts for this.

The Math done below is to find the expected value for each roll.

So to start off: 
1. The number of possiblities when you roll 3 dice is:
    - 6 * 6 * 6 = 216
    - this is because each die has 6 different possible outcomes 1-6 and each of them is independent of each other. So 216 actually represent the number of ways you can actually arrange them. not too sure.
1. As mentioned above, set of good outcomes:
    - {3,5,7,8,9,11,13,14,17,18}
1. And Now the ways to roll these good outcomes (I wont bother explaining this here's a [link](https://www.thoughtco.com/probabilities-for-rolling-three-dice-3126558#:~:text=Just%20as%20one%20die%20has,sums%20from%20rolling%20several%20dice.))
    - Num Ways to roll a 3 = 1
    - Num Ways to roll a 5 = 6
    - Num Ways to roll a 7 = 15
    - Num Ways to roll a 8 = 21
    - Num Ways to roll a 9 = 25
    - Num Ways to roll a 11 = 27
    - Num Ways to roll a 13 = 21
    - Num Ways to roll a 14 = 15
    - Num Ways to roll a 17 = 3
    - Num Ways to roll a 18 = 1
    - Total Ways to roll a sho zangmi = 135
    - Probability of rolling a sho zangmi on the first try = 135/216 - 0.625
1. The probability of you actually getting a sho mazangmi i.e. probability of you getting an unlucky number three times in a row:
    - Num ways to roll an unlucky number: 216-135 = 81
    - probability of getting a sho mazangmi on the first try = 81/216 = 0.375
    - since we only consider that the Shos' show an ill fortune only when we roll a sho mazangmi three times in a row. So lets find out the probability of rolling a sho mazangmi three times in a row:
        - 0.375 * 0.375 * 0.375 = 0.05273
    - now since we have the probability of getting a sho mazangmi it is easy to find the probability of getting a sho zangmi:
        - 1 - 0.05273 = 0.94727
1. So to sum up the probability of you getting a sho zangmi is 0.94727 and this is mainly because you get three chances. The probability of getting a sho mazangmi is: 0.05273. 
# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# Authors and Acknowledgement
1. Karma Z. Yoezer
1. Jigme T. Namgyal
