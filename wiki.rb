#!/usr/bin/ruby
require "rubygems"
require "curb"


page = 'London_Hack_Space'

if (!ARGV[4].to_s.empty?)
    page = String.new
    (4..(ARGV.length - 1)).each { |index|
        page += "#{ARGV[index].to_s} "
    }
    page.gsub!(/ /, "_").gsub!(/_$/, "")
end

curl = Curl::Easy.new
curl.follow_location = true
curl.url = "http://wiki.hackspace.org.uk/w/index.php?search=#{page}"
curl.http_head

puts curl.last_effective_url
