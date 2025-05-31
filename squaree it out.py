def squares_and_separation():
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))

    squares = [num**2 for num in range(start_range, end_range + 1)]

    odd_squares = [square for square in squares if square % 2 != 0]
    even_squares = [square for square in squares if square % 2 == 0]

    print("Squares:", squares)
    print("Odd Squares:", odd_squares)
    print("Even Squares:", even_squares)

squares_and_separation()