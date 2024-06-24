# Generador de Contraseñas con Python

Para utilizar el generador de contraseñas, puedes ejecutarlo de la siguiente manera:

```bash
python3 pass_gen.py
```

O puedes ejecutar el binario ubicado en la carpeta `dist`, compilado específicamente para Linux. Puedes compilarlo para tu sistema operativo utilizando [PyInstaller](https://pyinstaller.org/en/stable/index.html).

```bash
./pass_gen
```
Por defecto se utilizan todas las opciones de caracteres (numeros, letras y caracteres especiales) y una longitud de 30 caracteres. Esto puede cambiarse con los argumentos
## Argumentos

El generador acepta dos argumentos. El primer argumento especifica qué tipo de caracteres se utilizarán en la contraseña. Por defecto, se utilizan todos los tipos disponibles (números, letras minúsculas y mayúsculas). El segundo argumento indica la longitud de la contraseña.

El primer argumento tiene la siguiente sintaxis:

```bash
python3 pass_gen.py -lne
# Esta es la configuración por defecto
```

- El parámetro `-l` incluye letras.
- El parámetro `-n` incluye números.
- El parámetro `-e` incluye caracteres especiales.

Los parámetros deben combinarse. Por ejemplo, si deseas una contraseña solo con letras y números, debes ejecutar:

```bash
python3 pass_gen.py -ln
```

Si solo quieres letras, ejecuta:

```bash
python3 pass_gen.py -l
```

Si solo quieres números, ejecuta:

```bash
python3 pass_gen.py -n
```

Para especificar la longitud de la contraseña, puedes hacerlo de la siguiente manera:

```bash
python3 pass_gen.py -lne 20
# Genera una contraseña con todas las opciones y de 20 caracteres
```

Si solo especificas la longitud sin opciones de caracteres, se utilizarán todas las opciones por defecto:

```bash
python3 pass_gen.py 20
# Genera una contraseña con todas las opciones y de 20 caracteres
```

Por defecto, el número de caracteres es 30.

### Copiar al portapapeles

Cuando se genera una contraseña, también se copia automáticamente al portapapeles. Esta funcionalidad está disponible solo en Linux y macOS.

### Propósito

Esto fue hecho como estudio para mis clases de la universidad. Espero que sea útil.
