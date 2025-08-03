from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import NotificacionClient

class NotificacionRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = NotificacionClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="notificacion_obtener_notificaciones",  # Prefijo para evitar duplicados
            description="Obtener notificaciones del usuario",
            tags=["notificacion", "consulta"]
        )
        async def obtener_notificaciones(
            fecha_desde: Optional[str] = Field(default=None, description="Fecha desde (YYYY-MM-DD)"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha hasta (YYYY-MM-DD)")
        ) -> Dict[str, Any]:
            """
            Obtiene las notificaciones del usuario
            
            Args:
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_notificaciones(
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo notificaciones: {str(e)}"}

        @mcp.tool(
            name="marcar_notificacion_leida",
            description="Marcar notificación como leída",
            tags=["notificacion", "actualizar"]
        )
        async def marcar_notificacion_leida(
            id_notificacion: int = Field(description="ID de la notificación")
        ) -> Dict[str, Any]:
            """
            Marca una notificación como leída
            
            Args:
                id_notificacion: ID de la notificación
            """
            try:
                result = await self.client.marcar_notificacion_leida(id_notificacion)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error marcando notificación como leída: {str(e)}"} 