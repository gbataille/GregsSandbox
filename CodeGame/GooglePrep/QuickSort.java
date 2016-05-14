import java.util.Random;

public class QuickSort {
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

    Node result = QuickSort.quickSort(head);
    result.print();
  }

  public static Node quickSort(Node head) {
    Node pivot = head;
    Node ltHead = null;
    Node gtHead = null;
    Node ltTail = null;
    Node gtTail = null;

    if (head == null) {
      return null;
    }
    if (head.length() == 1) {
      return head;
    }
    Node current = head.nextNode;

    while (current != null) {
      if (current.value < pivot.value) {
        if (ltHead == null) {
          ltHead = current;
          ltTail = current;
        } else {
          ltTail.nextNode = current;
          ltTail = ltTail.nextNode;
        }
      } else {
        if (gtHead == null) {
          gtHead = current;
          gtTail = current;
        } else {
          gtTail.nextNode = current;
          gtTail = gtTail.nextNode;
        }
      }
      current = current.nextNode;
    }
    if (ltTail != null) {
      ltTail.nextNode = null;
    }
    if (gtTail != null) {
      gtTail.nextNode = null;
    }
    head.nextNode = null;
    ltHead = QuickSort.quickSort(ltHead);
    gtHead = QuickSort.quickSort(gtHead);

    Node finalHead = null;
    if (ltHead != null) {
      finalHead = ltHead;
      ltHead.get(ltHead.length() - 1).nextNode = head;
    } else {
      finalHead = head;
    }
    head.nextNode = gtHead;

    return finalHead;
  }

}
