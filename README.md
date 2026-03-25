# Calculadora CLI

Calculadora de línea de comandos escrita en Python. Soporta las 7 principales operaciones aritmeticas del lenguaje.

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

python calculadora.py 7.5 * 2
# 7.5 * 2 = 15

python calculadora.py 5 / 0
# Error: No se puede dividir entre cero.

python calculadora.py hola + 3
# Error: 'hola' no es un número válido.
```

## Operadores soportados

| Operador | Operación       |
|----------|-----------------|
| `+`      | Suma            |
| `-`      | Resta           |
| `*`      | Multiplicación  |
| `/`      | División        |
| `//`     | División entera |
| `%`      | Módulo          |
| `**`     | Potencia        |


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
