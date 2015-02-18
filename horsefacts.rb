#!/usr/bin/ruby1.9
 
require 'rubygems'
require 'thread'
require 'marky_markov'
 
PATH_TO_FACTS = '/usr/share/irccat/horsefacts.txt'
 
markov = MarkyMarkov::Dictionary.new('dictionary') # Saves/opens dictionary.mmd
markov.parse_file PATH_TO_FACTS
fact = markov.generate_n_sentences(2).split(/\#\</).first.chomp.chop

puts "#{fact}"
