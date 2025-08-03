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
            name="obtener_portafolio",
            description="Obtener portafolio del usuario",
            tags=["portafolio"]
        )
        async def obtener_portafolio(
            pais: Optional[str] = Field(default=None, description="País del portafolio (argentina, estados_unidos, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene el portafolio del usuario
            
            Args:
                pais: País del portafolio (argentina, estados_unidos, etc)
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
            description="Obtener operaciones del usuario",
            tags=["portafolio", "operaciones"]
        )
        async def obtener_operaciones(
            pais: Optional[str] = Field(default=None, description="País de las operaciones (argentina, estados_unidos, etc)"),
            estado: Optional[str] = Field(default=None, description="Estado de las operaciones (todas, pendientes, terminadas, canceladas)"),
            fecha_desde: Optional[str] = Field(default=None, description="Fecha de inicio en formato YYYY-MM-DD"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha de fin en formato YYYY-MM-DD")
        ) -> Dict[str, Any]:
            """
            Obtiene las operaciones del usuario
            
            Args:
                pais: País de las operaciones (argentina, estados_unidos, etc)
                estado: Estado de las operaciones (todas, pendientes, terminadas, canceladas)
                fecha_desde: Fecha de inicio en formato YYYY-MM-DD
                fecha_hasta: Fecha de fin en formato YYYY-MM-DD
            """
            try:
                result = await self.client.obtener_operaciones(
                    pais=pais,
                    estado=estado,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo operaciones: {str(e)}"}
                
        @mcp.tool(
            name="obtener_portafolio_valorizado",
            description="Obtener portafolio valorizado del usuario",
            tags=["portafolio", "valorizado"]
        )
        async def obtener_portafolio_valorizado(
            pais: Optional[str] = Field(default=None, description="País del portafolio (argentina, estados_unidos, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene el portafolio valorizado del usuario
            
            Args:
                pais: País del portafolio (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_portafolio_valorizado(pais=pais)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo portafolio valorizado: {str(e)}"}
                
        @mcp.tool(
            name="obtener_rendimiento_historico",
            description="Obtener rendimiento histórico del portafolio",
            tags=["portafolio", "rendimiento"]
        )
        async def obtener_rendimiento_historico(
            pais: Optional[str] = Field(default=None, description="País del portafolio (argentina, estados_unidos, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene el rendimiento histórico del portafolio
            
            Args:
                pais: País del portafolio (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_rendimiento_historico(pais=pais)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo rendimiento histórico: {str(e)}"}
                
        @mcp.tool(
            name="obtener_composicion_portafolio",
            description="Obtener composición del portafolio por tipo de instrumento",
            tags=["portafolio", "composicion"]
        )
        async def obtener_composicion_portafolio(
            pais: Optional[str] = Field(default=None, description="País del portafolio (argentina, estados_unidos, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene la composición del portafolio por tipo de instrumento
            
            Args:
                pais: País del portafolio (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_composicion_portafolio(pais=pais)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo composición del portafolio: {str(e)}"} 