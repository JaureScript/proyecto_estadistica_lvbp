# 1. Usamos una imagen oficial de Python
FROM python:3.9

# 2. Creamos un directorio de trabajo dentro del servidor
WORKDIR /code

# 3. Copiamos el archivo de librerías primero para que la instalación sea rápida
COPY ./requirements.txt /code/requirements.txt

# 4. Instalamos las librerías necesarias (pandas, streamlit, etc.)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 5. Copiamos el resto de tus archivos (app.py y el .csv de la LVBP)
COPY . .

# 6. Ejecutamos Streamlit en el puerto que usa Hugging Face (7860)
CMD ["streamlit", "run", "app.py", "--server.port", "7860", "--server.address", "0.0.0.0"]