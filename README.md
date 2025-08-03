# IOL MCP Server

Servidor MCP (Model-Controller-Proxy) para la API de InvertirOnline (IOL).

## Descripción

Este proyecto implementa un servidor MCP que actúa como intermediario entre el cliente y la API de InvertirOnline. Proporciona una interfaz simplificada y estructurada para acceder a las funcionalidades de la API.

## Características

- Autenticación automática con manejo de tokens
- Endpoints para consulta de portafolio
- Endpoints para consulta de títulos y cotizaciones
- Manejo de errores y reintentos
- Logging detallado
- Soporte para Docker y Docker Compose
- Hot-reload para desarrollo

## Requisitos

- Python 3.11+
- FastMCP >= 2.10.6
- Docker y Docker Compose (opcional)
- Cuenta de InvertirOnline

## Instalación

### Usando Docker (Recomendado)

1. Clonar el repositorio:
```bash
git clone <repository_url>
cd iol-mcp
```

2. Copiar el archivo de ejemplo de variables de entorno:
```bash
cp .env.example .env
```

3. Editar el archivo `.env` con tus credenciales:
```env
IOL_USERNAME=tu_usuario
IOL_PASSWORD=tu_contraseña
```

4. Iniciar los servicios con Docker Compose:
```bash
# Iniciar todos los servicios
docker-compose up -d

# O iniciar solo el servidor principal
docker-compose up -d iol-mcp

# O iniciar solo el servidor SSE (para desarrollo)
docker-compose up -d iol-mcp-sse
```

### Instalación Manual

1. Clonar el repositorio:
```bash
git clone <repository_url>
cd iol-mcp
```

2. Asegurarse de tener Python 3.11 o superior:
```bash
python --version
# Debe mostrar Python 3.11.x o superior
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

5. Iniciar el servidor:
```bash
# Servidor principal
./start-server.sh

# O servidor SSE (para desarrollo)
./start-server-sse.sh
```

## Uso de Docker Compose

El proyecto incluye dos servicios en Docker Compose:

1. **iol-mcp** (Puerto 8000):
   - Servidor principal
   - Sin hot-reload
   - Para producción

2. **iol-mcp-sse** (Puerto 8001):
   - Servidor con hot-reload
   - Para desarrollo
   - Actualiza automáticamente al modificar el código

### Comandos Útiles

```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Reiniciar servicios
docker-compose restart

# Detener servicios
docker-compose down

# Reconstruir imágenes
docker-compose build

# Ver estado de los servicios
docker-compose ps
```

## Endpoints Disponibles

### Portafolio

- `obtener_portafolio`: Obtiene el portafolio del usuario
  - Parámetros:
    - `pais` (opcional): Filtrar por país

- `obtener_operaciones`: Obtiene las operaciones del usuario
  - Parámetros:
    - `filtro` (opcional): Tipo de operación
    - `pais` (opcional): País de la operación
    - `estado` (opcional): Estado de la operación
    - `fecha_desde` (opcional): Fecha desde (YYYY-MM-DD)
    - `fecha_hasta` (opcional): Fecha hasta (YYYY-MM-DD)
    - `numero` (opcional): Número de operación

### Títulos

- `obtener_cotizacion`: Obtiene la cotización de un título
  - Parámetros:
    - `simbolo`: Símbolo del título
    - `mercado`: Mercado del título
    - `plazo` (opcional): Plazo de la cotización

- `obtener_panel`: Obtiene el panel de un instrumento
  - Parámetros:
    - `instrumento`: Tipo de instrumento
    - `panel`: Tipo de panel
    - `pais`: País del panel

- `obtener_opciones`: Obtiene las opciones de un título
  - Parámetros:
    - `simbolo`: Símbolo del título
    - `mercado`: Mercado del título

- `obtener_puntas`: Obtiene las puntas de un título
  - Parámetros:
    - `simbolo`: Símbolo del título
    - `mercado`: Mercado del título
    - `plazo` (opcional): Plazo de la cotización

## Contribuir

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. 