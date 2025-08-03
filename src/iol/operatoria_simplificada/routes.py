from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import OperatoriaSimplificadaClient

class OperatoriaSimplificadaConfig(BaseModel):
    operatoria_simplificada: bool = Field(description="Estado de la operatoria simplificada")

    model_config = ConfigDict(extra="ignore", validate_assignment=True)

    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class OperatoriaSimplificadaRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = OperatoriaSimplificadaClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_operatoria_simplificada",
            description="Obtener configuración de operatoria simplificada",
            tags=["operatoria_simplificada", "consulta"]
        )
        async def obtener_operatoria_simplificada() -> Dict[str, Any]:
            """Obtiene la configuración de operatoria simplificada"""
            try:
                result = await self.client.obtener_operatoria_simplificada()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo operatoria simplificada: {str(e)}"}

        @mcp.tool(
            name="actualizar_operatoria_simplificada",
            description="Actualizar configuración de operatoria simplificada",
            tags=["operatoria_simplificada", "actualizar"]
        )
        async def actualizar_operatoria_simplificada(
            config: OperatoriaSimplificadaConfig = Field(
                description="Configuración de operatoria simplificada",
                example={
                    "operatoria_simplificada": True
                }
            )
        ) -> Dict[str, Any]:
            """
            Actualiza la configuración de operatoria simplificada
            
            Args:
                config: Configuración de operatoria simplificada
            """
            try:
                result = await self.client.actualizar_operatoria_simplificada(
                    operatoria_simplificada=config.operatoria_simplificada
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando operatoria simplificada: {str(e)}"} 