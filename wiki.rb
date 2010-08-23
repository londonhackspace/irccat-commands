#!/usr/bin/ruby

page = 'London_Hack_Space'

if (!ARGV[4].to_s.empty?)
    page = ARGV[4]
end

puts "http://wiki.hackspace.org.uk/wiki/#{page}"
