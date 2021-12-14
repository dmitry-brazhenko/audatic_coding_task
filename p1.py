import json


def process_float_to_str(item):
    item = round(item, 2)
    return '{:g}'.format(item)


def extract_item_from_list(item):
    if type(item) in (float, int):
        return item
    elif type(item) == list:
        if not item:
            return 0
        s = 0
        for j in item:
            s += extract_item_from_list(j)
        return s / len(item)
    else:
        raise ValueError("Item should be list or int")

def check_name(name):
    name = name[2:]
    available_letters = list(range(48, 58)) + list(range(97, 123)) + list(range(65, 91))
    available_letters = set(list(map(chr, available_letters)))
    for letter in name:
        if letter not in available_letters:
            raise ValueError("Not available values in value naming")


def process_element(element):
    if not element.startswith("--"):
        raise ValueError("Element should start with --")
    if element.count("=") != 1:
        raise ValueError("Element should contain exactly one =")
    if " " in element:
        raise ValueError("There should be no whiespaces")
    name, val = element.split("=")
    check_name(name)

    if "[" not in val:
        return float(val)

    try:
        val = json.loads(val)
        return extract_item_from_list(val)
    except Exception:
        raise ValueError("Error parsing JSON object")


def process_input(q):
    output = []
    q = q.split()
    for i in q:
        try:
            output.append(process_element(i))
        except ValueError:
            return "ERROR"

    output = list(map(process_float_to_str, output))
    return " ".join(output)


def main():
    N = int(input())
    for i in range(N):
        line = input()
        output = process_input(line)
        print(output)


if __name__ == "__main__":
    main()
