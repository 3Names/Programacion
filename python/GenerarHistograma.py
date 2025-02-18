DIE_FACES: int = 6
throw_list: dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

def main() -> None:
    throw_generator()
    show_histogram()
    show_max()


def throw_generator() -> None:
    i: int = 1
    while i <= DIE_FACES:
        j: int = 1
        while j <= DIE_FACES:
            throw_list[i+j] += 1
            j += 1
        i += 1


def show_histogram() -> None:
    for key, value in throw_list.items():
        throw_value: str = add_aesthetic_to_key(key)
        print(throw_value, ":", "*" * value)


def add_aesthetic_to_key(key: int) -> str:
    result: str = ""

    if key < 10:
        result = f" {key}"
    else:
        result = str(key)
    
    return result


def show_max() -> None:
    '''value_max: int = 0
    key_max: int = 0

    for key, value in throw_list.items():
        if value > value_max:
            value_max = value
            key_max = key
    
    print(f"The maximum is {key_max}.")'''

    max_value = get_the_key_with_max_value()
    print(f"{max_value} has the maximum value")


def get_the_key_with_max_value() -> int:
    maximum_value: int = 0
    key_with_maximum_value: int = 0

    for key, value in throw_list.items():
        if value > maximum_value:
            maximum_value = value
            key_with_maximum_value = key
    
    return key_with_maximum_value

main()
