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


## Week 5 Assignment

> ```bash
> #bash
> docker exec <your container> cat /etc/os-release
> ```
> * This command prints the operating system details of the container by displaying the content of `/etc/os-release`. 
>   - **Output**: The container is running **Ubuntu 24.04.1 LTS** with codename `noble`. It also provides other details like `VERSION_ID`, `HOME_URL`, and support URLs.

> ```bash
> #bash
> docker exec <your container> git --version
> ```
> * This command checks the version of Git installed inside the container.
>   - **Output**: The installed Git version is **2.43.0**.

> ```bash
> #bash
> docker exec <your container> python3 --version
> ```
> * This command checks the version of Python 3 installed in the container.
>   - **Output**: The installed Python version is **3.12.3**.

> ```bash
> #bash
> docker inspect --format="{{ .HostConfig.Binds }}" <container_name>
> ```
> * This command inspects the container's configuration and displays the volume bindings between the host and the container.
>   - **Output**: The host directory `/home/moonjang/moonjang_dir` is mounted to the container at `/container_directory`.
