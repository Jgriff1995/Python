from typing import List


def totalFruit(fruits: List[int]) -> int:
    max_fruit_collected = 0
    basket = {}
    start, end = 0, len(fruits) + 1

    while start < end:
        current = 0
        for i in range(start, end):
            if len(basket) < 2:
                if fruits[i] not in basket:
                    basket[fruits[i]] = 1
                else:
                    basket[fruits[i]] += 1
            else:
                current = sum(basket.values())
                max_fruit_collected = max(current, max_fruit_collected)
                basket.clear()
                if len(fruits[:i-1]) == 1:
                    start = i - 1
                else:
                    start += 1

    return max_fruit_collected

def totalFruitCorrect(fruits: List[int]) -> int:
    max_fruit_collected = 0
    basket = {}
    left = 0

    for right in range(len(fruits)):
        if fruits[right] in basket:
            basket[fruits[right]] += 1
        else:
            basket[fruits[right]] = 1

        while len(basket) > 2:
            basket[fruits[left]] -= 1
            if basket[fruits[left]] == 0:
                del basket[fruits[left]]
            left += 1

        max_fruit_collected = max(max_fruit_collected, right - left + 1)

    return max_fruit_collected


print(totalFruit([1, 2, 3, 2, 2]))
