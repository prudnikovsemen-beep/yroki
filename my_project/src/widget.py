from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(input_string: str) -> str:
    """
    Маскирует номер карты или счёта в строке.

    Для карт использует формат: XXXX XX** **** XXXX
    Для счетов использует формат: **XXXX

    Args:
        input_string (str): Строка, содержащая тип и номер (например, "Visa Platinum 7000792289606361").

    Returns:
        str: Строка с замаскированным номером.
    """
    # Разделяем строку на части, последняя часть — номер
    parts = input_string.strip().split()
    if not parts:
        return input_string

    number = parts[-1]
    prefix = ' '.join(parts[:-1])

    # Проверяем, является ли номер счётом (начинается со слова «Счёт»)
    if prefix.startswith('Счёт'):
        masked_number = get_mask_account(number)
    else:
        # Предполагаем, что это карта
        try:
            masked_number = get_mask_card_number(number)
        except ValueError:
            # Если номер карты некорректен, возвращаем исходный номер
            masked_number = number

    return f"{prefix} {masked_number}"

def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_string (str): Дата в формате "2024-03-11T02:26:18.671407".

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ" (например, "11.03.2024").
    """
    try:
        # Парсим дату из строки ISO
        dt = datetime.fromisoformat(date_string)
        # Форматируем в нужный вид
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        # Если формат даты некорректен, возвращаем исходную строку
        return date_string
