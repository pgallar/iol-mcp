#!/bin/bash

# Verificar variables de entorno
./check-env.sh
if [[ $? -ne 0 ]]; then
    exit 1
fi

# Crear directorio de logs si no existe
mkdir -p logs

# Establecer variables de entorno para SSE
export RELOAD=true

# Iniciar el servidor
python src/main.py 