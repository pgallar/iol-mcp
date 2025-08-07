from typing import Dict, Any, Optional, List
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import TitulosClient

class CotizacionModel(BaseModel):
    """Modelo para representar una cotización según el swagger"""
    # Aquí se definirían los campos específicos de CotizacionModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class TituloFCIModel(BaseModel):
    """Modelo para representar un título FCI según el swagger"""
    # Aquí se definirían los campos específicos de TituloFCIModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class InstrumentoModel(BaseModel):
    """Modelo para representar un instrumento según el swagger"""
    # Aquí se definirían los campos específicos de InstrumentoModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class CotizacionDetalleMobileModel(BaseModel):
    """Modelo para representar una cotización detallada para móvil según el swagger"""
    # Aquí se definirían los campos específicos de CotizacionDetalleMobileModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

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
            simbolo: str = Field(description="Símbolo del título (Ejemplo: ALUA, APBR)"),
            mercado: str = Field(description="Mercado del título", enum=["bCBA", "nYSE", "nASDAQ", "aMEX", "bCS", "rOFX"]),
            plazo: Optional[str] = Field(default=None, description="Plazo de la cotización (t0, t1, t2, t3)")
        ) -> Dict[str, Any]:
            """
            Obtiene la cotización de un título
            
            Args:
                simbolo: Símbolo del título (Ejemplo: ALUA, APBR)
                mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
                plazo: Plazo de la cotización (t0, t1, t2, t3)
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
                result = await self.client.obtener_instrumentos(
                    pais=pais
                )
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
                result = await self.client.obtener_fci(
                    simbolo=simbolo
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo FCI: {str(e)}"}

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
            name="obtener_tipos_fondos_por_administradora",
            description="Obtener tipos de fondos por administradora",
            tags=["titulos", "fci"]
        )
        async def obtener_tipos_fondos_por_administradora(
            administradora: str = Field(description="Nombre de la administradora", enum=["cONVEXITY", "sUPERVIELLE"])
        ) -> Dict[str, Any]:
            """
            Obtiene los tipos de fondos por administradora
            
            Args:
                administradora: Nombre de la administradora (cONVEXITY, sUPERVIELLE)
            """
            try:
                result = await self.client.obtener_tipos_fondos_por_administradora(
                    administradora=administradora
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo tipos de fondos por administradora: {str(e)}"}


                
        @mcp.tool(
            name="obtener_cotizaciones_panel_todos",
            description="Obtener todas las cotizaciones de un instrumento en un panel",
            tags=["titulos", "panel", "cotizaciones"]
        )
        async def obtener_cotizaciones_panel_todos(
            instrumento: str = Field(description="Tipo de instrumento", enum=[
                "opciones", "cedears", "acciones", "aDRs", "titulosPublicos", "cauciones",
                "cHPD", "futuros", "obligacionesNegociables", "letras"
            ]),
            pais: str = Field(description="País", enum=["estados_Unidos", "argentina"])
        ) -> Dict[str, Any]:
            """
            Obtiene todas las cotizaciones de un instrumento en un panel
            
            Args:
                instrumento: Tipo de instrumento (opciones, cedears, acciones, etc.)
                pais: País (estados_Unidos, argentina)
            """
            try:
                result = await self.client.obtener_cotizaciones_panel_todos(
                    instrumento=instrumento,
                    pais=pais
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo cotizaciones del panel: {str(e)}"}
                
        @mcp.tool(
            name="obtener_cotizaciones_panel_operables",
            description="Obtener cotizaciones operables de un instrumento en un panel",
            tags=["titulos", "panel", "cotizaciones", "operables"]
        )
        async def obtener_cotizaciones_panel_operables(
            instrumento: str = Field(description="Tipo de instrumento", enum=[
                "opciones", "cedears", "acciones", "aDRs", "titulosPublicos", "cauciones",
                "cHPD", "futuros", "obligacionesNegociables", "letras"
            ]),
            pais: str = Field(description="País", enum=["estados_Unidos", "argentina"])
        ) -> Dict[str, Any]:
            """
            Obtiene las cotizaciones operables de un instrumento en un panel
            
            Args:
                instrumento: Tipo de instrumento (opciones, cedears, acciones, etc.)
                pais: País (estados_Unidos, argentina)
            """
            try:
                result = await self.client.obtener_cotizaciones_panel_operables(
                    instrumento=instrumento,
                    pais=pais
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo cotizaciones operables del panel: {str(e)}"}
                
        @mcp.tool(
            name="obtener_cotizacion_detalle_mobile",
            description="Obtener detalle de cotización para móvil de un título",
            tags=["titulos", "cotizacion", "mobile"]
        )
        async def obtener_cotizacion_detalle_mobile(
            mercado: str = Field(description="Mercado del título", enum=["bCBA", "nYSE", "nASDAQ", "aMEX", "bCS", "rOFX"]),
            simbolo: str = Field(description="Símbolo del título"),
            plazo: str = Field(description="Plazo de la cotización", enum=["t0", "t1", "t2", "t3"])
        ) -> Dict[str, Any]:
            """
            Obtiene el detalle de cotización para móvil de un título
            
            Args:
                mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
                simbolo: Símbolo del título
                plazo: Plazo de la cotización (t0, t1, t2, t3)
            """
            try:
                result = await self.client.obtener_cotizacion_detalle_mobile(
                    mercado=mercado,
                    simbolo=simbolo,
                    plazo=plazo
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo detalle de cotización para móvil: {str(e)}"}
                
        @mcp.tool(
            name="obtener_cotizacion_serie_historica",
            description="Obtener serie histórica de cotizaciones de un título",
            tags=["titulos", "cotizacion", "historica"]
        )
        async def obtener_cotizacion_serie_historica(
            mercado: str = Field(description="Mercado del título", enum=["bCBA", "nYSE", "nASDAQ", "aMEX", "bCS", "rOFX"]),
            simbolo: str = Field(description="Símbolo del título"),
            fecha_desde: str = Field(description="Fecha desde en formato ISO (YYYY-MM-DD)"),
            fecha_hasta: str = Field(description="Fecha hasta en formato ISO (YYYY-MM-DD)"),
            ajustada: str = Field(description="Indica si los datos deben estar ajustados", enum=["ajustada", "sinAjustar"])
        ) -> Dict[str, Any]:
            """
            Obtiene la serie histórica de cotizaciones de un título
            
            Args:
                mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
                simbolo: Símbolo del título
                fecha_desde: Fecha desde en formato ISO
                fecha_hasta: Fecha hasta en formato ISO
                ajustada: Indica si los datos deben estar ajustados (ajustada, sinAjustar)
            """
            try:
                result = await self.client.obtener_cotizacion_serie_historica(
                    mercado=mercado,
                    simbolo=simbolo,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta,
                    ajustada=ajustada
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo serie histórica de cotizaciones: {str(e)}"} 