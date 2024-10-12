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
> docker exec moonjang cat /etc/os-release
> ```
> * This command prints the operating system details of the container by displaying the content of `/etc/os-release`. 
>   - **Output**:
>   - ```bash
>   - PRETTY_NAME="Ubuntu 24.04.1 LTS"
>   - NAME="Ubuntu"
>   - VERSION_ID="24.04"
>   - VERSION="24.04.1 LTS (Noble Numbat)"
>   - VERSION_CODENAME=noble
>   - ID=ubuntu
>   - ID_LIKE=debian
>   - HOME_URL="https://www.ubuntu.com/"
>   - SUPPORT_URL="https://help.ubuntu.com/"
>   - BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
>   - PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
>   - UBUNTU_CODENAME=noble
>   - LOGO-ubuntu-logo
>   - ```
>   - The container is running **Ubuntu 24.04.1 LTS** with codename `noble`. It also provides other details like `VERSION_ID`, `HOME_URL`, and support URLs.

> ```bash
> #bash
> docker exec moonjang git --version
> ```
> * This command checks the version of Git installed inside the container.
>   - **Output**: 'git version 2.43.0'
>   - The installed Git version is **2.43.0**.

> ```bash
> #bash
> docker exec moonjang python3 --version
> ```
> * This command checks the version of Python 3 installed in the container.
>   - **Output**: 'Python 3.12.3'
>   - The installed Python version is **3.12.3**.

> ```bash
> #bash
> docker inspect --format="{{ .HostConfig.Binds }}" moonjang
> ```
> * This command inspects the container's configuration and displays the volume bindings between the host and the container.
>   - **Output**: `[/home/moonjang/moonjang_dir:/container_directory]`
>   - The host directory `/home/moonjang/moonjang_dir` is mounted to the container at `/container_directory`.
