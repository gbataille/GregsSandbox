class Hamming {
  public static void main(String[] args) {
    System.out.println(Hamming.distance(5,5));
    System.out.println(Hamming.distance(24,16));
    System.out.println(Hamming.distance(1,3));
    System.out.println(Hamming.distance(1,2));
  }

  public static int distance(int a, int b) {
    int diff = a ^ b;
    return Hamming.weight(diff);
  }

  public static int weight(int a) {
    int count = 0;
    int pow = 1;
    for (int i = 0; i < 32; i++) {
      if ((a & pow) == pow) {
        count++;
      }
      pow = pow * 2;
    }
    return count;
  }
}
