class Solution(object):
    def isPalindrome(self, x):
        
    # Negative Zahlen sind keine Palindrome
        if x < 0:
            return False

        original = x
        reversed_number = 0

    # Umkehren der Zahl
        while x > 0:
            reversed_number = (reversed_number * 10) + (x % 10)
            x //= 10

    # Überprüfung auf Palindrom
        return original == reversed_number

    # Testen der Funktion
        print(isPalindrome(121))  # Sollte True zurückgeben
        print(isPalindrome(-121)) # Sollte False zurückgeben
        print(isPalindrome(10))   # Sollte False zurückgeben
