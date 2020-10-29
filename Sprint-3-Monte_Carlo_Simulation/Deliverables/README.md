# Sprint 3 &ndash; Deliverables

## Honor Code

“On my honor, I have not given, nor received, nor witnessed any unauthorized assistance on this work."

## List Your Team Members

TJ Donahue, Jay Jiranek

## Issue uploading the code

Every time I tried to upload the code as a program my internet would crash so I decided to put the code straight on this file. I apologize for the inconvenience.

## The Newton-Pepys Problem

<img src="https://cdn.aarp.net/content/dam/aarp/food/healthy-eating/2016/2016-05/1140-peeps-nation.imgcache.rev3aa6a5a0b7d521bbef63f0e833d97a8f.web.900.513.jpg" width="40%" />

Samuel Pepys (pronounced "Peeps") was a 17th Century British naval administrator, best known for the detailed diary he kept describing his life in the 1660's. In 1693 he
corresponded with Isaac Newton regarding a wager:

>Which of the following three propositions has the greatest chance of success?
>
>- Six fair dice are tossed independently and at least one six appears.
1-(5/6)^6 = 0.6651

>- Twelve fair dice are tossed independently and at least two sixes appear.
1 - ((5/6)^12 + (1/6)*(5/6)^11) = 0.61866

>- Eighteen fair dice are tossed independently and at least three sixes appear.
1 - ((5/6)^18 + (1/6)*(5/6)^17 + (1/6)^2 * (5/6)^16) = 0.59735

What is the answer to Pepys' question? Calculate your answer exactly using a discrete probability distribution, not a simulation model.

Tip: notice that the problem is phrased as *at least* **not** *exactly*.

## Geometric Urn

I have an urn that contains 100 balls. I know that some are black and some are red, but I don’t the numbers of each. Suppose I draw from the urn with replacement (putting each ball back in the urn, so that the number of balls remains the same) and write down the number of draws needed to get the first red ball. I then repeat this process several times and then use all of my results to calculate the expected number of draws needed to get the first red ball.

My experiment shows that the expected number of draws to get one red ball is 20. What are reasonable estimates for the number of black and red balls in the urn?

E[x] = 20 = 1/20 = 0.05 = 5%

Since there are 100 balls in the Urn and there is replacement after taking a ball out, my estimate is that there are 5-10 red balls and 90-95 black balls since there is replacement and you could be picking the same ball twice in a row. But from the probability I would say 5 red balls and 95 black balls.

## Dragon Dice

Hermione is back for another problem!

Hermione has settled into a nice routine with her fellow Slytherins. During the day, she eats meals in the Great Hall, reads about famous Dark Wizards in the library, and attends her classes. During the evening, she practices jinxing the Hufflepuffs, does her homework, and plays wizard games with her new friends, Daphne Greengrass and Tracey Davis.

One of their games is called Dragon's Dice. It's a simple carnival game, also known as Chuck-a-Luck.

Hermione picks a number 1-6 and rolls three fair dice. If her number comes up *k* = 1, 2, or 3 times, she wins *k* galleons. If it does not appear on any of the dice, she loses one galleon.

What is Hermione's expected outcome from playing Dragon's Dice? Solve this problem analytically.

P(0) = (3:0) * (1/6)^0 * (5/6)^3 = 0.5787
P(1) = (3:1) * (1/6)^1 * (5/6)^2 = 0.3472
P(2) = (3:2) * (1/6)^2 * (5/6)^1 = 0.0695
P(3) = (3:3) * (1/6)^3 * (5/6)^0 = 0.0046

((0 * 0.5787) + (1 * 0.3472) + (2 * 0.0695) + (3 * 0.0046)) / (0.5787 + 0.3472 + 0.0695 + 0.0046) = 0.5


## *Les Poissons*! *Les Poissons*! How I Love *les Poissons*!

<img src="https://vignette.wikia.nocookie.net/disney/images/4/4d/Tlmpe834.jpg/revision/latest?cb=20101108233151" width="40%" />

