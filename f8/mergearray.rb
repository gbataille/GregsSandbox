class Merge
  def self.perform a, b
    result = []
    a.each do |i|
      while not b.empty? and b[0] < i
        result << b[0]
        b = b[1, b.length]
      end
      result << i
    end
    if not b.empty?
      result.concat b
    end
    result
  end
end

p Merge.perform([1,2,3,4],[1,2,3,4])
p Merge.perform([1,2],[3,4] )
p Merge.perform([3,4],[1,2])
p Merge.perform([1,3],[2,4])
