# Imagen base mínima recomendada
FROM python:3.12-slim

# Directorio de trabajo
WORKDIR /app

# Copiar las dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente completo
COPY . .

# Permisos
RUN chmod -R 755 /app

# Comando para ejecutar tu app
CMD ["python", "P1.3_Tienda_online/main.py"]