Recall that the derivation of the Poisson distribution is closely related to the binomial distribution when *n* is large and *p* is small. In this problem, you're going
to show the Poisson distribution is a good approximation for the binomial under these conditions.

- Write a Python function to simulate a binomial process with *n* = 1000 and *p* = .025. To do this, perform 1000 random coin flips where each flip comes up heads with probability .025. Record the number of heads that occur, which should be 25 on average.

- Repeat the above process 1000 times and plot the fraction of times each outcome occurs &ndash; for example, the fraction of binomial trials that resulted in 0 heads, the fraction of trials that results in exactly 1 head, and so forth. You should see a peak around the expected mean of 25 successes per trial.

- On the same plot, show the Poisson pmf with *λ* = 25. You should see that the two distributions are very similar.

I recommend using two line plots in two different styles for the two distributions.

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import math

from random import randint

def poisson(x, len):   
    output = []
    for i in range(1, x):
        temp1 = (((math.e) ** (-len)) * (len ** i))
        temp2 = temp1 / float(math.factorial(i))
        output.append(temp2)
    return output

def simulate():
    n = 1000
    heads = 0
    for i in range(n):
        temp = randint(1, 40)
        if temp == 1:
            heads += 1
    return heads

def main():
    n_iter = 1000 
    fraction_h_list = [0] * 1000
    for i in range(num_i):
        heads = simulate() 
        fraction_h_list[heads] = fraction_h_list[heads] + 1
    nList = [x / 1000 for x in fraction_h_list]
    poisson_list = poisson(50, 25)
    plt.figure()
    plt.plot(nList)
    plt.plot(poisson_list)
    plt.xlim(0, 50)
    plt.title('Probability of Heads Line Plot')
    plt.ylabel('Percentage of Success')
    plt.xlabel('Number of Trials')
    plt.savefig('Poisson Line Plot.pdf', bbox_inches='tight')

if __name__ == '__main__':
    main()


## The Ticket Problem

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b2/20th_Century_Limited_pulled_by_Commodore_Vanderbilt_1935.JPG" width="50%" />

One hundred passengers are waiting to board a train with one hundred seats. Every passenger has been assigned a seat, with the assigned seat numbers given on the passengers'
tickets. The passengers will board one at a time and each passenger must take his or her seat before the next one can board.

However, the first passenger has lost her ticket and can't remember her assigned seat number, so she just chooses a seat 1-100 at random and sits there. Each subsequent passenger will board in the following way:

- If his assigned seat is open, the passenger sits there.

- If his seat has already been taken, he chooses a random open seat instead.

Write a simulation program to determine the probability that passenger 100 gets to sit in her originally assigned seat.

Tips:

- As in the previous problem, use a `simulate` method to simulate one trial and return the result.

- Because the seats could be renumbered, you can assume, without loss of generality, that the first passenger was assigned in seat 1, the second passenger in seat 2, and so forth. This simplifies the simulation because you don't need to generate a complete set of seat assignments.

from random import randint
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def simulate():
  result = randint(1, 100)
  return result

def main():  
  travelers = 100
  all_seats = []
  next_seat = 0

  result = simulate()
  if result == 100:
    return 0
  else: 
    all_seats.append(result)

  for i in range(travelers - 1):
    next_seat = i+2
    if next_seat not in all_seats:
      all_seats.append(next_seat)
    else:
      next_seat = simulate()
      if next_seat == 100:
        return 0
      elif next_seat not in all_seats:
          all_seats.append(next_seat)
  return 1

if __name__ == '__main__':
  result_seats = []

    # use this to run more trials and collect data
  for i in range(1000):
    total_seats_result = main()
    result_seats.append(total_seats_result)

  plt.figure()
  plt.hist(results, 10)
  plt.title("Train Tickets Histogram")
  plt.xlabel("Success for last person to sit in seat 100)")
  plt.ylabel("Occurances")  
  plt.savefig('Train Tickets.pdf', )  

## The Martingale

Throughout history, numerous frauds, hucksters, and morons have claimed to devise "unbeatable" betting systems that allow gamblers to somehow overcome the house edge that's built into every game of chance.

