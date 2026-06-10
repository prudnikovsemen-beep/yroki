from typing import Union

def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Маскирует номер банковской карты.

    Видимы первые 6 и последние 4 цифры, остальные заменяются на звёздочки.
    Формат вывода: XXXX XX** **** XXXX

    Args:
        card_number (Union[str, int]): Номер карты в виде строки или числа.

    Returns:
        str: Замаскированный номер карты.

    Raises:
        ValueError: Если номер карты не содержит ровно 16 цифр.
    """
    # Приводим к строке и оставляем только цифры
    cleaned_number = ''.join(filter(str.isdigit, str(card_number)))

    if len(cleaned_number) != 16:
        raise ValueError(f"Номер карты должен содержать ровно 16 цифр, получено: {len(cleaned_number)}")

    # Формируем маску: первые 6 + 6 звёздочек + последние 4
    masked = cleaned_number[:6] + '*' * 6 + cleaned_number[-4:]

    # Разбиваем на блоки по 4 цифры и соединяем пробелами
    blocks = [masked[i:i+4] for i in range(0, 16, 4)]
    return ' '.join(blocks)


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Маскирует номер банковского счёта.

    Видимы только последние 4 цифры, перед ними две звёздочки.
    Формат вывода: **XXXX

    Args:
        account_number (Union[str, int]): Номер счёта в виде строки или числа.

    Returns:
        str: Замаскированный номер счёта.

    Raises:
        ValueError: Если номер счёта содержит меньше 4 цифр.
    """
    # Приводим к строке и оставляем только цифры
    cleaned_number = ''.join(filter(str.isdigit, str(account_number)))

    if len(cleaned_number) < 4:
        raise ValueError(f"Номер счёта должен содержать минимум 4 цифры, получено: {len(cleaned_number)}")

    # Берём последние 4 цифры
    visible_part = cleaned_number[-4:]
    return f"**{visible_part}"
