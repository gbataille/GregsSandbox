import java.util.Random;
import java.util.Map;
import java.util.Map.Entry;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;

public class MergeArray {

  int[] array;

  public MergeArray() {
    this.array = new int[] {1,3,5,10,49,6,2,4,78,7};
  }

  public int length() {
    return this.array.length;
  }

  public int get(int i) {
    return this.array[i];
  }

  public void sort() {
    this.splitSort(0, this.array.length);
    return;
  }

  public void print() {
    for (int i = 0; i < this.array.length; i++) {
      System.out.print(this.array[i]);
      System.out.print(" ");
    }
    System.out.print('\n');
  }

  public void splitSort(int from, int to) {
    if (from > to) {
      System.exit(0);
    }
    if ((to - from) == 1) {
      return;
    }
    if ((to - from) == 2) {
      if (this.array[from] > this.array[to - 1]) {
        int temp = this.array[from];
        this.array[from] = this.array[to - 1];
        this.array[to - 1] = temp;
      }
      return;
    }
    int half = from + ((to - from) / 2);
    this.splitSort(from, half);
    this.splitSort(half, to);
    this.merge(from, half, to);
  }

  public void merge(int from, int split, int to) {
    int pivot = split;
    int i = from;
    while ((i < pivot) && (pivot < to)) {
      if (this.array[i] > this.array[pivot]) {
        // then shift
        int temp = this.array[pivot];
        for (int j = pivot; j > i; j--) {
          this.array[j] = this.array[j-1];
        }
        this.array[i] = temp;
        pivot++;
        if (pivot >= to) {
          break;
        }
      }
      i++;
    }
    return;
  }

  public static void main (String[] args) {
    MergeArray ma = new MergeArray();
    ma.sort();
    ma.print();
  }

}
