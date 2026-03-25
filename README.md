# Calculadora CLI

Calculadora de línea de comandos escrita en Python puro. Soporta las cuatro operaciones básicas con manejo robusto de errores.

## Uso

```bash
python calculadora.py <num1> <operador> <num2>
```

### Ejemplos

```bash
python calculadora.py 10 + 5
# 10 + 5 = 15

python calculadora.py 9 / 4
# 9 / 4 = 2.25

python calculadora.py 7.5 "*" 2
# 7.5 * 2 = 15

python calculadora.py 5 / 0
# Error: No se puede dividir entre cero.

python calculadora.py hola + 3
# Error: 'hola' no es un número válido.
```

> En algunos terminales el `*` necesita comillas para evitar que el shell lo expanda como glob.

## Operadores soportados

| Operador | Operación       |
|----------|-----------------|
| `+`      | Suma            |
| `-`      | Resta           |
| `*`      | Multiplicación  |
| `/`      | División        |

## Instalación

No requiere dependencias externas. Solo necesitas Python 3.8+.

```bash
git clone https://github.com/santiagoortizc/calculadora-cli.git
cd calculadora-cli
python calculadora.py 10 + 5
```

## Tests

```bash
# Instalar pytest (única dependencia de desarrollo)
pip install pytest

# Ejecutar todos los tests
python -m pytest tests/ -v
```

Salida esperada:

```
tests/test_calculadora.py::TestParsearNumero::test_entero_positivo    PASSED
tests/test_calculadora.py::TestParsearNumero::test_entero_negativo    PASSED
...
20 passed in 0.05s
```

## Estructura del proyecto

```
calculadora-cli/
├── calculadora.py       # Lógica principal y CLI
├── tests/
│   └── test_calculadora.py
└── README.md
```

## Conceptos practicados

- Funciones puras y separación de responsabilidades
- Manejo de errores con `try/except` y excepciones personalizadas
- Argumentos de línea de comandos con `argparse`
- Tests unitarios con `pytest`
- Documentación con docstrings y README
