import random

'''
# IDEAS
- Check for word similarity. Nothing too similar
'''


# Adjectives-ish
behaviours = [
    'bold', 'brave', 'clumsy', 'forgetful', 'rampant'
]
colours = [
    'black', 'blue', 'brown', 'green', 'indigo', 'jade', 'orange',
    'pink', 'purple', 'red', 'violet', 'yellow', 'crimson', 'magenta',
    'silver', 'chartreuse']
emotions = [
    'angry', 'delighted', 'manic', 'sad'
]
flavours = [
    'spearmint'
]
materials = [
    'concrete', 'cotton', 'diamond', 'emerald', 'glass', 'granite', 'grassy',
    'ivory', 'obsidian', 'sandy', 'sapphire', 'satin', 'silk', 'snowy', 'steel',
    'stone'
]
sensations = [
    'blind', 'cold', 'deaf', 'hungry', 'numb', 'sleepy', 'thirsty'
]
seasons = [
    'autumn', 'spring', 'summer', 'winter'
]
sounds = [
    'noisy', 'silent'
]
sizes = [
    'bonsai', 'double', 'epic', 'giant', 'giga', 'hyper', 'long', 'maximum', 'mega',
    'miniature', 'short', 'ultra'
]
times = [
    'dawn', 'day', 'dusk', 'evening', 'midday', 'midnight', 'morning', 'night',
    'noon', 'sunrise', 'sunset'
]
adj_misc = [
    'closed', 'common', 'millenium', 'misty', 'open', 'quantum', 'rare',
    'secret', 'space', 'winding', 'windy'
]

adjective_groups = [
    behaviours, colours, emotions, flavours, materials, sensations, seasons,
    sounds, sizes, times, adj_misc
]

adjectives = []
for group in adjective_groups:
    adjectives += group



# Nouns
animals = [
    'badger', 'boar', 'bunny', 'cat', 'dolphin', 'donkey', 'dragon', 'duck',
    'falcon', 'ferret', 'fox', 'fox', 'gopher', 'hawk', 'hawkmoth', 'jay',
    'lizard', 'minnow', 'monkey', 'otter', 'panda', 'parrot', 'parrot',
    'peacock', 'platypus', 'poodle', 'possum', 'rabbit', 'rhino', 'setter',
    'shark', 'slug', 'tiger', 'unicorn', 'vixen'
]
architecture = [
    'arch', 'bank', 'ceiling', 'column', 'dome', 'door', 'doorway', 'elevator',
    'esculator', 'gate', 'gateway', 'tower', 'verge'
]
body_parts = [
    'beard', 'cheeks', 'cloaca', 'eye', 'fist', 'foot', 'hand', 'heart', 'mouth',
    'neck'
]
buildings = [
    'church', 'clock', 'firehouse', 'graveyard', 'inn', 'lighthouse',
    'school', 'tavern', 'temple', 'windmill'
]
clothing = [
    'garter', 'jacket', 'shoes', 'top', 'veil'
]
coding = [
    'array', 'function', 'integer', 'loop', 'macro'
]
collectives = [
    'army', 'battlion', 'clowder', 'cluster', 'colony', 'congregation',
    'flock', 'herd', 'majority', 'minority', 'pack', 'parliament', 'swarm',
    'tribe', 'troop'
]
geography = [
    'cliff', 'mountain', 'lagoon','pool', 'river', 'rock', 'sea', 'stream'
]
jobs = [
    'archer', 'astronaut', 'beekeeper', 'bishop', 'diver', 'driver', 'envoy',
    'joker', 'king', 'knight', 'prince', 'queen', 'ranger', 'senator', 'warden',
    'warrior', 'wizard'
]
names = [
    'Dean', 'Hebe', 'Herald', 'Jack', 'Janet', 'Maria', 'Pippin', 'Thor', 'Vesta',
    'William', 'Zeus'
]
plants = [
    'apple', 'bamboo', 'barley', 'birch', 'blossom', 'branch', 'bush', 'cabbage',
    'cedar', 'crop', 'flax', 'garland', 'garlic', 'ginger', 'grass', 'lemon',
    'lily', 'mahagony', 'oak', 'orchid', 'palm', 'rose', 'rosette', 'thistle',
    'tree', 'tulip', 'walnut', 'willow'
]
religion = [
    'angel', 'devil', 'satan'
]
sailing = [
    'anchor', 'boye', 'gallion', 'yacht'
]
space = [
    'asteroid', 'comet', 'moon', 'planet', 'satelite', 'star', 'station', 'sun'
]
titles = [
    'duchess', 'duke', 'knave', 'provost'
]
vehicles = [
    'bus', 'rocket', 'tank', 'wagon'
]
weapons = [
    'arrow', 'axe', 'bow', 'club', 'crossbow', 'halbard', 'mace', 'pike',
    'rapier', 'shield', 'spear', 'sword', 'trident'
]
weather = [
    'aurora', 'sky'
]
noun_misc = [
    'banner', 'bottle', 'bracket', 'brick', 'carpet', 'cheese', 'cocktail',
    'corkscrew', 'drover', 'duster', 'flag', 'flannel', 'flash', 'garter',
    'hammer', 'hammock', 'harvest', 'light', 'passion', 'pound', 'putter',
    'riband', 'salad', 'shadow', 'sparkler', 'streak', 'study', 'sugar',
    'ticket', 'toffee', 'water'
]

noun_groups = [
    animals, architecture, body_parts, coding, collectives, geography, jobs,
    names, plants, sailing, space, titles, vehicles, weapons, weather, noun_misc
]
nouns = []
for group in noun_groups:
    nouns += group


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

