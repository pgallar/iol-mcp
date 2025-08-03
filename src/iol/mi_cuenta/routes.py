from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import MiCuentaClient

class MiCuentaRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = MiCuentaClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="mi_cuenta_obtener_estado",  # Prefijo para evitar duplicados
            description="Obtener estado de cuenta",
            tags=["mi_cuenta", "consulta"]
        )
        async def obtener_estado_cuenta() -> Dict[str, Any]:
            """Obtiene el estado de cuenta del usuario"""
            try:
                result = await self.client.obtener_estado_cuenta()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo estado de cuenta: {str(e)}"}

        @mcp.tool(
            name="obtener_saldos",
            description="Obtener saldos de la cuenta",
            tags=["mi_cuenta", "consulta"]
        )
        async def obtener_saldos() -> Dict[str, Any]:
            """Obtiene los saldos de la cuenta"""
            try:
                result = await self.client.obtener_saldos()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo saldos: {str(e)}"}

        @mcp.tool(
            name="obtener_movimientos",
            description="Obtener movimientos de la cuenta",
            tags=["mi_cuenta", "movimientos"]
        )
        async def obtener_movimientos(
            fecha_desde: Optional[str] = Field(default=None, description="Fecha desde (YYYY-MM-DD)"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha hasta (YYYY-MM-DD)")
        ) -> Dict[str, Any]:
            """
            Obtiene los movimientos de la cuenta
            
            Args:
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_movimientos(
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo movimientos: {str(e)}"}

        @mcp.tool(
            name="obtener_movimientos_fondos",
            description="Obtener movimientos de fondos",
            tags=["mi_cuenta", "movimientos", "fondos"]
        )
        async def obtener_movimientos_fondos(
            fecha_desde: Optional[str] = Field(default=None, description="Fecha desde (YYYY-MM-DD)"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha hasta (YYYY-MM-DD)")
        ) -> Dict[str, Any]:
            """
            Obtiene los movimientos de fondos
            
            Args:
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_movimientos_fondos(
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo movimientos de fondos: {str(e)}"}

        @mcp.tool(
            name="obtener_movimientos_fci",
            description="Obtener movimientos de FCI",
            tags=["mi_cuenta", "movimientos", "fci"]
        )
        async def obtener_movimientos_fci(
            fecha_desde: Optional[str] = Field(default=None, description="Fecha desde (YYYY-MM-DD)"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha hasta (YYYY-MM-DD)")
        ) -> Dict[str, Any]:
            """
            Obtiene los movimientos de FCI
            
            Args:
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_movimientos_fci(
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo movimientos de FCI: {str(e)}"} 