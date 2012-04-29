require 'json'

path = ARGV[0]
file = File.open(path, "r")
lastline=""

while line=file.gets do
	lastline = line	
end
puts JSON.pretty_generate(JSON.parse(lastline))
#puts lastline

file.close
