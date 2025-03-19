import re

def parseAddress(address: str) -> str:
    """
    We're expecting an address string in this style:
      "<full name>, <street address>, <city> <state> <zip>"
    The full name can include a title at the start or a suffix at the end.
    """

    # Break the address into three parts.
    parts = [p.strip() for p in address.split(',')]
    if len(parts) != 3:
        return "Invalid address format. Expected 3 comma separated parts."

    name_str, street_str, css_str = parts

    # --- Let's break down the Name ---
    prefixes = {"Mr.", "Mrs.", "Ms.", "Dr.", "Prof."}
    # A simple list of suffixes; note that "Duke of Arrakis" is handled later.
    suffixes = {"Jr.", "Sr.", "II", "III", "IV"}

    name_tokens = name_str.split()
    prefix = ""
    suffix = ""
    first_name = ""
    middle_initial = ""
    last_name = ""

    index = 0
    if name_tokens and name_tokens[0] in prefixes:
        prefix = name_tokens[0]
        index = 1

    if index < len(name_tokens):
        first_name = name_tokens[index]
        index += 1

    # Look for the multi-word suffix "Duke of arrakis" regardless of case.
    if len(name_tokens) - index >= 3 and " ".join(name_tokens[-3:]).lower() == "duke of arrakis":
        suffix = "Duke of Arrakis"  # Keeping that cool casing intact
        name_body = name_tokens[index:-3]
    elif name_tokens and name_tokens[-1] in suffixes:
        suffix = name_tokens[-1]
        name_body = name_tokens[index:-1]
    else:
        name_body = name_tokens[index:]

    if len(name_body) >= 2:
        middle_initial = name_body[0][0]
        last_name = " ".join(name_body[1:])
    elif len(name_body) == 1:
        last_name = name_body[0]

    # --- Now let's figure out the Street Address ---
    street_tokens = street_str.split()
    street_number = ""
    street_name_tokens = []

    if street_tokens and street_tokens[0].isdigit():
        street_number = street_tokens[0]
        street_name_tokens = street_tokens[1:]
    else:
        for i, token in enumerate(street_tokens):
            if token.isdigit():
                street_number = token
                street_name_tokens = street_tokens[i+1:]
                break
    apt = ""
    if "Apt." in street_name_tokens:
        apt_index = street_name_tokens.index("Apt.")
        if apt_index + 1 < len(street_name_tokens):
            apt = street_name_tokens[apt_index] + " " + street_name_tokens[apt_index+1]
        street_name_tokens = street_name_tokens[:apt_index] + street_name_tokens[apt_index+2:]
    street_name = " ".join(street_name_tokens)

    # --- And finally, extract City, State, and Zip ---
    css_tokens = css_str.split()
    if len(css_tokens) < 3:
        return "Invalid city, state, zip format."
    zip_code = css_tokens[-1]
    state = css_tokens[-2]
    city = " ".join(css_tokens[:-2])

    result = (
        f"Prefix: {prefix}\n"
        f"First Name: {first_name}\n"
        f"Middle Initial: {middle_initial}\n"
        f"Last Name: {last_name}\n"
        f"Suffix: {suffix}\n"
        f"Street Number: {street_number}\n"
        f"Street Name: {street_name}\n"
        f"Apt/Unit: {apt}\n"
        f"City: {city}\n"
        f"State: {state}\n"
        f"Zip Code: {zip_code}"
    )
    return result

# Some examples to try out.
example_input = "Mr. Frodo Baggins, 10 Bagshot Row, Hobbiton WV 25411"
example_input2 = "Paul A Muad'dib Atreides Duke of Arrakis, 13000 Desert Road, Arrakis AZ 85390"
example_input3 = "Dr. Shohei T Ohtani, 17 Dodgers Lane Apt. 700, Los Angeles CA 90012"

if __name__ == "__main__":
    for addr in [example_input, example_input2, example_input3]:
        print("Input:", addr)
        print(parseAddress(addr))
        print("-" * 40)
