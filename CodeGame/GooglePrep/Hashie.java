import java.util.Random;
import java.util.ArrayList;
import java.util.TreeSet;
import java.util.Set;
import java.util.List;

public class Hashie {

  private List<Integer> values;
  private Set<Integer> index;

  public static void main (String[] args) {
    Random r = new Random();
  }

  public Hashie() {
    this.values = new ArrayList<Integer>();
    this.index = new TreeSet<Integer>();
  }

  public void add(Integer i) {
    int hash = i.hashCode();
  }
}
