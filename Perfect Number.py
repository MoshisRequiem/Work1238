def is_perfect_number(n):
    original_number = n
    while n > 0:
        digit = n % 10  # Get the last digit
        if digit == 0 or original_number % digit != 0:
            return False
        n //= 10  # Remove the last digit
    return True


def find_perfect_numbers_sum(start, end):
    total_sum = 0

    for number in range(start, end + 1):
        if is_perfect_number(number):
            total_sum += number

    return total_sum


def main():
    start_range = int(input())
    end_range = int(input())
    perfect_numbers_sum = find_perfect_numbers_sum(start_range, end_range)
    print(perfect_numbers_sum)


if __name__ == "__main__":
    main()
