from typing import List

"""


"""


def encode(strs: List[str]) -> str:
    # Previous implementation didn't properly handle delimiters between strings
    longer = ""

    if not strs:
        return str(strs)

    if len(strs) == 1:
        return strs[0]

    for string in strs:
        longer += string + ";"

    print(longer)

    return longer


def decode(s: str) -> List[str]:

    if s == "[]":
        return []

    return s.split(";")


print(encode(["neet", "code", "love", "you"]))
print(decode("neet code love you"))
print(encode(["we", "say", ":", "yes"]))
print(decode("we say : yes"))
print(encode([""]))
print(decode(encode([""])))

print(
    decode(
        encode(
            [
                "The quick brown fox",
                "jumps over the",
                "lazy dog",
                "1234567890",
                "abcdefghijklmnopqrstuvwxyz",
            ]
        )
    )
)

print(decode(encode(["1,23", "45,6", "7,8,9"])))

print(
    decode(
        encode(
            [
                "",
                "   ",
                "!@#$%^&*()_+",
                "LongStringWithNoSpaces",
                "Another, String With, Commas",
            ]
        )
    )
)
