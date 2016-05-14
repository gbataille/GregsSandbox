import java.util.Random;

public class MergeSort {
  public static class Node {
    int value;
    Node nextNode;

    public Node(int value, Node next) {
      this.value = value;
      this.nextNode = next;
    }

    public int length() {
      Node current = this;
      int count = 0;
      while (current != null) {
        count++;
        current = current.nextNode;
      }
      return count;
    }

    public Node get(int i) {
      Node current = this;
      int index = 0;
      while ((index != i) && (current != null)) {
        index++;
        current = current.nextNode;
      }
      return current;
    }

    public void print() {
      Node current = this;
      System.out.println("  head");
      while (current != null) {
        System.out.println(current.value);
        current = current.nextNode;
      }
    }
  }

  public static void main (String[] args) {
    Random r = new Random();
    Node previous = null;
    Node head = null;
    for (int i = 0; i < 30; i++) {
      Node newNode = new Node(r.nextInt(), null);
      if (head == null) {
        head = newNode;
      }
      if (previous != null) {
        previous.nextNode = newNode;
      }
      previous = newNode;
    }

    MergeSort.mergeSort(head).print();
  }

  public static Node mergeSort(Node head) {
    int length = head.length();

    if (length == 1) {
      return head;
    }
    int half = length / 2;
    Node subList1 = head;
    Node subList1Tail = subList1.get(half-1);
    Node subList2 = subList1Tail.nextNode;
    subList1Tail.nextNode = null;

    return mergeSorted(mergeSort(subList1), mergeSort(subList2));
  }

  public static Node mergeSorted(Node list1, Node list2) {
    Node head = null;
    Node tail = null;
    while ((list1 != null) && (list2 !=null)) {
      Node min = null;
      if (list2.value < list1.value) {
        min = list2;
        list2 = list2.nextNode;
      } else {
        min = list1;
        list1 = list1.nextNode;
      }

      if (tail != null) {
        tail.nextNode = new Node(min.value, null);
        tail = tail.nextNode;
      } else {
        tail = new Node(min.value, null);
        head = tail;
      }
    }
    if (list1 != null) {
      tail.nextNode = list1;
    } else {
      tail.nextNode = list2;
    }
    head.print();
    return head;
  }
}
