from typing import Dict, Any
from fastmcp import FastMCP

class BaseRoutes:
    """Clase base para todas las rutas de la API"""
    
    def __init__(self):
        """Inicializa la clase base de rutas"""
        self.client = None

    def register_tools(self, mcp: FastMCP) -> None:
        """
        Registra las herramientas FastMCP. Debe ser implementado por las clases hijas.
        
        Args:
            mcp: Instancia de FastMCP
        """
        raise NotImplementedError("Las clases hijas deben implementar register_tools")

    def get_auth_headers(self) -> Dict[str, str]:
        """
        Obtiene los headers de autenticación.
        
        Returns:
            Dict[str, str]: Headers de autenticación
        """
        if not self.client:
            raise ValueError("Cliente no inicializado")
        return self.client.get_auth_headers() 