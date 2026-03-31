def minSwaps(self, s):
    """
    Given a string s consisting of '[' and ']', this function returns the minimum number of swaps required to make the string balanced.
    :type s: str
    :rtype: int
    """
    open_available = 0  # Tracks the number of unmatched '[' brackets
    imbalance = 0       # Tracks the number of unmatched ']' brackets (imbalance)

    # Iterate through each character in the string
    for ch in s:
        if ch == '[':
            # Found an opening bracket, increment available open brackets
            open_available += 1
        else:  # ch == ']'
            if open_available > 0:
                # There is an unmatched '[', so match it with this ']'
                open_available -= 1
            else:
                # No unmatched '[', so this ']' is imbalanced
                imbalance += 1

    # Each swap can fix two imbalances, so the answer is (imbalance + 1) // 2
    return (imbalance + 1) // 2