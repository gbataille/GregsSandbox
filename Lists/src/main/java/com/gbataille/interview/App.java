package com.gbataille.interview;

/**
 * Hello world!
 *
 */
public class App
{
  static class Node {
    public int value;
    public Node next;

    public Node(int value, Node next) {
      this.value = value;
      this.next = next;
    }
  }

  public static void main( String[] args )
  {
    Node node1 = new Node(7, null);
    Node node2 = new Node(4, node1);
    Node node3 = new Node(2, node2);
    Node head = new Node(1, node3);

    Node node10 = new Node(10, null);
    Node node20 = new Node(8, node10);
    Node node30 = new Node(5, node20);
    Node head0 = new Node(3, node30);

    Node node = App.mergeSortedListInPlace(head0, head);

    while (node != null) {
      System.out.println(node.value);
      node = node.next;
    }
  }

  public static Node mergeSortedRec(Node list1, Node list2) {
    if (list1 == null) {
      return list2;
    }
    if (list2 == null) {
      return list1;
    }

    Node smaller = list2;
    if (list1.value < list2.value) {
      smaller = list1;
    }
    smaller.next = App.mergeSortedRec(list1.next, list2);
    return smaller;
  }

  public static Node mergeSortedListInPlace(Node list1, Node list2) {
    Node head = null;
    Node current = null;
    Node smallest = null;

    while (list1 != null && list2 != null) {
      if (list1.value < list2.value) {
        smallest = list1;
        list1 = list1.next;
      } else {
        smallest = list2;
        list2 = list2.next;
      }

      if (head == null) {
        head = smallest;
        current = smallest;
      }

      current.next = smallest;
      current = smallest;
    }

    if (list1 != null) {
      current.next = list1;
    }
    if (list2 != null) {
      current.next = list2;
    }

    return head;
  }
}
