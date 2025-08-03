from typing import Dict, Any, Optional, List
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import PerfilClient

class PerfilClienteModel(BaseModel):
    """Modelo para representar el perfil del cliente según el swagger"""
    # Aquí se definirían los campos específicos de PerfilClienteModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class PerfilRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = PerfilClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_datos_perfil",
            description="Obtener datos del perfil del cliente",
            tags=["perfil", "consulta"]
        )
        async def obtener_datos_perfil() -> Dict[str, Any]:
            """
            Obtiene los datos del perfil del cliente
            """
            try:
                result = await self.client.obtener_datos_perfil()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo datos del perfil: {str(e)}"} 