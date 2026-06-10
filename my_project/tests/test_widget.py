import pytest
from src.widget import mask_account_card, get_date

class TestWidget:
    def test_mask_account_card_card(self):
        result = mask_account_card("Visa Platinum 7000792289606361")
        assert result == "Visa Platinum 7000 79** **** 6361"

    def test_mask_account_card_account(self):
        result = mask_account_card("Счёт 73654108430135874305")
        assert result == "Счёт **4305"

    def test_get_date_valid(self):
        result = get_date("2024-03-11T02:26:18.671407")
        assert result == "11.03.2024"

    def test_get_date_invalid(self):
        result = get_date("некорректная дата")
        assert result == "некорректная дата"
