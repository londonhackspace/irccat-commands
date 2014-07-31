#!/usr/bin/python

import random

colours = ['pink', 'blue', 'red', 'crimson', 'magenta', 'silver', 'chartreuse', 'violet']
behaviours = ['clumsy', 'rampant', 'forgetful', 'bold', 'brave']
emotions = ['angry', 'sad', 'manic', 'delighted']
sensations = ['thirsty', 'hungry', 'sleepy', 'cold', 'blind', 'deaf', 'numb']
seasons = ['spring', 'summer', 'winter', 'autumn']
times = ['sunrise', 'sunset', 'noon', 'midnight', 'midday', 'dusk', 'morning', 'evening', 'night', 'day', 'dawn']
sizes = ['long', 'short', 'double', 'miniature', 'giant', 'maximum', 'bonsai', 'ultra', 'giga', 'mega', 'hyper']
flavours = ['spearmint']
sounds = ['silent', 'noisy']
misc = ['millennium', 'secret', 'space', 'misty', 'windy', 'winding', 'rare', 'common', 'epic', 'quantum']
materials = ['glass', 'concrete', 'grassy', 'snowy', 'silk', 'cotton', 'obsidian', 'rocky', 'sandy']

adjectives = colours + behaviours + emotions + sensations + seasons + times + sizes + flavours + sounds + misc + materials


animals = ['gopher', 'shark', 'donkey', 'unicorn', 'platypus', 'badger', 'dragon', 'hawkmoth', 'rhino', 'rabbit', 'falcon', 'otter', 'ferret', 'fox', 'parrot', 'vixen', 'panda', 'monkey']
space = ['moon', 'star', 'satellite', 'station', 'sun', 'planet', 'comet', 'asteroid']
jobs = ['beekeeper', 'driver', 'senator', 'astronaut', 'warden']
currency = ['pound']
coding = ['integer', 'array', 'loop', 'function', 'macro']
geography = ['cliff', 'river', 'mountain', 'stream', 'pool']
vehicles = ['bus', 'wagon', 'rocket', 'tank', 'galleon', 'yacht']
weapons = ['shield', 'spear', 'sword', 'pike', 'halbard', 'axe', 'trident', 'mace', 'bow', 'crossbow']
plants = ['bush', 'tree', 'branch', 'lily', 'willow', 'birch', 'mahogany']
body_parts = ['fist', 'hand', 'eye', 'cloaca', 'mouth', 'foot', 'heart']
titles = ['duke', 'duchess', 'provost', 'knave']
buildings = ['windmill', 'clock tower', 'graveyard', 'tavern', 'inn', 'church', 'firehouse', 'lighthouse', 'school']
architecture = ['ceiling', 'dome', 'elevator', 'door', 'gateway', 'escalator', 'verge', 'column', 'arch', 'bank']
collectives = ['majority', 'minority', 'parliament', 'flock', 'herd', 'clowder', 'pack', 'congregation', 'swarm', 'colony', 'army', 'battalion', 'cluster', 'tribe', 'troop']
weather = ['sun', 'sky', 'aurora']

noun_groups = [animals, space, jobs, currency, coding, geography, vehicles, weapons, plants, body_parts, titles, buildings, architecture, collectives, weather]
nouns = []
for i in noun_groups:
    nouns += i


def weighted_choice(items):
    '''
    Like random.choice but the items have weights to decide which is 
    more likely to be choosen.

    Format: List of tuples. Tuple should have item first, then its weight i.e. [(item, weight), (item, weight)]
    '''
    total = sum([weight for item, weight in items])
    threshold = random.uniform(0, total)

    for item, weight in items:
        # Lower the threshold each time through the loop
        threshold -= weight

        # If threshold met then item picked
        if threshold <= 0:
            return item
    assert False, "Unreachable code point"
    

def pick_two_nouns(noun_groups):
    # Pick two random noun groups
    noun_group1 = random.choice(noun_groups)
    noun_group2 = random.choice(noun_groups)

    # Make sure the groups aren't the same
    while noun_group1 == noun_group2:
        noun_group2 = random.choice(noun_groups)

    # Pick random nouns from the two groups
    noun1 = random.choice(noun_group1)
    noun2 = random.choice(noun_group2)
    return [noun1, noun2]


def pick_words(noun_groups, adjectives):
    '''
    Return a list of some chosen terms from the nouns and adjectives.
    '''
    
    # Certain options should be more likely than others i.e adj noun most common
    options = [('adj double noun', 1), ('double noun', 3), ('adjective noun', 6)]
    option = weighted_choice(options)

    if option == 'double noun':
        return pick_two_nouns(noun_groups)
    if option == 'adj double noun':
        adj = random.choice(adjectives)
        nouns = pick_two_nouns(noun_groups)
        return [adj] + nouns

    adj = random.choice(adjectives)
    noun_group = random.choice(noun_groups)
    noun = random.choice(noun_group)
    return [adj, noun]


terms = pick_words(noun_groups, adjectives)

name = ' '.join(terms).upper()
phrase = "Your project name is {0}".format(name)
print phrase
