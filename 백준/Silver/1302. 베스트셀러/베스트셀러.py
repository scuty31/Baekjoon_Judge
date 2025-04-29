def solution():
    books = dict()
    n = int(input())

    for _ in range(n):
        book = input()

        if book in books:
            books[book] += 1
        else:
            books[book] = 1

    sold_books = sorted(books.items(), key=lambda x:(-x[1], x[0]))

    print(sold_books[0][0])

solution()