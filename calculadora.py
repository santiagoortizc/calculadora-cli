import argparse
import sys


# ── Operaciones ────────────────────────────────────────────────────────────────


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def division_entera(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a // b


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a % b


def potencia(a: float, b: float) -> float:
    return a**b


OPERACIONES = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
    "//": division_entera,
    "%": modulo,
    "**": potencia,
}


# ── Helpers ────────────────────────────────────────────────────────────────────


def parsear_numero(valor: str) -> float:
    """Convierte un string a float, lanzando un error claro si no es válido."""
    try:
        return float(valor)
    except ValueError:
        raise ValueError(f"'{valor}' no es un número válido.")


def formatear_resultado(resultado: float) -> str:
    """
    Muestra enteros sin decimales y floats con hasta 10 decimales
    eliminando ceros al final.
      formatear_resultado(4.0)      → "4"
      formatear_resultado(3.14159)  → "3.14159"
    """
    if resultado == int(resultado):
        return str(int(resultado))
    return f"{resultado:.10f}".rstrip("0")


# ── Lógica principal ───────────────────────────────────────────────────────────


def calcular(num1: str, operador: str, num2: str) -> str:
    """
    Recibe los argumentos como strings (igual que vienen de la CLI),
    valida, calcula y devuelve el resultado formateado.
    """
    a = parsear_numero(num1)
    b = parsear_numero(num2)

    if operador not in OPERACIONES:
        ops = ", ".join(OPERACIONES.keys())
        raise ValueError(f"Operador '{operador}' no reconocido. Usa: {ops}")

    resultado = OPERACIONES[operador](a, b)
    return formatear_resultado(resultado)


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calculadora",
        description="Calculadora de línea de comandos. Soporta +, -, *, /",
        epilog="Ejemplo: python calculadora.py 10 / 3",
    )
    parser.add_argument("num1", help="Primer número")
    parser.add_argument("operador", help="Operador: + - * /")
    parser.add_argument("num2", help="Segundo número")
    return parser


def main():
    parser = construir_parser()
    args = parser.parse_args()

    try:
        resultado = calcular(args.num1, args.operador, args.num2)
        print(f"{args.num1} {args.operador} {args.num2} = {resultado}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
