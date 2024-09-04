def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        book = f.read()
    word_count = count_words(book)
    character_counts = count_characters(book)
    display_report(word_count, character_counts)


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    lower_case_text = text.lower()
    character_counts = {}
    for character in lower_case_text:
        if character.isalpha():
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1
    return character_counts


def sort_on(dict):
    return dict["num"]


def display_report(word_count, character_counts):
    characters = []
    for character in character_counts:
        characters.append({"name": character, "num": character_counts[character]})
    characters.sort(reverse=True, key=sort_on)

    print(
        "\n--- Begin report of books/frankenstein.txt ---\n",
        f"\n{word_count} words found in the document\n",
    )

    for character in characters:
        print(
            f"The '{character["name"]}' character was found {character["num"]} times"
        )
    print("\n--- End report ---\n")


main()
