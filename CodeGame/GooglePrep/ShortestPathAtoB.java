import java.util.Random;
import java.util.Map;
import java.util.Map.Entry;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

public class ShortestPathAtoB {
  public static class Node {
    char value;
    Map<Node, Integer> linkedNodes;

    public Node(char value) {
      this.value = value;
      this.linkedNodes = new HashMap<Node, Integer>();
    }

    public void addLink(Node destination, int length) {
      this.linkedNodes.put(destination, Integer.valueOf(length));
    }
  }

  public static void main (String[] args) {
    Node a = new Node('a');
    Node b = new Node('b');
    Node c = new Node('c');
    Node d = new Node('d');
    Node e = new Node('e');
    Node f = new Node('f');
    Node g = new Node('g');

    a.addLink(b, 3);
    a.addLink(c, 3);
    b.addLink(d, 4);
    b.addLink(e, 6);
    c.addLink(e, 2);
    d.addLink(f, 5);
    e.addLink(g, 5);
    g.addLink(f, 1);

    ShortestPathAtoB.shortest(a, f);
  }

  public static void shortest(Node from, Node to) {
    Set<Node> unvisited = ShortestPathAtoB.allConnectedNodes(from);
    Map<Node, Integer> shortestRoad = new HashMap<Node, Integer>();
    shortestRoad.put(from, Integer.valueOf(0));
    Node visiting = from;
    while (visiting != to) {
      for (Entry<Node, Integer> edge : visiting.linkedNodes.entrySet()) {
        int length = shortestRoad.get(visiting) + edge.getValue();
        if ((!shortestRoad.keySet().contains(edge.getKey())) || (length < shortestRoad.get(edge.getKey()))) {
          shortestRoad.put(edge.getKey(), Integer.valueOf(length));
        }
      }
      unvisited.remove(visiting);
      visiting = ShortestPathAtoB.smallest(unvisited, shortestRoad);
    }

    System.out.println(shortestRoad.get(to));
  }

  public static Node smallest(Set<Node> set, Map<Node, Integer> shortestRoad) {
    Node smallest = null;
    Integer min = null;
    for (Node n : set) {
      if (shortestRoad.get(n) != null) {
        if (smallest == null) {
          smallest = n;
          min = shortestRoad.get(n);
        } else {
          if (shortestRoad.get(n) < min) {
            min = shortestRoad.get(n);
            smallest = n;
          }
        }
      }
    }
    return smallest;
  }

  public static Set<Node> allConnectedNodes(Node from) {
    Set<Node> result = new HashSet<Node>();
    int i = 0;
    if (!result.contains(from)) {
      result.add(from);
      for (Node child : from.linkedNodes.keySet()) {
        if (!result.contains(child)) {
          result.addAll(ShortestPathAtoB.allConnectedNodes(child));
        }
      }
    }
    return result;
  }
}
