#!/usr/bin/python

""" Repeats either individual or all rules to the user """
# SamLR 18-05 feel free to do what you like with this

from sys import argv
from time import sleep
import socket

max_hackspace_rule = 20

rules = {
# London Hackspace
  '0': "Do not be on fire",
  '-0': 'see Rule 0',
  'abs(0)': "Do not be freeze dried",

  '1': "Work safely and stop others working unsafely",
  '2': "Don't defeat/hack safety features",
  '3': "Check the wiki. If in doubt: ask",

  '4': "If something is broken, fix it; don't complain. If you can't, tell the trustees",
  '5': "If you're doing something major, ask the mailing list first",

  '6': "Do not treat the Hackspace like your home. Sleeping is forbidden",

  '7': "Members may store things in the space but it must be in a box; one box per member",
  '8': "Large items must be cleared with the list first and labelled",

  '9': "Please don't donate stuff without advance notification on the ML",
  '10': "If you don't want something hacked label it as such",
  '11': "If something looks valuable check before hacking",
  '12': "Don't take tools without asking the mailing list first",

  '13': "Workareas must be clean before you leave, tools must be returned",
  '14': "Put dirty crockery in the dishwasher before you leave", 
  '15': "Items left in workareas are fair game",
  '16': "Made a mess? Clean it up",
  '17': "Don't bring bikes in unless you are working on them, they take up too much room",

  '18': "If an item needs to be thrown put it in the 3 week box",
  '19': "Large items (that won't fit in the box) should be checked with the list before disposal",
  '20': "Check with the list before throwing useful items",

# Russ
  'russ': "never ascribe to malice that which can otherwise be explained by someone tidying stuff up",
  'russ2': "every social problem in the hackspace inevitably devolves into people suggesting an over-engineered, over-complicated technological solution",

# Red Dwarf:
  '003': "By joining Star Corps each individual tacitly consents to give up his inalienable rights "
         "to life, liberty and adequate toilet facilities", # Red Dwarf 1996 Log Book
  '005': "Gross negligence, leading to the endangerment of personnel, is discouraged", # "Queeg"
  '112': "A living crew member always out-ranks a mechanical", # Season V/"White Hole"
  '142': "In a hostage demand situation, a hologrammatic personality is entirely expendable",
         # Season V
  '147': "Crew members are expressly forbidden from leaving their vessel except on permission of "
         "a permit. Permits can only be issued by the Chief Navigation Officer, who is expressly "
         "forbidden from issuing them except on production of a permit",
         # "Ouroboros"/Red Dwarf 1996 Log Book
  '195': "In an emergency power situation, a hologrammatic crewmember must lay down his life in "
         "order that the living crew-members might survive", # "White Hole"
  '271': "No chance, you metal bastard", # "White Hole"
  '312': "Crew members in quarantine must be provided with minimum leisure facilities",
         # "Quarantine"
  '349': "Any officer found to have been slaughtered and replaced by a shape-changing chameleonic "
         "life form shall forfeit all pension rights", # Red Dwarf 1996 Log Book
  '497': "When a crewmember has run out of credits, food may not be supplied until the balance is "
         "restored", # Queeg
  '592': "In an emergency situation involving two or more officers of equal rank, seniority will "
         "be given to whichever officer can programme a VCR", # PBS Ident/Red Dwarf 1996 Log Book
  '595': "Any member of the crew who has been to a zone identified as rife with disease, or "
         "Camden, must be quarantined", # "Quarantine"
  '596': "Crew files are for the eyes of the Captain only", # "Back to Earth (Part Two)"
  '597': "One berth per registered crew member", # "Quarantine"
  '699': "Crew members may demand a rescreening after five days in quarantine showing no ill "
         "effect", # "Quarantine"
  '723': "Terraformers are expressly forbidden from recreating Swindon",
         # PBS Ident/Red Dwarf 1996 Log Book
  '997': "Work done by an officer's doppleganger in a parallel universe cannot be claimed as "
         "overtime", # Red Dwarf 1996 Log Book
  '1694': "During temporal disturbances, no questions shall be raised about any crew member whose "
          "timesheet shows him or her clocking off 187 years before he clocked on",
          # Red Dwarf 1996 Log Book
  '1742': "No member of the Corps should ever report for active duty in a ginger toupee",
          # "Psirens"/Red Dwarf 1996 Log Book
  '1743': "No registered vessel should attempt to traverse an asteroid belt without deflectors",
          # "Psirens"
  '5796': "No officer above the rank of mess sergeant is permitted to go into combat with pierced "
          "nipples", # "Psirens"
  '5797': "A crew-member is not be allowed back aboard if he may, in fact, be a brain-sucking "
          "psychotic temporal lobe slurper", # "Psirens"
  '7214': "To preserve morale during long-haul missions, all male officers above the rank of First "
          "Technician must, during panto season, be ready to put on a dress and a pair of false "
          "breasts", # Red Dwarf 1996 Log Book
  '7713': "The ship's log must be kept up to date at all times with current service records, "
          "complete mission data and a comprehensive and accurate list of all crew birthdays so "
          "that senior officers may avoid bitter and embarrassing silences when meeting in the "
          "corridor with subordinates who have not received a card", # Red Dwarf 1996 Log Book
  '34124': 'No officer with false teeth should attempt oral sex in zero gravity',
           # "Legion"/Red Dwarf 1996 Log Book
  '43872': "Suntans will be worn during off-duty hours only", # Red Dwarf 1996 Log Book
  '68250': "In case of rampant sin, Kapparot shall be performed in full", # "Kapparot"/"Emohawk"
  '98247': "No officer should be left behind on an inhabited planet unless he is missing two or "
           "more limbs", # Advertising for the 2009 Red Dwarf special episodes
  '196156': "Any officer caught sniffing the saddle of the exercise bicycle in the women's gym "
            "will be discharged without trial", # "Rimmerworld"/Red Dwarf 1996 Log Book
  '1947945': "A mechanoid may issue orders to human crew members if the lives of said crew members "
             "are directly or indirectly under threat from a hitherto unperceived source and there "
             "is inadequate time to explain the precise nature of the enormous and most imminent "
             "death threat", # Original script for "Back to Reality"
  '572 436 8217968B': "At all times show your allegiance to Red Dwarf in the US by picking up your "
      "phone and calling your local public television station with your pledge", # PBS ident
  '39436175880932/B': "All nations attending the conference are only allocated one car parking "
      "space", # "Gunmen of the Apocalypse"
  '39436175880932/C': "POW's have a right to non-violent constraint", # "Gunmen of the Apocalypse"

# Not quite Red Dwarf
  '426': 'You must not eat kippers while riding a donkey saw',

# Star Trek
  #'33': "It never hurts to suck up to the boss",
  '45': "Expand or die",
  '208': "Sometimes the only thing more dangerous than a question is an answer",
  '285': "No good deed ever goes unpunished",

# Dr Who
  '27': "Never knowingly be serious",
  '408': "You should always waste time when you don't have any",

# Monty Python
  'four': "I don't want to catch anyone *not* drinking in their room after lights out",
  'six': "There is no rule six",

# Urban Dictionary
  #'21': "All numbers pertaining to a rule are completely and utterly random",
  '1138': "No matter how dumb something in Star Wars or its accompanying expanded universe is, there is ALWAYS something dumber.",

# 4chan/Rules of the Internet
  '-1': "/b/ is not your friend",
  '32': "Pics or it didn't happen",
  '33': "Lurk moar - it's never enough",
  '34': "If it exists, there is porn of it. No exceptions",
  '35': "If no porn is found of it, it will be made",
  '42': "Always bring your towel. No exceptions",
  '71': "The Internet is SERIOUS FUCKING BUSINESS",
  '85': "If it exists, there is a pony of it. No exceptions",

# Hercules
  '38': "Keep them up there",
  '95': "Concentrate",
  '96': "Aim",

# Magic: The Gathering
  '502.9d': "Ignore this rule",

# Automata
  #'30': "http://www.wolframalpha.com/input/?i=rule+30",
  '90': "http://www.wolframalpha.com/input/?i=rule+90",
  '110': "http://www.wolframalpha.com/input/?i=rule+110",
  '184': "http://www.wolframalpha.com/input/?i=rule+184",

# Evil Overlord List
  '22': "No matter how tempted I am with the prospect of unlimited power, I will not consume any "
        "energy field bigger than my head",
  #'27': "I will never build only one of anything important. All important systems will have "
  #      "redundant control panels and power supplies. For the same reason I will always carry "
  #      "at least two fully loaded weapons at all times",
  '40': "I will be neither chivalrous nor sporting. If I have an unstoppable superweapon, I will "
        "use it as early and as often as possible instead of keeping it in reserve",
  '46': 'If an advisor says to me "My liege, he is but one man. What can one man possibly do?", '
        'I will reply "This", and kill the advisor',
  '50': "My main computers will have their own special operating system that will be completely "
        "incompatible with standard IBM and Macintosh powerbooks",
  '59': "I will never build a sentient computer smarter than I am",
  '67': "No matter how many shorts we have in the system, my guards will be instructed to treat "
        "every surveillance camera malfunction as a full-scale emergency",
  #'96': "My door mechanisms will be designed so that blasting the control panel on the outside "
  #    "seals the door and blasting the control panel on the inside opens the door, not vice versa",
  '99': "Any data file of crucial importance will be padded to 1.45MB in size",

# Seventy Maxims of Maximally Effective Mercenaries (http://www.schlockmercenary.com/)
  '21': "Give a man a fish, feed him for a day. Take his fish away and tell him he's lucky just "
        "to be alive, and he'll figure out how to catch another one for you to take tomorrow.",
  '37': "There is no 'overkill.' There is only 'open fire' and 'I need to reload.'",
  '41': '"Do you have a backup?" means "I can\'t fix this."',

# LOTR
  '\xe2\x88\x98': "One Ring to rule them all, One Ring to find them,\n"
  "One Ring to bring them all and in the darkness bind them.",

# IRC
  '/kick': "Abusing the bots will result in a severe kicking.",

# ATOC easements
  '300393': "Customers travelling via Norwich using fares routed Irish Ferries may travel via Norwich.",
  '300326': "Journeys via Ryde Hoverport must be routed HOVER TRAVEL.",

# XKCD
  'social\xc2\xb7b.99.1': 'If friends spend more than 60 minutes deciding what to do, they must default to sexual experimentation.',

# Misc
  'Britannia' : "Britons never, never, never will be slaves",
  'britannia' : "Britons never, never, never will be slaves",

  'NaN': 'typeof NaN == "number"',
  'nan': 'typeof NaN == "number"',

  'jwz': 'Every program attempts to expand until it can read mail. Those programs which cannot so expand are replaced by ones which can.',
}

if len(argv) >= 5:
    arg = ' '.join(argv[5:])
else:
    arg = argv[-1]


if arg in ('e^(pi*i)', 'e^(i*pi)', 'e^i*pi', 'e^i\xcf\x80', 'e^\xcf\x80i'):
    arg = '-1'

if arg in ('99.1', 'b.99.1', 'social.b.99.1'):
    arg = 'social\xc2\xb7b.99.1'


if arg in ('help', '?', '-?'):
    print "Use ?rules <n> for a specific rule or ?rules to be PM'd all the rules"

elif arg in rules:
    msg = u"Rule %s: %s" % (arg.decode('utf-8'), rules[arg].decode('utf-8'))
    print msg.encode('utf-8')

else:
    if False:
        print argv[1], "I have PM'd you a list of the hackspace rules"
        # open a socket to localhost to allow the pm to be sent
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 12345))
        start = '@%s The rules of the hackspace: \n'% argv[1]
        s.send(start)
        for i in range(max_hackspace_rule + 1):
            msg = "%i of %i: %s \n"%(i, max_hackspace_rule, rules[str(i)])
            s.send(msg)
            sleep(0.1)
        s.close()
    else:
        print 'http://wiki.london.hackspace.org.uk/view/Rules'

