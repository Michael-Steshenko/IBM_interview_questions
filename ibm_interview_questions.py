# Question 1
# Given two integers a and b, divide two integers without using multiplication, division, and mod operator.

# divide n by d without remainder and return the result, if d is 0 raise division by zero exception
def divide_naive(n, d):
    if d == 0:
        raise ZeroDivisionError("division by zero")

    negative = False
    if n < 0:
        n = -n
        negative = not negative
    if d < 0:
        d = -d
        negative = not negative

    res = 0
    while n >= d:
        n -= d
        res += 1
    if negative:
        return -res
    return res


# find the leftmost bit in the result of dividing n by d without remainder
# assumes n and d are positive integers
def find_next_bit(n, d):
    cur_sum, next_sum = d, d
    cur_mult, next_mult = 1, 1
    while next_sum <= n:
        cur_sum = next_sum
        next_sum = next_sum << 1  # in production code we would check for overflow when shifting left

        cur_mult = next_mult
        next_mult = next_mult << 1

    return cur_sum, cur_mult


# divide n by d without remainder and return the result, if d is 0 raise division by zero exception
# runtime: each iteration of the while loop inside find_next_bit() "moves a single bit" from right to left in the result
# of the division to the correct place in its binary representation,
# the result is at most n
# the number of bits in the representation of n is proportional to log(n) hence we get runtime of:
# O(1 + 2 + ... + log(n)) = O( (log(n)) ^ 2 )
def divide_efficient(n, d):
    if d == 0:
        raise ZeroDivisionError("division by zero")

    negative = False
    if n < 0:
        n = -n
        negative = not negative
    if d < 0:
        d = -d
        negative = not negative

    res = 0
    while n >= d:
        cur_sum, cur_mult = find_next_bit(n, d)
        n -= cur_sum
        res += cur_mult

    if negative:
        return -res
    return res


# Question 2
# Gnome buys a lottery ticket that has a 4-digit code associated with it. He thinks that digit 5 is his lucky digit
# and brings him good luck.
# Gnome will win some amount in the lottery if at least one of the digits of the lottery ticket is 5.
# Given three digits N1, N2, N3, and N4 of the lottery ticket, tell whether Gnome wins something or not?
# Input: four integers N1, N2, N3, N4
# Example: 2 4 6 8 – result “no”, 4 5 6 7 – result “yes”

# Input: four integers N1, N2, N3, N4
# Output: print "yes" if one of the digits
def is_winning_ticket(n1, n2, n3, n4):
    if n1 == 5 or n2 == 5 or n3 == 5 or n4 == 5:
        print("yes")
    else:
        print("no")


# Question 3
# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abcabcbb", with the length of 3

# return the length of the longest non repeating substring, using sliding window to get O(n) run time on average
# run time is O(n) because inside the loop each iteration advances i or j, and i and j go from 0 to n = len(str)
# accessing the dictionary to check/update repeating chars is O(1) on average and is done once each iteration.
# memory complexity is constant as we have a finite set of chars that we store in char_count as keys
def no_repeat_substring(str):
    last_index = len(str) - 1
    # store the number of times each letter appears in the current sliding window
    char_count = {}
    max_window_size = 0

    # i, j are left and right side of sliding window respectively
    i, j = 0, 0

    while j <= last_index:
        # increment j until the window contains a duplicate
        # if char does not exist in dict or char count in dict is 0, set it to 1
        while str[j] not in char_count or char_count[str[j]] == 0:
            char_count[str[j]] = 1
            max_window_size = max(max_window_size, j - i + 1)
            j += 1

            # if we reached the end of the string we are sure there are no dupes and can't find a longer window
            if j > last_index:
                return max_window_size

        # we exited the while so str[j] contains a dupe that is char_count[str[j]] == 1
        dupe_char = str[j]

        # increment i until the window doesn't contain duplicates
        while char_count[dupe_char] == 1:
            char_count[str[i]] -= 1
            i += 1

    return max_window_size
