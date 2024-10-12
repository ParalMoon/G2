# SWE_2021_41_2024_2_week_6

---

* https://github.com/ParalMoon/SWE_2021_42_2024_2_week_4
```python
#python
def isHappy(n):
    def go(number):
        total = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total += digit ** 2
        return total

    slow = n
    fast = go(n)
    while fast != 1 and slow != fast:
        slow = go(slow)
        fast = go(go(fast))

    return fast == 1

```
* The `isHappy` function determines if a number is a **happy number**. It uses a helper function `go(number)` to compute the sum of the squares of the number's digits. Two variables of numbers, `slow` and `fast`, track the progression of the sum: `slow` is updated once per iteration, while `fast` is updated twice. If `fast` reaches 1, the number is happy. If `slow` and `fast` converge without reaching 1, a cycle is detected, meaning the number is not happy. The function returns `True` if $n$ is a happy number, and `False` otherwise.

* This approach leverages **Floyd's cycle detection algorithm** (also known as the **tortoise and hare algorithm**). [Learn more about the algorithm here](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare)


---
## Week 5 Assignment

>
```bash
docker exec <your container> cat /etc/os-release
```



