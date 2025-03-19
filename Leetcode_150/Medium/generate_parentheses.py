from typing import List


def generateParenthesis(n: int) -> List[str]:
    """
    Generate all combinations of well-formed parentheses for n pairs
    using backtracking approach.
    """
    result = []

    def backtrack(open_count: int, close_count: int, current: str):
        # Base case: if we have used all n pairs
        if len(current) == 2 * n:
            result.append(current)
            return

        # Add open parenthesis if we haven't used all n
        if open_count < n:
            backtrack(open_count + 1, close_count, current + "(")

        # Add closing parenthesis if we have more open than closed
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ")")

    # Start backtracking with empty string
    backtrack(0, 0, "")
    return result


print(generateParenthesis(1))
print(generateParenthesis(3))
