#!/usr/bin/env python
#@+leo-ver=5-thin
#@+node:peckj.20140519080415.3928: * @file culture.py
#@@first
#@@language python

#@+<< imports >>
#@+node:peckj.20140519080415.3929: ** << imports >>
import random
import inflect
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140519080415.3930: ** << declarations >>
GAMETURNS = 50

STARTING_POPULATIONS = 10
STARTING_CITIES = 1

p = inflect.engine()
#@-<< declarations >>

#@+others
#@+node:peckj.20140519080415.3933: ** class Player
class Player:
  def __init__(self, name, populations=STARTING_POPULATIONS, cities=STARTING_CITIES):
    self.name = name
    self.populations = populations
    self.populations_distributions = {'agriculture': populations,
                                      'trade': 0,
                                      'labor': 0,
                                      'scholars': 0,
                                      'armies': 0,
                                      'navies': 0}
    self.leaders = {'ruler': 0,
                    'general': 0,
                    'thinker': 0,
                    'builder': 0,
                    'religious': 0,
                    'diplomat': 0}            
    self.cities = cities
    self.natural_resources = {'grain': 0,
                              'fish': 0,
                              'iron': 0,
                              'horses': 0,
                              'precious metals': 0,
                              'fruits': 0,
                              'livestock': 0,
                              'wood': 0} # stub
    self.manufactured_resources = {} # stub
    self.advances = []
                              
#@+node:peckj.20140519080415.3932: ** roll
def roll(sides=6, n=1):
  total = 0
  for i in range(n):
    total += random.randint(1,sides)
  return total
#@+node:peckj.20140519080415.3931: ** main
def main():
  ## make player(s)
  players = [Player(name="Squishy")]
  ## run game
  gameloop(players)
#@+node:peckj.20150302155009.1: *3* gameloop
def gameloop(players):
  for turn in range(1, GAMETURNS+1):
    for player in players:
      print "Turn %s, Player %s" % (turn, player.name)
      # population
      population_phase(player)
      # resource
      # distribution
      # leader
      # harvest
      # disaster
      # upkeep
      ## war
      ## trade
      # build
      # research
      # income
#@+node:peckj.20150302155009.2: *4* population_phase
def population_phase(player):
  # Population growth:
  # by default, it's 1d6-2 min 0
  # affected by number of Religious leaders (+1d6 each)
  # affected by Monotheism (+1, so 1d6 - 1 min 0)
  
  mod = -2
  if 'monotheism' in player.advances: mod = -1
  pop_growth = max(0, roll() + mod)
  for i in range(player.leaders['religious']):
    pop_growth += roll()
  player.populations += pop_growth
  print "You've gained %s %s this turn. New total: %s" % (pop_growth, p.plural('population', pop_growth), player.populations)
#@-others

if __name__=='__main__':
  main()

#@-leo
