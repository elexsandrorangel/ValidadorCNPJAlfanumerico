import pytest
from cnpj import CNPJ

def test_cnpj_validos():
    assert CNPJ().is_valid("12.ABC.345/01DE-35") == True
    assert CNPJ().is_valid("90.021.382/0001-22") == True
    assert CNPJ().is_valid("90.024.778/0001-23") == True
    assert CNPJ().is_valid("90.025.108/0001-21") == True
    assert CNPJ().is_valid("90.025.255/0001-00") == True
    assert CNPJ().is_valid("90.024.420/0001-09") == True
    assert CNPJ().is_valid("90.024.781/0001-47") == True
    assert CNPJ().is_valid("04.740.714/0001-97") == True
    assert CNPJ().is_valid("44.108.058/0001-29") == True
    assert CNPJ().is_valid("90.024.780/0001-00") == True
    assert CNPJ().is_valid("90.024.779/0001-78") == True
    assert CNPJ().is_valid("00000000000191") == True
    assert CNPJ().is_valid("ABCDEFGHIJKL80") == True

def test_cnpj_invalidos():
    assert CNPJ().is_valid("") == False # Vazio
    assert CNPJ().is_valid("'!@#$%&*-_=+^~") == False # Apenas caracteres não permitidos
    assert CNPJ().is_valid("$0123456789ABC") == False # Caracter não permitido no início
    assert CNPJ().is_valid("0123456?789ABC") == False # Caracter não permitido no meio
    assert CNPJ().is_valid("0123456789ABC#") == False # Caracter não permitido no fim
    assert CNPJ().is_valid("0000000000019") == False # Dígitos a menos
    assert CNPJ().is_valid("000000000001911") == False # Dígitos a mais
    assert CNPJ().is_valid("0000000000019L") == False # Letra na posição do segundo DV
    assert CNPJ().is_valid("000000000001P1") == False # Letra na posição do primeiro DV
    assert CNPJ().is_valid("00000000000192") == False # DV inválido
    assert CNPJ().is_valid("ABCDEFGHIJKL81") == False # DV inválido
    assert CNPJ().is_valid("00000000000000") == False # CNPJ zerado
    assert CNPJ().is_valid("00.000.000/0000-00") == False # CNPJ zerado com máscara
