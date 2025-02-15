#!/bin/bash

# Define arrays for test inputs and expected outputs
nums_list=(
    "[2,7,11,15]"
    "[3,2,4]"
    "[3,3]"
)

targets=(
    9
    6
    6
)

answers=(
    "[0, 1]"
    "[1, 2]"
    "[0, 1]"
)

# Get the number of test cases
num_cases=${#nums_list[@]}  # Test case 개수
pass_count=0  # 통과한 테스트 수 초기화

# Loop through each test case
for ((i=0; i<num_cases; i++)); do
    nums=${nums_list[$i]}  # 현재 테스트 케이스의 숫자 배열
    target=${targets[$i]}  # 현재 테스트 케이스의 타겟 값
    answer=${answers[$i]}  # 기대하는 결과 값
    
    # Run the twoSum function and capture the output
    output=$(python3 -c "from main import twoSum; print(twoSum($nums, $target))")
    
    # Compare the output with the expected output
    if [ "$output" == "$answer" ]; then
        echo "Test case $((i+1)): Passed / answer: $answer, Got: $output"
        ((pass_count++))
    else
        echo "Test case $((i+1)): Failed / answer: $answer, Got: $output"
    fi
done

# Print the summary of test results
echo "$pass_count/$num_cases test cases passed"
