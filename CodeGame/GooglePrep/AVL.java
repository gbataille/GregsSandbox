import java.util.Random;
import java.util.List;
import java.util.ArrayList;

public class AVL {

  int value;
  int balance;
  int depth;
  AVL leftAVL;
  AVL rightAVL;
  AVL parent;

  public AVL(int value, AVL left, AVL right) {
    this.value = value;
    this.leftAVL = left;
    this.rightAVL = right;
    this.depth = 0;
    int leftBalance = 0;
    int rightBalance = 0;
    if (left != null) {
      leftBalance = left.balance;
    }
    if (right != null) {
      rightBalance = right.balance;
    }
    this.balance = leftBalance - rightBalance;
    this.parent = null;
  }

  public boolean equalsAVL(AVL other) {
    if (other == null) {
      return false;
    }
    return this.value == other.value;
  }

  public int hashCode() {
    return Integer.valueOf(this.value).hashCode();
  }

  public void print() {
    this.print(0);
  }

  public void print(int offset) {
    for (int i = 0; i < offset; i++) {
      System.out.print(" ");
    }
    System.out.println("left");

    if (this.leftAVL != null) {
      this.leftAVL.print(offset + 1);
    }
    for (int i = 0; i < offset; i++) {
      System.out.print(" ");
    }
    System.out.print(value);
    System.out.print(" - ");
    System.out.print(balance);
    System.out.print('\n');
    for (int i = 0; i < offset; i++) {
      System.out.print(" ");
    }
    System.out.println("right");
    if (this.rightAVL != null) {
      this.rightAVL.print(offset + 1);
    }
    if (offset == 0) {
      System.out.println("---");
    }
  }

  public void addNode(AVL newAVL) {
    if (newAVL.value < this.value) {
      if (this.leftAVL == null) {
        this.leftAVL = newAVL;
        newAVL.parent = this;
        this.updateBalance(1);
      } else {
        this.leftAVL.addNode(newAVL);
      }
    } else {
      if (this.rightAVL == null) {
        this.rightAVL = newAVL;
        newAVL.parent = this;
        this.updateBalance(-1);
      } else {
        this.rightAVL.addNode(newAVL);
      }
    }
  }

  public void updateBalance(int delta) {
    this.balance += delta;
    if ((this.balance == 2) || (this.balance == -2)) {
      this.rebalance();
    } else {
      if (this.parent != null) {
        if (this == this.parent.leftAVL) {
          this.parent.updateBalance(1);
        } else {
          this.parent.updateBalance(-1);
        }
      }
    }
  }

  public void rebalance() {
    if (this.balance == 2) {
      if (this.leftAVL.balance == -1) {
        this.leftAVL.rotateLeft();
      }
      this.rotateRight();
    } else {
      if (this.rightAVL.balance == 1) {
        this.rightAVL.rotateRight();
      }
      this.rotateLeft();
    }
  }

  public void rotateRight() {
    this.balance = 0;
    if (this.leftAVL != null) {
      this.leftAVL.balance = 0;
    }
    if (this.rightAVL != null) {
      this.rightAVL.balance = 0;
    }
    AVL ancestor = this.parent;
    AVL rightOfLeft = this.leftAVL.rightAVL;
    this.leftAVL.rightAVL = this;
    if (ancestor != null) {
      if (ancestor.leftAVL == this) {
        ancestor.leftAVL = this.leftAVL;
      } else {
        ancestor.rightAVL = this.leftAVL;
      }
    }
    this.leftAVL = rightOfLeft;
  }
  public void rotateLeft() {
    this.balance = 0;
    if (this.leftAVL != null) {
      this.leftAVL.balance = 0;
    }
    if (this.rightAVL != null) {
      this.rightAVL.balance = 0;
    }
    AVL ancestor = this.parent;
    AVL leftOfRight = this.rightAVL.leftAVL;
    this.rightAVL.leftAVL = this;
    if (ancestor != null) {
      if (ancestor.leftAVL == this) {
        ancestor.leftAVL = this.rightAVL;
      } else {
        ancestor.rightAVL = this.rightAVL;
      }
    }
    this.rightAVL = leftOfRight;
  }

  public static void main (String[] args) {
    AVL a = new AVL(0, null, null);
    for(int i = 1; i < 6; i++) {
      AVL node = new AVL(i, null, null);
      a.addNode(node);
      if (i != 0) {
        node = new AVL(-1*i, null, null);
        a.addNode(node);
      }
    }
    a.print();
  }

}
