# Usa una imagen base de Python
FROM python:3.9-slim

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . .

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
