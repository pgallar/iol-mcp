from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, validator
from ..base_routes import BaseRoutes
from .client import AsesoresClient

class AsesoresRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = AsesoresClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_asesores",
            description="Obtener listado de asesores",
            tags=["asesores", "consulta"]
        )
        async def obtener_asesores() -> Dict[str, Any]:
            """Obtiene el listado de asesores disponibles"""
            try:
                result = await self.client.obtener_asesores()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo asesores: {str(e)}"}

        @mcp.tool(
            name="obtener_asesor",
            description="Obtener información de un asesor específico",
            tags=["asesores", "consulta"]
        )
        async def obtener_asesor(
            id_asesor: int
        ) -> Dict[str, Any]:
            """Obtiene la información de un asesor específico"""
            try:
                result = await self.client.obtener_asesor(id_asesor)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo asesor: {str(e)}"}

        @mcp.tool(
            name="obtener_clientes_asesor",
            description="Obtener listado de clientes del asesor",
            tags=["asesores", "clientes"]
        )
        async def obtener_clientes_asesor() -> Dict[str, Any]:
            """Obtiene el listado de clientes del asesor"""
            try:
                result = await self.client.obtener_clientes_asesor()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo clientes: {str(e)}"}

        @mcp.tool(
            name="obtener_cliente_asesor",
            description="Obtener información de un cliente específico",
            tags=["asesores", "clientes"]
        )
        async def obtener_cliente_asesor(
            id_cliente: int
        ) -> Dict[str, Any]:
            """Obtiene la información de un cliente específico del asesor"""
            try:
                result = await self.client.obtener_cliente_asesor(id_cliente)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo cliente: {str(e)}"}

        @mcp.tool(
            name="obtener_operaciones_cliente",
            description="Obtener operaciones de un cliente",
            tags=["asesores", "operaciones"]
        )
        async def obtener_operaciones_cliente(
            id_cliente: int,
            fecha_desde: Optional[str] = None,
            fecha_hasta: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene las operaciones de un cliente específico
            
            Args:
                id_cliente: ID del cliente
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_operaciones_cliente(
                    id_cliente=id_cliente,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo operaciones: {str(e)}"} 