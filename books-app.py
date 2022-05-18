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

def search(books_dict, mode, author_name = None, book_title = None):
    if mode == 'A':
        book_results = books_dict.get(author_name, ["None"])
        return f"Books by {author_name}: {', '.join(sorted(book_results))}"
    elif mode == 'B':
        for author, titles in books_dict.items():
                if book_title.lower() in titles:
                    return f"{author.title()} wrote {book_title}"
        return f"{book_title} not found"
    else:
        return "Invalid search mode!"

def add(books_dict, author_name, book_title):
    if author_name in books_dict:
        books_dict[author_name].append(book_title)
    else:
        books_dict[author_name] = [book_title]
    return f"{book_title} added to dictionary!"

def main():
    while True:
        author_name = input("Enter author name: ").lower()
        mode = input("[A]dd or [S]earch? ").upper()
        if mode == 'S':
            search_by = input("Search by [B]ook or [A]uthor? ").upper()
            if search_by == 'B':
                title = input("Enter title to search for: ")
                print(search(books, search_by, author_name, title))
            else:
                print(search(books, search_by, author_name))
        elif mode == 'A':
            title = input("Enter title to add: ").lower()
            print(add(books, author_name, title))
        else:
            print("Invalid mode")
        if input("Continue? (Y/N): ").upper() == 'N':
            break

if __name__ == '__main__':
    main()
