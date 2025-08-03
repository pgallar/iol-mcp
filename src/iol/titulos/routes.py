from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import TitulosClient

class TitulosRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = TitulosClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="titulos_obtener_cotizacion",  # Prefijo para evitar duplicados
            description="Obtener cotización de un título",
            tags=["titulos", "cotizacion"]
        )
        async def obtener_cotizacion(
            simbolo: str,
            mercado: str,
            plazo: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene la cotización de un título
            
            Args:
                simbolo: Símbolo del título
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
                plazo: Plazo de la cotización (t0, t1, t2)
            """
            try:
                result = await self.client.obtener_cotizacion(
                    simbolo=simbolo,
                    mercado=mercado,
                    plazo=plazo
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo cotización: {str(e)}"}

        @mcp.tool(
            name="obtener_panel",
            description="Obtener panel de instrumentos",
            tags=["titulos", "panel"]
        )
        async def obtener_panel(
            instrumento: str,
            panel: str,
            pais: str
        ) -> Dict[str, Any]:
            """
            Obtiene el panel de un instrumento
            
            Args:
                instrumento: Tipo de instrumento (Acciones, Bonos, etc)
                panel: Tipo de panel (Líderes, General, etc)
                pais: País del panel (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_panel(
                    instrumento=instrumento,
                    panel=panel,
                    pais=pais
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo panel: {str(e)}"}

        @mcp.tool(
            name="obtener_opciones",
            description="Obtener opciones de un título",
            tags=["titulos", "opciones"]
        )
        async def obtener_opciones(
            simbolo: str,
            mercado: str
        ) -> Dict[str, Any]:
            """
            Obtiene las opciones de un título
            
            Args:
                simbolo: Símbolo del título
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
            """
            try:
                result = await self.client.obtener_opciones(
                    simbolo=simbolo,
                    mercado=mercado
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo opciones: {str(e)}"}

        @mcp.tool(
            name="obtener_puntas",
            description="Obtener puntas de un título",
            tags=["titulos", "puntas"]
        )
        async def obtener_puntas(
            simbolo: str,
            mercado: str,
            plazo: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene las puntas de un título
            
            Args:
                simbolo: Símbolo del título
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
                plazo: Plazo de la cotización (t0, t1, t2)
            """
            try:
                result = await self.client.obtener_puntas(
                    simbolo=simbolo,
                    mercado=mercado,
                    plazo=plazo
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo puntas: {str(e)}"} 