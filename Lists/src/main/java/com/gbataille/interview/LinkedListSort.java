package com.gbataille.interview;

/**
 * Created by gbataille on 16/07/15.
 */
public class LinkedListSort {
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
    Node node1 = new Node(17, null);
    Node node2 = new Node(14, node1);
    Node node3 = new Node(20, node2);
    Node node4 = new Node(4, node3);
    Node node5 = new Node(10, node4);
    Node node6 = new Node(2, node5);
    Node node7 = new Node(3, node6);
    Node head = new Node(100, node7);

//    Node node = null;
//    node = LinkedListSort.insertionSort(head);
//
//    while (node != null) {
//      System.out.println(node.value);
//      node = node.next;
//    }
    int[] list = new int[]{10,2,3,15,30,12,20,50,39,42};
    LinkedListSort.insertionSort(list);
    for (int i = 0; i < list.length; i++) {
      System.out.println(list[i]);
    }
  }

  public static Node insertionSort(Node first) {
    Node head = first;
    Node beforeLast = null;
    Node last = first;
    Node future = null;
    Node current = first.next;
    while (current != null) {
      future = current.next;
      if (current.value < last.value) {
        if (beforeLast == null) {
          head = current;
          current.next = last;
          beforeLast = current;
        } else {
          // Insert
          LinkedListSort.insertAfter(current, beforeLast);
          beforeLast = beforeLast.next;
          last = beforeLast.next;
        }
      } else {
        last.next = current;
        beforeLast = last;
        last = current;
      }

      current = future;
    }
    last.next = null;

    return head;
  }

  public static void insertAfter(Node toInsert, Node afterThisOne) {

    Node currentAfter = afterThisOne.next;
    afterThisOne.next = toInsert;
    toInsert.next = currentAfter;
  }

  public static void insertionSort(int[] list) {
    int i = 1;
    while (i < list.length) {
      for(int j = i - 1; j >= 0; j--) {
        if (list[j+1] < list[j]) {
          //Swap them
          int temp = list[j+1];
          list[j+1] = list[j];
          list[j] = temp;
        }
      }
      i++;
    }
  }

}
