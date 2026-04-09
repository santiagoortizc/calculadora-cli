"""
Tests para calculadora.py
Ejecutar: python -m pytest tests/ -v
"""

import pytest
from calculadora import calcular, parsear_numero, formatear_resultado


# ── parsear_numero ─────────────────────────────────────────────────────────────


class TestParsearNumero:
    def test_entero_positivo(self):
        assert parsear_numero("5") == 5.0

    def test_entero_negativo(self):
        assert parsear_numero("-3") == -3.0

    def test_decimal(self):
        assert parsear_numero("3.14") == pytest.approx(3.14)

    def test_string_invalido(self):
        with pytest.raises(ValueError, match="no es un número válido"):
            parsear_numero("abc")

    def test_string_vacio(self):
        with pytest.raises(ValueError):
            parsear_numero("")


# ── formatear_resultado ────────────────────────────────────────────────────────


class TestFormatearResultado:
    def test_entero_sin_decimales(self):
        assert formatear_resultado(4.0) == "4"

    def test_float_con_decimales(self):
        assert formatear_resultado(3.14159) == "3.14159"

    def test_ceros_finales_eliminados(self):
        assert formatear_resultado(2.50) == "2.5"


# ── calcular ───────────────────────────────────────────────────────────────────


class TestSuma:
    def test_positivos(self):
        assert calcular("3", "+", "4") == "7"

    def test_negativos(self):
        assert calcular("-2", "+", "-3") == "-5"

    def test_decimales(self):
        assert calcular("1.5", "+", "2.5") == "4"


class TestResta:
    def test_resultado_positivo(self):
        assert calcular("10", "-", "3") == "7"

    def test_resultado_negativo(self):
        assert calcular("3", "-", "10") == "-7"

    def test_mismos_numeros(self):
        assert calcular("5", "-", "5") == "0"


class TestMultiplicacion:
    def test_basica(self):
        assert calcular("6", "*", "7") == "42"

    def test_por_cero(self):
        assert calcular("99", "*", "0") == "0"

    def test_negativos(self):
        assert calcular("-3", "*", "4") == "-12"


class TestPotencia:
    def test_basica(self):
        assert calcular("3", "**", "3") == "27"

    def test_por_cero(self):
        assert calcular("99", "**", "0") == "1"

    def test_negativos(self):
        assert calcular("-3", "**", "4") == "81"
        assert calcular("-3", "**", "3") == "-27"


class TestDivision:
    def test_division_exacta(self):
        assert calcular("10", "/", "2") == "5"

    def test_division_decimal(self):
        resultado = calcular("1", "/", "3")
        assert resultado.startswith("0.3333")

    def test_division_por_cero(self):
        with pytest.raises(ValueError, match="dividir entre cero"):
            calcular("5", "/", "0")


class TestDivisionEntera:
    def test_division_exacta(self):
        assert calcular("10", "//", "3") == "3"

    def test_division_decimal(self):
        resultado = calcular("1", "//", "3")
        assert resultado.startswith("0")

    def test_division_por_cero(self):
        with pytest.raises(ValueError, match="dividir entre cero"):
            calcular("5", "//", "0")


class TestModulo:
    def test_modulo_basico(self):
        assert calcular("10", "%", "3") == "1"

    def test_modulo_con_dividendo_menor(self):
        assert calcular("1", "%", "3") == "1"

    def test_division_por_cero(self):
        with pytest.raises(ValueError, match="dividir entre cero"):
            calcular("5", "%", "0")


class TestErrores:
    def test_operador_invalido(self):
        with pytest.raises(ValueError, match="no reconocido"):
            calcular("5", "^", "2")

    def test_num1_invalido(self):
        with pytest.raises(ValueError, match="no es un número válido"):
            calcular("cinco", "+", "3")

    def test_num2_invalido(self):
        with pytest.raises(ValueError, match="no es un número válido"):
            calcular("5", "+", "tres")
