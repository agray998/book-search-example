# Problem: create a dictionary associating authors to lists of books, and write
# search functionality to take an author name from the user and print the books by
# that author.
# Stretch goals: display the books in alphabetical order, and implement add 
# functionality.

books = {
    "margaret atwood": ["the handmaid's tale", "the blind assassin"],
    "roald dahl": ["charlie and the chocolate factory", "matilda", "james and the giant peach"],
    "j.r.r. tolkien": ["the hobbit", "the lord of the rings", "the silmarillion"]
    }

while True:
    author_name = input("Enter author name: ").lower()
    mode = input("[A]dd or [S]earch? ").upper()
    if mode == 'S':
        search_by = input("Search by [B]ook or [A]uthor? ").upper()
        if search_by == 'A':
            book_results = books.get(author_name, ["None"])
            print(f"Books by {author_name}: ", ', '.join(sorted(book_results)))
        elif search_by == 'B':
            title = input("Enter title to search for: ")
            for author, titles in books.items():
                if title.lower() in titles:
                    print(author.title(), "wrote", title)
                    break
        else:
            print("Invalid term to search by!")
    elif mode == 'A':
        title = input("Enter title to add: ").lower()
        if author_name in books:
            books[author_name].append(title)
        else:
            books[author_name] = [title]
    else:
        print("Invalid mode")
    if input("Continue? (Y/N): ").upper() == 'N':
        break
