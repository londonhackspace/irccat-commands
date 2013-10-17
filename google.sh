#! /usr/bin/env ruby

who = ARGV[0]

4.times { ARGV.delete_at(0) }

output = "#{who}: http://lmgtfy.com/?q=#{ARGV.join('+')}"

puts output