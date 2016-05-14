import java.util.Random;
import java.util.Map;
import java.util.Map.Entry;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Collections;

public class AdjacencyMatrixGraph {

  List<List<Integer>> matrix;
  Map<Character, Integer> indexCtoI;
  Map<Integer, Character> indexItoC;

  public AdjacencyMatrixGraph() {
    this.matrix = new ArrayList<List<Integer>>();
    this.indexCtoI = new HashMap<Character, Integer>();
    this.indexItoC = new HashMap<Integer, Character>();
  }

  public void addNode(char c) {
    int matrixSide = this.matrix.size();
    // Add a column to the matrix
    for (List<Integer> line : this.matrix) {
      line.add(Integer.valueOf(0));
    }
    // Add a line to the matrix
    List<Integer> newLine = new ArrayList<Integer>(Collections.nCopies(matrixSide + 1, Integer.valueOf(0)));
    matrix.add(newLine);
    // Updates the indexCtoI
    this.indexCtoI.put(Character.valueOf(c), matrixSide);
    this.indexItoC.put(matrixSide, Character.valueOf(c));
  }

  public void addDirectedEdge(char from, char to, int length) {
    int fromIndex = this.indexCtoI.get(from).intValue();
    int toIndex = this.indexCtoI.get(to).intValue();
    this.matrix.get(fromIndex).set(toIndex, Integer.valueOf(length));
  }

  public int dijkstra(char from, char to) {
    Set<Character> unvisited = this.indexCtoI.keySet();
    Map<Character, Integer> shortestPath = new HashMap<Character, Integer>();
    Character visiting = from;
    shortestPath.put(Character.valueOf(from), Integer.valueOf(0));
    while (visiting != null) {
      Integer visitingIndex = this.indexCtoI.get(visiting);
      List<Integer> fromLine = this.matrix.get(visitingIndex);
      for (int i = 0; i < fromLine.size(); i++) {
        Integer length = fromLine.get(i);
        if (length != 0) {
          Integer curDist = shortestPath.get(this.indexItoC.get(Integer.valueOf(i)));
          if ((curDist == null) || (curDist > shortestPath.get(visiting) + length)) {
            shortestPath.put(this.indexItoC.get(Integer.valueOf(i)), length + shortestPath.get(visiting));
          }
        }
      }

      // Loop
      unvisited.remove(visiting);
      visiting = closestUnvisited(unvisited, shortestPath);
    }

    return shortestPath.get(Character.valueOf(to));
  }

  public Character closestUnvisited(Set<Character> unvisited, Map<Character, Integer> shortestPath) {
    Character result = null;
    Integer smallest = null;
    for (Character cur : unvisited) {
      if (smallest == null) {
        result = cur;
        smallest = shortestPath.get(cur);
      } else {
        if ((shortestPath.get(cur) != null) && (shortestPath.get(cur) < smallest)) {
          result = cur;
          smallest = shortestPath.get(cur);
        }
      }
    }
    return result;
  }

  public void print() {
    System.out.print("  ");
    for (int i = 0; i < this.matrix.size(); i++) {
      System.out.print(Character.toString((char) (97 + i)));
      System.out.print(" ");
    }
    System.out.print('\n');
    int j = 0;
    for (List<Integer> line : this.matrix) {
      System.out.print(Character.toString((char) (97 + j)));
      System.out.print(" ");
      for (Integer i : line) {
        System.out.print(i);
        System.out.print(" ");
      }
      System.out.print('\n');
      j++;
    }
  }

  public static void main (String[] args) {
    AdjacencyMatrixGraph graph = new AdjacencyMatrixGraph();
    graph.addNode('a');
    graph.addNode('b');
    graph.addNode('c');
    graph.addNode('d');
    graph.addNode('e');
    graph.addNode('f');
    graph.addNode('g');

    graph.addDirectedEdge('a', 'b', 3);
    graph.addDirectedEdge('a', 'c', 3);
    graph.addDirectedEdge('b', 'd', 4);
    graph.addDirectedEdge('b', 'e', 6);
    graph.addDirectedEdge('c', 'e', 2);
    graph.addDirectedEdge('d', 'f', 5);
    graph.addDirectedEdge('e', 'f', 3);
    graph.addDirectedEdge('e', 'g', 5);
    graph.addDirectedEdge('g', 'f', 1);

    graph.print();

    System.out.println(graph.dijkstra('a', 'f'));
  }

}
