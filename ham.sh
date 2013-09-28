#!/usr/bin/env ruby

# irccat passes [$username, x, x, x] as the first four parameters
# then we get (maybe) more parameters, which should be:
#   "set <date>"

require 'date'

filename = "/usr/share/irccat/.ham.txt"
admins = ["tgreer", "wyan", "Filbert", "samuelk"]

if ARGV.length > 4 && ARGV[4].downcase == "set" && admins.include?(ARGV[0])
  begin
    new_date = DateTime.parse(ARGV[5..99].join ' ')
    File.open(filename, 'w') { |f| f.write(new_date) }
  rescue
  end
end

line = File.open(filename, &:readline)
# Sun Jun 23 23:02:29 BST 2013
puts "Next amateur radio meeting: " +
     DateTime.parse(line).strftime("%a %b %e %H:%M:%S #{Time.now.zone} %Y")
