class Hamming
  def self.distance a, b
    diff = a ^ b
    p Hamming.weight(diff)
  end

  def self.weight a
    bit = 2 ** 0
    count = 0
    (0..32).each do |i|
      if (bit & a) == bit
        count +=1
      end
      bit *= 2
    end
    count
  end
end

Hamming.distance(3,3 )
Hamming.distance(16,3)
Hamming.distance(24,8)
Hamming.distance(7,15)

RSpec.describe Hamming do
  it 'should run' do
    expect(1).to eq(1)
  end
end
