# SWE_2021_41_2024_2_week_6

---

* https://github.com/ParalMoon/SWE_2021_42_2024_2_week_4
```
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
* The `isHappy` function checks whether a number is a **happy number**. It uses a helper function `go(number)` that calculates the sum of the squares of a number's digits. The main idea is to track two sequences of numbers: `slow` and `fast`. `slow` progresses by applying `go()` once, while `fast` progresses by applying `go()` twice. This is similar to the **tortoise and hare** cycle detection algorithm.

* If `fast` becomes 1, the number is happy. If `slow` meets `fast` (without reaching 1), a cycle exists, indicating the number is not happy. The function returns `\textbf{True}` if $n$ is a happy number and `\textbf{False}` otherwise.


---

