require 'json'

path = ARGV[0]
file = File.open(path, "r")

puts JSON.pretty_generate(file.read)

file.close
