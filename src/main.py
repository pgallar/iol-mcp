import os
import logging
import sys
import asyncio
from typing import Dict, Any, Tuple
from fastmcp import FastMCP
from dotenv import load_dotenv

# Importar rutas
from iol.portafolio.routes import PortafolioRoutes
from iol.titulos.routes import TitulosRoutes
from iol.mi_cuenta.routes import MiCuentaRoutes
from iol.notificacion.routes import NotificacionRoutes
from iol.operar.routes import OperarRoutes
from iol.perfil.routes import PerfilRoutes

def setup_logging() -> None:
    """Configura el sistema de logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('iol_mcp.log')
        ]
    )

def get_credentials() -> tuple:
    """Obtiene las credenciales desde variables de entorno"""
    load_dotenv()
    username = os.getenv('IOL_USERNAME')
    password = os.getenv('IOL_PASSWORD')
    
    if not username or not password:
        raise ValueError("IOL_USERNAME y IOL_PASSWORD son requeridas")
        
    return username, password

def get_server_config() -> Dict[str, Any]:
    """Obtiene la configuración del servidor"""
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '8001'))  # Puerto por defecto para SSE
    
    return {
        'host': host,
        'port': port
    }

def create_mcp_server() -> FastMCP:
    """Crea y configura el servidor MCP"""
    try:
        mcp = FastMCP("iol")
        return mcp
    except Exception as e:
        logging.getLogger(__name__).critical(f"Error creando servidor MCP: {str(e)}")
        raise

def register_routers(mcp: FastMCP) -> None:
    """Registra las rutas en el servidor MCP"""
    logger = logging.getLogger(__name__)
    routers = [
        PortafolioRoutes(),
        TitulosRoutes(),
        MiCuentaRoutes(),
        NotificacionRoutes(),
        OperarRoutes(),
        PerfilRoutes()
    ]
    
    for router in routers:
        try:
            router.register_tools(mcp)
            logger.debug(f"Router registrado: {router.__class__.__name__}")
        except Exception as e:
            logger.error(f"Error registrando router {router.__class__.__name__}: {str(e)}")
            raise

async def run_sse_server(mcp: FastMCP, host: str, port: int) -> None:
    """Ejecuta el servidor SSE"""
    logger = logging.getLogger(__name__)
    logger.info(f"Iniciando servidor SSE en {host}:{port}")
    
    # Agregar un delay para asegurar que el servidor esté completamente inicializado
    await asyncio.sleep(1)
    logger.info("Inicialización del servidor completa, listo para aceptar conexiones")
    
    await mcp.run_async(transport="sse", host=host, port=port)

def main() -> None:
    """Función principal"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Inicializando servidor IOL MCP con SSE...")
        
        # Obtener credenciales y configuración
        username, password = get_credentials()
        config = get_server_config()
        
        logger.info("Credenciales cargadas exitosamente")
        logger.info(f"Configuración del servidor SSE: {config}")
        
        mcp = create_mcp_server()
        
        logger.info("Registrando routers...")
        register_routers(mcp)
        logger.info("Todos los routers registrados exitosamente")
        
        # Ejecutar servidor SSE
        logger.info(f"Iniciando servidor SSE en el puerto {config['port']}...")
        asyncio.run(run_sse_server(mcp, config['host'], config['port']))
            
    except Exception as e:
        logger.critical(f"Error fatal: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 