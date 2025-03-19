# Date: 03/04/2025
# Author: @Jgriff1995
# Link: https://leetcode.com/problems/add-binary/
# Time: 45 mins

def addBinary(a, b):
    """
    Adds two binary strings and returns the result as a binary string.

    :type a: str
    :type b: str
    :rtype: str
    Time complexity: O(n)
    Space complexity: O(1)
    """

    # Edge case: if both strings are "0", return "0"
    if a == "0" and b == "0":
        return '0'

    # Remove leading zeros from both strings
    a = a.lstrip('0')
    b = b.lstrip('0')

    # Convert a and b to lists and get their lengths
    n = len(a)
    m = len(b)

    # Ensure 'a' is the longer string to simplify the addition process
    if n < m:
        a, b = b, a
        n, m = m, n

    j = m - 1  # Pointer for string 'b'
    carry = 0  # Initialize carry to 0
    result = []  # List to store the result bits

    # Iterate through the longer string from the end to the start
    for i in range(n-1, -1, -1):
        bit1 = int(a[i])  # Current bit of 'a'
        bitSum = bit1 + carry  # Sum of current bit and carry

        # If there are bits left in 'b', add the current bit of 'b'
        if j >= 0:
            bit2 = int(b[j])
            bitSum += bit2
            j -= 1

        # Calculate the result bit and the new carry
        bit = bitSum % 2
        carry = bitSum // 2

        # Append the result bit to the list
        result.append(str(bit))

    # If there is a carry left after the loop, append it to the result
    if carry > 0:
        result.append('1')

    # Reverse the result list and join it into a string
    return ''.join(result[::-1])


def dumbBinary(a, b):
    """
    Adds two binary strings by converting them to decimal, performing the addition,
    and then converting the result back to binary.

    :type a: str
    :type b: str
    :rtype: str
    Time complexity: O(n)
    Space complexity: O(n)
    """

    # Edge case: if both strings are "0", return "0"
    if a == "0" and b == "0":
        return '0'

    decimalA = 0  # Decimal equivalent of binary string 'a'
    decimalB = 0  # Decimal equivalent of binary string 'b'
    sum_total = 0  # Sum of decimalA and decimalB

    # Convert binary string 'a' to decimal
    for i in range(len(a)):
        bit = int(a[i])
        power = len(a) - 1 - i
        decimalA += bit * (2 ** power)

    # Convert binary string 'b' to decimal
    for i in range(len(b)):
        bit = int(b[i])
        power = len(b) - 1 - i
        decimalB += bit * (2 ** power)

    # Add the two decimal numbers
    sum_total = decimalA + decimalB

    # Convert the sum back to binary
    binaryArray = []
    while sum_total > 0:
        bit = sum_total % 2
        binaryArray.append(str(bit))
        sum_total //= 2

    # Reverse the binary array and join it into a string
    binaryArray.reverse()
    return "".join(binaryArray)


# Test cases with elegant printing
def test_addBinary():
    test_cases = [
        ("1101", "111"),  # Example case
        ("0", "0"),      # Edge case: both strings are "0"
        ("1010", "1011"),  # Case with carry overflow
        ("1111", "1"),   # Case with multiple carries
        ("1", "1111"),   # Reverse of the above case
        ("", "101"),     # Edge case: one string is empty
        ("101", ""),     # Edge case: the other string is empty
        ("101010", "1010101010"),  # Case with different lengths
    ]

    # Test addBinary function
    print("Testing addBinary function:")
    for a, b in test_cases:
        print(f"Test case: a = '{a}', b = '{b}'")
        result = addBinary(a, b)
        print(f"Result: {result}\n")

    # Test dumbBinary function
    print("Testing dumbBinary function:")
    for a, b in test_cases:
        print(f"Test case: a = '{a}', b = '{b}'")
        result = dumbBinary(a, b)
        print(f"Result: {result}\n")


# Run the test cases
test_addBinary()
