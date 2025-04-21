def square_filter(start, end):
    even_squares=[]
    odd_squares=[]

    for num in range(start, end + 1):
        square=num**2
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("even square values:", even_squares)
    print("odd square values:", odd_squares)
square_filter(1, 10)
