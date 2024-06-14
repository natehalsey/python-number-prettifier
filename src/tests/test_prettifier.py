import pytest

from pretty_number import PrettyNumber, PrettyNumberBuilder


class TestPrettyNumber:
    def test_get_num_digits(self, num_ten_million):
        pretty_number = PrettyNumber(num=num_ten_million)
        assert pretty_number.digits == 8

    def test_get_num_digits_with_dec(self, num_ten_million_with_desc):
        pretty_number = PrettyNumber(num=num_ten_million_with_desc)
        assert pretty_number.digits == 8

    def test_get_units_million(self, num_ten_million):
        pretty_number = PrettyNumber(num=num_ten_million)
        assert pretty_number.get_units() == "M"

    def test_get_units_billion(self, num_hundred_billion):
        pretty_number = PrettyNumber(num=num_hundred_billion)
        assert pretty_number.get_units() == "B"

    def test_get_units_trillion(self, num_trillion):
        pretty_number = PrettyNumber(num=num_trillion)
        assert pretty_number.get_units() == "T"

    def test_get_units_too_small(self, num_too_small):
        pretty_number = PrettyNumber(num=num_too_small)
        assert pretty_number.get_units() == ""

    def test_get_units_too_large(self, num_too_large):
        pretty_number = PrettyNumber(num=num_too_large)
        with pytest.raises(NotImplementedError) as excinfo:
            pretty_number.get_units()
        assert str(excinfo.value) == "Only numbers less than 16 digits are supported."


class TestPrettyNumberBuilder:
    def test_prettify_number_million(self, num_ten_million):
        pretty_number = PrettyNumberBuilder.prettify_number(str(num_ten_million))
        assert pretty_number == "12.3M"

    def test_prettify_number_billion(self, num_hundred_billion):
        pretty_number = PrettyNumberBuilder.prettify_number(str(num_hundred_billion))
        assert pretty_number == "123.4B"

    def test_prettify_number_trillion(self, num_trillion):
        pretty_number = PrettyNumberBuilder.prettify_number(str(num_trillion))
        assert pretty_number == "1.2T"

    def test_prettify_number_too_big(self, num_too_large):
        with pytest.raises(NotImplementedError) as excinfo:
            PrettyNumberBuilder.prettify_number(str(num_too_large))
        assert str(excinfo.value) == "Only numbers less than 16 digits are supported."

    def test_prettify_number_too_small(self, num_too_small):
        pretty_number = PrettyNumberBuilder.prettify_number(str(num_too_small))
        assert pretty_number == str(num_too_small)

    def test_prettify_number_with_desc(self, num_ten_million_with_desc):
        pretty_number = PrettyNumberBuilder.prettify_number(
            str(num_ten_million_with_desc)
        )
        assert pretty_number == "12.3M"

    def test_prettify_number_too_small_with_desc(self, num_too_small_with_desc):
        pretty_number = PrettyNumberBuilder.prettify_number(
            str(num_too_small_with_desc)
        )
        assert pretty_number == str(num_too_small_with_desc)

    def test_decimal_part_is_zero(
        self, num_ten_million_with_zero_desc_in_pretty_number
    ):
        pretty_number = PrettyNumberBuilder.prettify_number(
            str(num_ten_million_with_zero_desc_in_pretty_number)
        )
        assert pretty_number == "12M"
