from morse import decode
import pytest


@pytest.mark.parametrize('morse_msg,decoded_msg',
                         [ ('... --- ...', 'SOS'),
                           ('.-.. --- -. -.. --- -.', 'LONDON'),
                           ('.- ...- .. - ---', 'AVITO')
                         ])

def test_simple_decode(morse_msg, decoded_msg):
    """Тестирование одиночных слов"""
    assert decode(morse_msg) == decoded_msg

def test_wrong_chars():
    """Тестирование на декодирование неверных символов"""
    with pytest.raises(KeyError):
        decode('***')