from typing import Dict, Any, Optional, List
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import PerfilClient

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

class PerfilRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = PerfilClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_perfil",
            description="Obtener perfil del usuario",
            tags=["perfil", "consulta"]
        )
        async def obtener_perfil() -> Dict[str, Any]:
            """Obtiene el perfil del usuario"""
            try:
                result = await self.client.obtener_perfil()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo perfil: {str(e)}"}

        @mcp.tool(
            name="obtener_test_inversor",
            description="Obtener test de inversor del usuario",
            tags=["perfil", "test_inversor"]
        )
        async def obtener_test_inversor() -> Dict[str, Any]:
            """Obtiene el test de inversor del usuario"""
            try:
                result = await self.client.obtener_test_inversor()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo test de inversor: {str(e)}"}

        @mcp.tool(
            name="guardar_test_inversor",
            description="Guardar respuestas del test de inversor",
            tags=["perfil", "test_inversor"]
        )
        async def guardar_test_inversor(
            respuestas: List[Dict[str, Any]] = Field(
                description="Lista de respuestas del test",
                example=[
                    {"pregunta_id": 1, "respuesta_id": 2},
                    {"pregunta_id": 2, "respuesta_id": 1}
                ],
                items={
                    "type": "object",
                    "properties": {
                        "pregunta_id": {"type": "integer", "description": "ID de la pregunta"},
                        "respuesta_id": {"type": "integer", "description": "ID de la respuesta seleccionada"}
                    },
                    "required": ["pregunta_id", "respuesta_id"]
                }
            )
        ) -> Dict[str, Any]:
            """
            Guarda las respuestas del test de inversor
            
            Args:
                respuestas: Lista de respuestas del test
            """
            try:
                result = await self.client.guardar_test_inversor(respuestas=respuestas)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error guardando test de inversor: {str(e)}"}

        @mcp.tool(
            name="obtener_preguntas_test_inversor",
            description="Obtener preguntas del test de inversor",
            tags=["perfil", "test_inversor"]
        )
        async def obtener_preguntas_test_inversor() -> Dict[str, Any]:
            """Obtiene las preguntas del test de inversor"""
            try:
                result = await self.client.obtener_preguntas_test_inversor()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo preguntas del test de inversor: {str(e)}"}
                
        @mcp.tool(
            name="actualizar_perfil",
            description="Actualizar perfil del usuario",
            tags=["perfil", "actualizar"]
        )
        async def actualizar_perfil(
            datos_perfil: Dict[str, Any] = Field(
                description="Datos del perfil a actualizar",
                example={
                    "nombre": "Juan",
                    "apellido": "Perez",
                    "email": "juan.perez@example.com",
                    "telefono": "1122334455"
                }
            )
        ) -> Dict[str, Any]:
            """
            Actualiza el perfil del usuario
            
            Args:
                datos_perfil: Datos del perfil a actualizar
            """
            try:
                result = await self.client.actualizar_perfil(datos_perfil=datos_perfil)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando perfil: {str(e)}"}
                
        @mcp.tool(
            name="cambiar_clave",
            description="Cambiar clave del usuario",
            tags=["perfil", "clave"]
        )
        async def cambiar_clave(
            clave_actual: str = Field(description="Clave actual"),
            clave_nueva: str = Field(description="Nueva clave")
        ) -> Dict[str, Any]:
            """
            Cambia la clave del usuario
            
            Args:
                clave_actual: Clave actual
                clave_nueva: Nueva clave
            """
            try:
                result = await self.client.cambiar_clave(
                    clave_actual=clave_actual,
                    clave_nueva=clave_nueva
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error cambiando clave: {str(e)}"} 