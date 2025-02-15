from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

def parse_input(user_input: str) -> List[int]:
    nums_str = user_input.strip("[](){} ").replace(" ", "")
    return [int(x) for x in nums_str.split(",")]

if __name__ == "__main__":
    try :
        user_input = input("Enter nums (e.g., [1, 3, 5]): ")
        target = int(input("Enter the target value: ").strip())

        nums = parse_input(user_input)
        result = twoSum(nums, target)

        print(f"The indices are: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers correctly.")

