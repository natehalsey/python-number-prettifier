from pretty_number import PrettyNumberBuilder


def pretty_number():
    num = input("Enter a number: ")
    while num:
        try:
            prettified_number = PrettyNumberBuilder.prettify_number(num)
            print(prettified_number)
        except NotImplementedError as e:
            print(f"Number could not be prettified: {e}")

        num = input("Enter a number: ")


if __name__ == "__main__":
    pretty_number()
