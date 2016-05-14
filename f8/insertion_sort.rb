class Sort
  def self.insertion array
    array.each_index do |i|
      if i == 0
        next
      end

      cur_value = array[i]
      running_ind = i-1
      if cur_value < array[running_ind]
        while running_ind >= 0 and array[running_ind] > cur_value
          array[running_ind + 1] = array[running_ind]
          running_ind -= 1
        end
        if running_ind < 0
          array[running_ind + 1] = array[running_ind]
          array[running_ind] = cur_value
        else
          array[running_ind + 1] = cur_value
        end
      end
    end

    array
  end

  def self.quicksort array
    Sort.quicksort_sub array, 0, array.length - 1
  end

  def self.mergesort array
    Sort.mergesort_sub array
  end

  private

  def self.mergesort_sub array
    if array.length < 2
      return array
    end

    middle = array.length / 2

    sortedStart = mergesort_sub array[0, middle]
    sortedEnd   = mergesort_sub array[middle, array.length]
    Sort.merge(sortedStart, sortedEnd)
  end

  def self.merge a, b
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

  def self.quicksort_sub array, start, stop
    effective_length = stop - start + 1
    if effective_length <= 1
      return array
    end
    if effective_length == 2
      if array[start] > array[stop]
        Sort.swap(array, start, stop)
      end
      return array
    end

    pivotIndex = (stop + start) / 2
    pivot = array[pivotIndex]

    Sort.swap(array, pivotIndex, stop)
    small_ind = start
    (start..(stop-1)).each do |i|
      if array[i] < pivot
        Sort.swap(array, small_ind, i)
        small_ind += 1
      end
    end
    Sort.swap(array, small_ind, stop)
    Sort.quicksort_sub(array, start, small_ind - 1)
    Sort.quicksort_sub(array, small_ind + 1, stop)
    array
  end

  def self.swap array, i, j
    val = array[i]
    array[i] = array[j]
    array[j] = val
  end
end

p Sort.insertion [1,4,2,5,6,3]
p Sort.quicksort [1,4,2,5,6,3]
p Sort.mergesort [1,4,2,5,6,3]
