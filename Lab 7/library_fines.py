import re

# Whole-input patterns. [0-9] (not \d) so that only ASCII digits are
# accepted, and at most 10 digits so int() never sees a huge number.
MEMBER_ID_PATTERN = re.compile(r"([A-Za-z]+)-([0-9]{1,10})")
DAYS_PATTERN = re.compile(r"[0-9]{1,10}")


def parse_member_id(member_id):
    """'STU-1023' -> ('STU', 1023). Returns None for invalid input."""
    if not isinstance(member_id, str):
        return None
    match = MEMBER_ID_PATTERN.fullmatch(member_id.strip())
    if match is None:
        return None
    member_type, number = match.groups()
    return member_type.upper(), int(number)


def total_fine(days_csv):
    """'10,20,30' -> 44 (2 per day over 14). Returns None for invalid input."""
    if not isinstance(days_csv, str):
        return None
    items = [item.strip() for item in days_csv.split(',')]
    if not all(DAYS_PATTERN.fullmatch(item) for item in items):
        return None
    fine = 0
    for d in map(int, items):
        if d > 14:
            fine += (d - 14) * 2
    return fine


def shelf_code(title):
    """'Harry Potter' -> 'HP'. Returns None for invalid input."""
    if not isinstance(title, str):
        return None
    words = title.split()
    if len(words) < 2:
        return None
    # upper() can return more than one character ('ß' -> 'SS'),
    # so keep only the first one to make the code exactly 2 characters.
    return words[0][0].upper()[0] + words[1][0].upper()[0]


def read_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None


def main():
    print("==== Running parse_member_id ====")
    user_input = read_input("Enter a member ID (e.g. STU-1023): ")
    result = parse_member_id(user_input)
    if result is None:
        print("Invalid member ID. Use letters, '-' and a number, e.g. STU-1023.")
    else:
        print("Member Type and Number:", result)

    print("\n==== Running total_fine ====")
    user_input = read_input("Enter days kept for each book as CSV (e.g. 10,20,30): ")
    result = total_fine(user_input)
    if result is None:
        print("Invalid input. Enter whole numbers of days separated by commas.")
    else:
        print("Total Fine:", result)

    print("\n==== Running shelf_code ====")
    user_input = read_input("Enter a book title with at least two words: ")
    result = shelf_code(user_input)
    if result is None:
        print("Invalid title. Enter at least two words.")
    else:
        print("Shelf Code:", result)


if __name__ == "__main__":
    main()
