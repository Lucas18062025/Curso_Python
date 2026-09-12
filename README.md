# Curso.py

Curso práctico de Python: fundamentos (variables, strings, condicionales,
bucles, listas) y una serie de mini-proyectos (juegos, calculadoras
geométricas con clases, generación/hash de contraseñas y un experimento con
FastAPI). Cada archivo se ejecuta de forma independiente con `python <archivo>.py`.

## Requisitos

- Python 3.10 o superior.
- Para `main.py`, `Untitled-1.py` y `lanzador.py`: `fastapi`, `uvicorn` y `pytz`
  (no incluidos en el repo; instalar con `pip install fastapi uvicorn pytz`).

## Uso

```sh
python intro.py
python adivinar.py
python piedrapapel.py
```

## Fundamentos

| Archivo | Tema |
|---|---|
| `01-variables.py` | Variables y tipos básicos |
| `02-if.py` | Condicionales, incluido `if` anidado |
| `02-strings.py` | Strings: longitud, indexado y slicing |
| `03-formart-springs.py` | Concatenación y f-strings |
| `04-metodos-strings.py` | Métodos de string (`upper`, `strip`, `find`, `replace`, `in`) |
| `05-secuencias-escape.py` | Secuencias de escape (`\n`) |
| `06-numeros.py` | Módulo `math` y operaciones numéricas |
| `07-multiplicadora.py` | Suma/resta/multiplicación/división con `input` |
| `08-conversion-tipos.py` | Conversión de tipos y `bool()` |
| `09-conversor.py` | Mini programa: conversor Celsius/Fahrenheit |
| `10-listas.py` | Listas: indexado y asignación |
| `11-listas-metodos.py` | Métodos de listas (`insert`, `remove`, `in`) |
| `while.py` | Bucle `while` con cláusula `else` |
| `datos.py` / `format.py` / `intro.py` | Ejercicios sueltos de variables, f-strings y precedencia de operadores |

## Mini-proyectos

| Archivo | Descripción |
|---|---|
| `adivinar.py` | Juego de adivinar un número (`random.randint`) |
| `piedrapapel.py` | Piedra, papel o tijera contra la computadora |
| `calcularArea.py` | Funciones para el área de círculo, rectángulo, triángulo, cuadrado, trapecio, elipse, sector circular, paralelogramo y rombo |
| `calcularPerimetro.py` | Clases para el perímetro de cuadrado, rectángulo, triángulo, círculo y trapecio |
| `13_modelos.py` | Ejemplo de import de un módulo propio (`calcularArea`) |
| `54_pruebamodulos.py` | Uso puntual de `math.sqrt` |
| `gen.py` / `sec_psw.py` | Generadores de contraseñas aleatorias (`random` + `string`) |
| `sec_enc.py` | Hash de contraseña con `scrypt` (salt aleatorio) |
| `inventario.csv` | Datos de ejemplo (producto, precio, stock) |

## Experimento API (FastAPI)

- `main.py`: endpoint `/estado_actual` que devuelve hora local de Tucumán y
  datos de clima hardcodeados.
- `lanzador.py`: busca un puerto libre entre `[8600, 8700, 8800, 8900]` y
  levanta `uvicorn main:app` con `--ssl-keyfile=key.pem --ssl-certfile=cert.pem`.
  Esos certificados no están en el repo (ver nota de seguridad) y hay que
  generarlos localmente para que el lanzador funcione.
- `Untitled-1.py`: notas de instalación (`fastapi`, `uvicorn`) y el comando
  para levantar el servidor manualmente.

## Nota de seguridad

El `.gitignore` ignora `*.pem`, `*.key` y `.env` porque se purgaron claves
reales del historial del repo (commit `b3abfd1`). Si esas credenciales
estuvieron expuestas en algún momento, deben considerarse comprometidas y
rotarse; purgar el historial de git no revoca una clave ya filtrada.
