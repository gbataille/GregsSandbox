class Fizzbuzz
  def self.compute
    (1..100).each do |i|
      m3 = i % 3
      m5 = i % 5
      if m3 == 0 and m5 == 0
        puts "FizzBuzz"
      elsif m3 == 0
        puts "Fizz"
      elsif m5 == 0
        puts "Buzz"
      else
        puts i
      end
    end
  end
end

Fizzbuzz.compute
