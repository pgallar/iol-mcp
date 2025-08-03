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
            simbolo: str = Field(description="Símbolo del título"),
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)"),
            plazo: Optional[str] = Field(default=None, description="Plazo de la cotización (t0, t1, t2)")
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
            instrumento: str = Field(description="Tipo de instrumento (Acciones, Bonos, Opciones, etc)"),
            pais: str = Field(description="País del panel (argentina, estados_unidos, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene el panel de un instrumento
            
            Args:
                instrumento: Tipo de instrumento (Acciones, Bonos, Opciones, etc)
                pais: País del panel (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_panel(
                    instrumento=instrumento,
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
            simbolo: str = Field(description="Símbolo del título"),
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)")
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
            simbolo: str = Field(description="Símbolo del título"),
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)"),
            plazo: Optional[str] = Field(default=None, description="Plazo de la cotización (t0, t1, t2)")
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
                
        @mcp.tool(
            name="obtener_datos_historicos",
            description="Obtener datos históricos de un título",
            tags=["titulos", "historico"]
        )
        async def obtener_datos_historicos(
            simbolo: str = Field(description="Símbolo del título"),
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)"),
            desde: str = Field(description="Fecha de inicio en formato YYYY-MM-DD"),
            hasta: str = Field(description="Fecha de fin en formato YYYY-MM-DD"),
            ajustado: bool = Field(default=True, description="Indica si los datos deben estar ajustados por dividendos")
        ) -> Dict[str, Any]:
            """
            Obtiene los datos históricos de un título
            
            Args:
                simbolo: Símbolo del título
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
                desde: Fecha de inicio en formato YYYY-MM-DD
                hasta: Fecha de fin en formato YYYY-MM-DD
                ajustado: Indica si los datos deben estar ajustados por dividendos
            """
            try:
                result = await self.client.obtener_datos_historicos(
                    simbolo=simbolo,
                    mercado=mercado,
                    desde=desde,
                    hasta=hasta,
                    ajustado=ajustado
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo datos históricos: {str(e)}"}
                
        @mcp.tool(
            name="buscar_titulos",
            description="Buscar títulos por nombre o símbolo",
            tags=["titulos", "busqueda"]
        )
        async def buscar_titulos(
            filtro: str = Field(description="Texto a buscar"),
            mercado: Optional[str] = Field(default=None, description="Mercado del título (bcba, nyse, nasdaq, etc)")
        ) -> Dict[str, Any]:
            """
            Busca títulos por nombre o símbolo
            
            Args:
                filtro: Texto a buscar
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
            """
            try:
                result = await self.client.buscar_titulos(
                    filtro=filtro,
                    mercado=mercado
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error buscando títulos: {str(e)}"}
                
        @mcp.tool(
            name="obtener_detalle_titulo",
            description="Obtener información detallada de un título",
            tags=["titulos", "detalle"]
        )
        async def obtener_detalle_titulo(
            simbolo: str = Field(description="Símbolo del título"),
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene información detallada de un título
            
            Args:
                simbolo: Símbolo del título
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
            """
            try:
                result = await self.client.obtener_detalle_titulo(
                    simbolo=simbolo,
                    mercado=mercado
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo detalle del título: {str(e)}"}

        @mcp.tool(
            name="obtener_instrumentos",
            description="Obtener instrumentos disponibles para un país",
            tags=["titulos", "instrumentos"]
        )
        async def obtener_instrumentos(
            pais: str = Field(description="País (argentina, estados_unidos, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene los instrumentos disponibles para un país
            
            Args:
                pais: País (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_instrumentos(pais=pais)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo instrumentos: {str(e)}"}

        @mcp.tool(
            name="obtener_fci",
            description="Obtener información de fondos comunes de inversión",
            tags=["titulos", "fci"]
        )
        async def obtener_fci(
            simbolo: Optional[str] = Field(default=None, description="Símbolo del FCI (opcional)")
        ) -> Dict[str, Any]:
            """
            Obtiene información de fondos comunes de inversión
            
            Args:
                simbolo: Símbolo del FCI (opcional)
            """
            try:
                result = await self.client.obtener_fci(simbolo=simbolo)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo información de FCI: {str(e)}"}

        @mcp.tool(
            name="obtener_tipos_fondos",
            description="Obtener tipos de fondos disponibles",
            tags=["titulos", "fci"]
        )
        async def obtener_tipos_fondos() -> Dict[str, Any]:
            """
            Obtiene los tipos de fondos disponibles
            """
            try:
                result = await self.client.obtener_tipos_fondos()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo tipos de fondos: {str(e)}"}

        @mcp.tool(
            name="obtener_administradoras",
            description="Obtener administradoras de fondos",
            tags=["titulos", "fci"]
        )
        async def obtener_administradoras() -> Dict[str, Any]:
            """
            Obtiene las administradoras de fondos
            """
            try:
                result = await self.client.obtener_administradoras()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo administradoras: {str(e)}"}

        @mcp.tool(
            name="obtener_tipos_fondos_por_administradora",
            description="Obtener tipos de fondos por administradora",
            tags=["titulos", "fci"]
        )
        async def obtener_tipos_fondos_por_administradora(
            administradora: str = Field(description="Nombre de la administradora")
        ) -> Dict[str, Any]:
            """
            Obtiene los tipos de fondos por administradora
            
            Args:
                administradora: Nombre de la administradora
            """
            try:
                result = await self.client.obtener_tipos_fondos_por_administradora(administradora=administradora)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo tipos de fondos por administradora: {str(e)}"}

        @mcp.tool(
            name="obtener_fondos_por_administradora_y_tipo",
            description="Obtener fondos por administradora y tipo",
            tags=["titulos", "fci"]
        )
        async def obtener_fondos_por_administradora_y_tipo(
            administradora: str = Field(description="Nombre de la administradora"),
            tipo_fondo: str = Field(description="Tipo de fondo")
        ) -> Dict[str, Any]:
            """
            Obtiene los fondos por administradora y tipo
            
            Args:
                administradora: Nombre de la administradora
                tipo_fondo: Tipo de fondo
            """
            try:
                result = await self.client.obtener_fondos_por_administradora_y_tipo(
                    administradora=administradora,
                    tipo_fondo=tipo_fondo
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo fondos por administradora y tipo: {str(e)}"} 