Let's get one thing straight: **there's no such thing as an "unbeatable" betting system**. In fact, all betting strategies will produce, in the long run, the exact same expected outcome, which is determined by the house edge and not by the ordering or size of individual bets.

<img src="https://cdn5.vectorstock.com/i/1000x1000/72/59/american-roulette-wheel-vector-13367259.jpg" width="25%" />

Consider roulette. A typical American roulette wheel has numbers 0 to 36, plus a special "double zero" spot. Half of the numbers 1 to 36 are colored black and the other half are colored red, with the 0 and 00 locations colored green.

The basic bet in roulette is a color bet: the player bets that that the ball will land in a red-colored spot (or a black one, the two bets are symmetric). The bet pays even money, so if you bet $10 and win, you get $10. There are 38 total pockets on the wheel, of which 18 are red, 18 are black, and two are green, so the odds of winning the red or black bet are 18/38 ~ .4736.

In the long run, if you wager a total of $X on red/black in roulette, you should expect to wind up with about .47X in the bank at the end of your adventures. It doesn't matter if you play all $X in one bet, dribble it out over $1 bets, or make bets of variable size using some system: in the end, the house edge rules all.

If betting systems can't affect your long-run winnings, are they of any interest? The answer is a qualified yes. No betting system can modify your expected overall winnings, but they can affect how your winnings are distributed over a series of play sessions.

Consider the following betting strategy, which is one of the best known. It's usually called **the Martingale**, a name that emerged in 18th Century France, probably as a reference to a region called Martigues. In the Martingale strategy, the gambler doubles the bet after every loss.

- On the first round, bet $1. If you win, keep betting $1 on the next round.

- If you lose the first round, double the bet to $2. If you win this round, you'll have recovered the $1 you lost from the first round, plus one more dollar of profit.

- If you lose the second round, double the bet again to $4. If you win this round, you will have recovered all previous losses ($1 + $2) plus one additional dollar.

- Continue the same strategy, always doubling the bet after every loss and resetting to $1 after every win.

Therefore, as long as you eventually win one round, the Martingale guarantees that you'll recover all previous losses and leave the table with at least a tiny profit. This sounds unbeatable, **and it would be if you had an infinite bankroll**. In reality, the exponential growth of the bets guarantees that you'll eventually hit a string of losses that will bankrupt you.

Suppose that a gambler is playing roulette, always betting on black and using the Martingale system. She begins with $255, enough to cover seven losses. She ends her gambling session when either:

- She's played 100 spins.

- The size of the bet required by the Martingale becomes too large to cover. In this case, she ends the game and takes her remaining bankroll home.

Write a simulation program to evaluate the Martingale strategy. **Use matplotlib to create a histogram of the outcomes of 1000 simulated sessions of the process described above**. Your results should show that most sessions result in a small net gain for the player, but that these are balanced by catastrophic losses where she goes near bankruptcy.

Tips:

- Try playing a few sessions before you begin coding. Make sure you understand the process before thinking about how to implement it.

- As before, use a `simulate` method that plays one complete session, then returns that amount remaining in the gambler's bankroll at the end. Collect all of your results into a list, then use matplotlib's `hist` function to create the plot.

Remember to update the bankroll after each win or loss. Wins become part of the total bankroll and can be used for future bets.

from random import randint
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def attempt(bet):
    money = 255
    win = True

    rand_num = randint(1, 38)
    if rand_num <= 18:
        money = money + bet
    else:
        money = money - bet
        win = False
    return win
    
def plot(data):
    plt.figure()
    plt.hist(data, 50)
    plt.title("Martingale Histogram")
    plt.xlabel("Money in Pocket")
    plt.ylabel("Count")
    plt.savefig("Martingale.pdf", bbox_inches='tight')

def main():
    data = []
    money = 255
    
    for i in range(1000):
        bet = 1
        games = 0
        while money > bet and games < 100:
            outcome = attempt(bet)
            if outcome == True:
                bet = 1
            else:
                bet = bet * 2
            games+=1
            
        data.append(money)
        money = 255
    plot(data)
    
if __name__ == '__main__':
    main()
