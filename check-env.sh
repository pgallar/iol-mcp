#!/bin/bash

# Verificar variables de entorno requeridas
required_vars=(
    "IOL_USERNAME"
    "IOL_PASSWORD"
)

missing_vars=()

for var in "${required_vars[@]}"; do
    if [[ -z "${!var}" ]]; then
        missing_vars+=("$var")
    fi
done

if [[ ${#missing_vars[@]} -ne 0 ]]; then
    echo "Error: Las siguientes variables de entorno son requeridas pero no están definidas:"
    printf '%s\n' "${missing_vars[@]}"
    exit 1
fi

echo "✅ Todas las variables de entorno requeridas están definidas"
exit 0 