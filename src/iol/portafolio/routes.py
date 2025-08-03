from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import PortafolioClient

class PortafolioRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = PortafolioClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="portafolio_obtener_portafolio",  # Prefijo para evitar duplicados
            description="Obtener portafolio",
            tags=["portafolio", "consulta"]
        )
        async def obtener_portafolio(
            pais: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene el portafolio del usuario
            
            Args:
                pais: Filtrar por país (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_portafolio(pais=pais)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo portafolio: {str(e)}"}

        @mcp.tool(
            name="obtener_operaciones",
            description="Obtener operaciones",
            tags=["portafolio", "operaciones"]
        )
        async def obtener_operaciones(
            filtro: Optional[str] = None,
            pais: Optional[str] = None,
            estado: Optional[str] = None,
            fecha_desde: Optional[str] = None,
            fecha_hasta: Optional[str] = None,
            numero: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene las operaciones del usuario
            
            Args:
                filtro: Tipo de operación (Compra, Venta, etc)
                pais: País de la operación
                estado: Estado de la operación (pendiente, terminada, etc)
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
                numero: Número de operación
            """
            try:
                result = await self.client.obtener_operaciones(
                    filtro=filtro,
                    pais=pais,
                    estado=estado,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta,
                    numero=numero
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo operaciones: {str(e)}"}

        # No es necesario llamar a mcp.add_tool ya que el decorador @mcp.tool lo hace automáticamente 