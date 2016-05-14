package com.gbataille.interview;

/**
 * Created by gbataille on 16/07/15.
 */
public class Palindrome {
  public static void main(String[] args) {
    System.out.println(Palindrome.isPalindrome("anna"));
    System.out.println(Palindrome.isPalindrome("kayak"));
    System.out.println(Palindrome.isPalindrome("!kayak;;"));
    System.out.println(Palindrome.isPalindrome("!kay----ak;;"));
    System.out.println(Palindrome.isPalindrome("!ay----ak;;"));
    System.out.println(Palindrome.isPalindrome("an--na"));
  }

  public static boolean isPalindrome(String s) {
    int start = 0;
    int end = s.length() - 1;
    boolean isP = true;

    while (isP && (start < end)) {
      while (!Palindrome.isAlpha(s.charAt(start))) {
        start++;
      }
      while (!Palindrome.isAlpha(s.charAt(end))) {
        end--;
      }

      isP = (s.charAt(start) == s.charAt(end));

      start++;
      end--;
    }
    return isP;
  }

  public static boolean isAlpha(char c) {
    return Character.isLetter(c) || Character.isDigit(c);
  }
}
