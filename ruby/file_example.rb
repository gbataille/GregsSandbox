file = File.open("test.txt", "r")
while (line = file.gets)
				puts line
end
file.close
