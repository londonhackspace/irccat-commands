#!/usr/bin/python3

# Untrue facts about the hackspace

import random

facts = [
         'The first hackspace tour was given in 1804 by Sir Ranolph Stainsbury, a job which has remained in the family line with current tours being given by his great great great great grandson.',
         'London Hackspace was founded in 1936 by Geoff Hackspace, MP.',
         'Hackspaces do not have a liquid state at normal atmospheric pressure.',
         'There are 6(!) geocaches hidden in the current space.',
         'Noisebridge was the first hackspace to 3d print a living horse.',
         'In 1776 hackspace membership was given to people not quite insane enough to be sent to mental asylums. It is believed to have been the world\'s first community service sentence.',
         'The average hackspace carpet contains 4 tonnes of stripped wire insulation.',
         'During the Second World War, London Hackspace made tea for American servicemen.',
         'London Hackspace is twinned with Flurghoefen, East Germany.',
         'The paint storage area is built on the remains of London\'s first tube station - only the original gas piping remains.',
         'Due to Euler\'s law, laser cutters are unable to cut pentagons.',
         'The Queen is an honorary member of London Hackspace, but has only visited twice.',
         'The server hosting this script, Babbage, is one of the original 5 machines to power the internet.',
         'Alan Turing originally planned to build the Bombe at London Hackspace, but beards got in the way.',
         'Although they appear stationary, hackspaces drift westwards by up to 1ft/year.',
         '"Hackspace" is the only English word to have been removed from the official Scrabble dictionary due to a DMCA claim.',
         'In Hoover, Alamaba, a fight over woodworking tools led to the founding of a Church of Making in 1822. It lasted 7 years, but was inspiration for Make magazine when it relaunched.',
         'jontyw has posted every possible URL up to 1024 characters on the channel, so he gets alerted automatically to any links',
         'The term NoSQL was invented in the first London Hackspace after a founding member lost a bet involving large quantities of beer',
         'It is still a law on the English Law books that you can kill a Welshman with a bow and arrow within the bounds of the Hackspace yard, but you have to be on fire. This is also the only exception to Rule 0',
         'All swans in the Hackspace officially belong to Jonty',
]

print (random.choice(facts))


