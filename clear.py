import re

def clearing(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            # 1. 숫자만 추출 (공백, 쉼표, 등 여러 구분자를 무시)
            numbers = re.findall(r'-?\d+', line)  # 정수 추출 (음수 포함)
            # 2. 문자열을 정수로 변환
            row = list(map(int, numbers))
            # 3. 변환된 행 추가
            if row:
                matrix.append(row)
    return matrix

# 예시 실행
if __name__ == "__main__":
    input_file = "input.txt"
    clean_matrix = clearing(input_file)
    print("Resulting Matrix:")
    for row in clean_matrix:
        print(row)
