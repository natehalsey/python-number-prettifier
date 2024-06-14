from functools import cached_property


class PrettyNumber:
    MIN_DIGITS: int = 7
    MAX_DIGITS: int = 15

    def __init__(self, num: float):
        self.num: float = num

    @cached_property
    def digits(self) -> int:
        # we need the length the integer portion of the float
        return len(str(int(self.num)))

    @cached_property
    def sig_figs(self) -> int:
        # we can subtract the minimum digits (before million) and get the modulo to find the sig figs
        return ((self.digits - 7) % 3) + 1

    def get_units(self) -> str:
        # TODO: support more digits
        if self.digits > self.MAX_DIGITS:
            raise NotImplementedError("Only numbers less than 16 digits are supported.")

        if self.digits < 7:
            return ""
        if self.digits < 10:
            return "M"
        if self.digits < 13:
            return "B"
        if self.digits < 16:
            return "T"


class PrettyNumberBuilder:
    @staticmethod
    def prettify_number(num: str) -> str:
        pretty_number = PrettyNumber(float(num))

        if pretty_number.digits < pretty_number.MIN_DIGITS:
            return num

        units = pretty_number.get_units()

        # we join the tuple back together into a string
        whole_part = "".join((str(num[i]) for i in range(pretty_number.sig_figs)))
        decimal_part = num[pretty_number.sig_figs]

        if decimal_part == "0":
            return f"{whole_part}{units}"

        return f"{whole_part}.{decimal_part}{units}"
