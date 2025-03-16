import os

# File to store the library data
LIBRARY_FILE = "library.txt"

#Load library from file (if exists)
def load_library():
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as file:
                return eval(file.read()) # Safely load the list of dictionaries
        except:
            print("⚠️ Error Loading Library. Starting frest!")
    return []

# Save library to file

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        file.write(str(library))

# Add a book to the library
def add_book(library):
    print("\n 📚Add a Book")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        year = int(input("Publication Year: "))
    except ValueError:
        print("❌ Invalid Year. Please Enter a Number.")
        return
    genre = input("Genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    library.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read_status})
    print(f"✅ '{title}' added successfully!")


# Remove a book by title
def remove_book(library):
    print("\n🗑️ Remove a Book")
    title = input(f"Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            confirm = input(f"Remove '{title}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                library.remove(book)
                print(f"✅ '{title}' removed successfully!")
            else:
                print("❌ Removal Cancelled.")
            return
    print(f"⚠️ '{title}' not found.")


# Search for books by title or author
def search_book(library):
    print("\n🔍 Search for a Book")
    query = input("Search by Title or Author: ").strip().lower()
    matches = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    if matches:
        print("\n📖 Matching Books:")
        for i, book in enumerate(matches, 1):
            status = "✅ Read" if book["read_status"] else "❌ Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("⚠️ No Match Found.")

# Display all books in the library
def display_all_books(library):
    print("\n📚 Your Library")
    if not library:
        print("⚠️ Your library is empty.")
        return
    for i, book in enumerate(library, 1):
        status = "✅ Read" if book["read_status"] else "❌ Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display library statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read_status"])
    unread_books = total_books - read_books
    print("\n📊 Library Statistics")
    print(f"📚 Total Books: {total_books}")
    if total_books > 0:
        percentage_read = (read_books / total_books) * 100
        print(f"📖 Percentage Read: {percentage_read:.1f}%")
    else:
        print("⚠️ No Books in the Library.")


# Main Menu System
def main():
    library = load_library()

    while True:
        print("\n ⭐ Personal Library Manager ⭐")
        print("1. 📚 Add a Book")
        print("2. 🗑️ Remove a Book")
        print("3. 🔍 Search for a Book")
        print("4. 📝 View All Books")
        print("5. 📊 View Statistics")
        print("6. ❌ Exit")

        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("💾 Library saved. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try Again!")

# Signature
print("\n ---   Created by Afifa ----")

# Run the program
if __name__ == "__main__":
    main()
