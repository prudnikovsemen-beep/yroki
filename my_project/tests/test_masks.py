import pytest
from src.masks import get_mask_card_number, get_mask_account

class TestMasks:
    def test_get_mask_card_number_valid_string(self):
        result = get_mask_card_number("7000792289606361")
        assert result == "7000 79** **** 6361"

    def test_get_mask_card_number_valid_int(self):
        result = get_mask_card_number(7000792289606361)
        assert result == "7000 79** **** 6361"

    def test_get_mask_card_number_with_spaces(self):
        result = get_mask_card_number("7000 7922 8960 6361")
        assert result == "7000 79** **** 6361"

    def test_get_mask_card_number_invalid_length(self):
        with pytest.raises(ValueError, match="Номер карты должен содержать ровно 16 цифр"):
            get_mask_card_number("1234567890123")

    def test_get_mask_account_valid_string(self):
        result = get_mask_account("73654108430135874305")
        assert result == "**4305"

    def test_get_mask_account_valid_int(self):
        result = get_mask_account(73654108430135874305)
        assert result == "**4305"

    def test_get_mask_account_with_spaces(self):
        result = get_mask_account("7365 4108 4301 3587 4305")
        assert result == "**4305"

    def test_get_mask_account_invalid_length(self):
        with pytest.raises(ValueError, match="Номер счёта должен содержать минимум 4 цифры"):
            get_mask_account("123")
