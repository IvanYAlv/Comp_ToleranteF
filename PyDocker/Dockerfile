FROM alpine:3.10

# Instalar python y pip en la imagen.
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

# Crear directorio de trabajo. 
WORKDIR /ex_d

# Copiar contenido de la carpeta al directorio.
COPY . /ex_d

# Modulos requeridos para el funcionamiento del script (varia).
RUN pip3 --no-cache-dir install -r requirements.txt 

CMD ["python3", "src/ex.py"]