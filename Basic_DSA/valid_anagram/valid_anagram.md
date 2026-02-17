
# the concurrency counter pattern: Counting

# Valid Anagram:

    -> Given two strings 's' and 't', return true if the two strings are anagrams of each other, otherwise return false.

    -> An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


    Example 1:

        Input: s = "racecar", t = "carrace"

        Output: true

    Example 2:

        Input: s = "jar", t = "jam"

        Output: false
    Constraints:

        - s and t consist of lowercase English letters.

    approch:

        s = "listen" and t = "silent"

        1. check the lenght of both strings if same return True otherwise false -> can't be a anagram

        2. a seen varaible

        3. loop throw s and with each count of string +1 the seen, 
           loop throw t and with each count of string -1 the seen,

        4. after loop check all values == 0, means
        After the loop, c1 gets +6 and c2 gets -6, then they cancel to 0 = perfect anagram
    