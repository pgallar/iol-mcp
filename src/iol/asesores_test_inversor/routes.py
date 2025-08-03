from typing import Dict, Any, Optional, List
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import AsesoresTestInversorClient

class RespuestaTestInversor(BaseModel):
    pregunta_id: int = Field(description="ID de la pregunta")
    respuesta_id: int = Field(description="ID de la respuesta seleccionada")

    model_config = ConfigDict(extra="ignore", validate_assignment=True)

    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class AsesoresTestInversorRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = AsesoresTestInversorClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="asesores_obtener_test_inversor",  # Prefijo para evitar duplicados
            description="Obtener test de inversor de un cliente",
            tags=["asesores", "test_inversor"]
        )
        async def obtener_test_inversor(
            id_cliente: int
        ) -> Dict[str, Any]:
            """
            Obtiene el test de inversor de un cliente
            
            Args:
                id_cliente: ID del cliente
            """
            try:
                result = await self.client.obtener_test_inversor(id_cliente)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo test de inversor: {str(e)}"}

        @mcp.tool(
            name="obtener_preguntas_test",
            description="Obtener preguntas del test de inversor",
            tags=["asesores", "test_inversor"]
        )
        async def obtener_preguntas() -> Dict[str, Any]:
            """Obtiene las preguntas del test de inversor"""
            try:
                result = await self.client.obtener_preguntas()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo preguntas: {str(e)}"}

        @mcp.tool(
            name="asesores_guardar_test_inversor",  # Prefijo para evitar duplicados
            description="Guardar respuestas del test de inversor",
            tags=["asesores", "test_inversor"]
        )
        async def guardar_test_inversor(
            id_cliente: int,
            respuestas: List[RespuestaTestInversor] = Field(
                description="Lista de respuestas del test",
                example=[
                    {"pregunta_id": 1, "respuesta_id": 2},
                    {"pregunta_id": 2, "respuesta_id": 1}
                ]
            )
        ) -> Dict[str, Any]:
            """
            Guarda las respuestas del test de inversor de un cliente
            
            Args:
                id_cliente: ID del cliente
                respuestas: Lista de respuestas del test
            """
            try:
                # Convertir las respuestas al formato esperado por la API
                respuestas_api = [resp.model_dump() for resp in respuestas]
                result = await self.client.guardar_test_inversor(
                    id_cliente=id_cliente,
                    respuestas=respuestas_api
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error guardando test de inversor: {str(e)}"} 