#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20140519080415.3928: * @file culture.py
#@@first
#@@language python

#@+<< imports >>
#@+node:peckj.20140519080415.3929: ** << imports >>
import random
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140519080415.3930: ** << declarations >>
GAMETURNS = 50

STARTING_POPULATIONS = 10
STARTING_CITIES = 1
#@-<< declarations >>

#@+others
#@+node:peckj.20140519080415.3933: ** class Player
class Player:
  def __init__(self, name, population=STARTING_POPULATIONS, cities=STARTING_CITIES):
    self.name = name
    self.populations = populations
    self.cities = cities
#@+node:peckj.20140519080415.3932: ** roll
def roll(sides=6, n=1):
  total = 0
  for i in range(n):
    total += random.randint(1,sides)
  return total
#@+node:peckj.20140519080415.3931: ** main
def main():
  ## make player(s)
  players = [Player()]
  ## run game
  gameloop(players)
#@-others

if __name__=='__main__':
  main()

#@-leo
