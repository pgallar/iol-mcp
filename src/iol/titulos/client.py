from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class TitulosClient(IOLAPIClient):
    async def obtener_cotizacion(
        self,
        simbolo: str,
        mercado: str,
        plazo: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene la cotización de un título
        
        Args:
            simbolo: Símbolo del título (Ejemplo: ALUA, APBR)
            mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
            plazo: Plazo de la cotización (t0, t1, t2, t3)
            
        Returns:
            Dict[str, Any]: Objeto CotizacionModel con la información de la cotización
        """
        params = {
            "model.simbolo": simbolo,
            "model.mercado": mercado,
            "simbolo": simbolo,
            "mercado": mercado
        }
        
        if plazo:
            params["model.plazo"] = plazo
            
        return await self.get(f"/api/v2/{mercado}/Titulos/{simbolo}/Cotizacion", params=params)

    async def obtener_panel(
        self,
        instrumento: str,
        pais: str
    ) -> Dict[str, Any]:
        """
        Obtiene el panel de un instrumento
        
        Args:
            instrumento: Tipo de instrumento (Acciones, Bonos, Opciones, etc)
            pais: País del panel (argentina, estados_unidos, etc)
        """
        # El endpoint correcto según la documentación de Swagger
        return await self.get(f"/api/v2/{pais}/Titulos/Cotizacion/Paneles/{instrumento}")

    async def obtener_opciones(
        self,
        simbolo: str,
        mercado: str
    ) -> Dict[str, Any]:
        """
        Obtiene las opciones de un título
        
        Args:
            simbolo: Símbolo del título
            mercado: Mercado del título (bcba, nyse, nasdaq, etc)
        """
        return await self.get(f"/api/v2/{mercado}/Titulos/{simbolo}/Opciones")

    async def obtener_instrumentos(
        self,
        pais: str
    ) -> Dict[str, Any]:
        """
        Obtiene los instrumentos disponibles para un país
        
        Args:
            pais: País (argentina, estados_unidos, etc)
        """
        return await self.get(f"/api/v2/{pais}/Titulos/Cotizacion/Instrumentos")
        
    async def obtener_fci(
        self,
        simbolo: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene información de fondos comunes de inversión
        
        Args:
            simbolo: Símbolo del FCI (opcional)
        """
        if simbolo:
            return await self.get(f"/api/v2/Titulos/FCI/{simbolo}")
        return await self.get("/api/v2/Titulos/FCI")
        
    async def obtener_tipos_fondos(self) -> Dict[str, Any]:
        """
        Obtiene los tipos de fondos disponibles
        """
        return await self.get("/api/v2/Titulos/FCI/TipoFondos")
        

        
    async def obtener_tipos_fondos_por_administradora(
        self,
        administradora: str
    ) -> Dict[str, Any]:
        """
        Obtiene los tipos de fondos por administradora
        
        Args:
            administradora: Nombre de la administradora (cONVEXITY, sUPERVIELLE)
        """
        return await self.get(f"/api/v2/Titulos/FCI/Administradoras/{administradora}/TipoFondos")
        

        
    async def obtener_cotizaciones_panel_todos(
        self,
        instrumento: str,
        pais: str
    ) -> Dict[str, Any]:
        """
        Obtiene todas las cotizaciones de un instrumento en un panel
        
        Args:
            instrumento: Tipo de instrumento (opciones, cedears, acciones, etc.)
            pais: País (estados_Unidos, argentina)
            
        Returns:
            Dict[str, Any]: Objeto InstrumentoModel con la información de las cotizaciones
        """
        params = {
            "cotizacionInstrumentoModel.instrumento": instrumento,
            "cotizacionInstrumentoModel.pais": pais
        }
        return await self.get(f"/api/v2/cotizaciones-orleans-panel/{instrumento}/{pais}/Todos", params=params)
        
    async def obtener_cotizaciones_panel_operables(
        self,
        instrumento: str,
        pais: str
    ) -> Dict[str, Any]:
        """
        Obtiene las cotizaciones operables de un instrumento en un panel
        
        Args:
            instrumento: Tipo de instrumento (opciones, cedears, acciones, etc.)
            pais: País (estados_Unidos, argentina)
            
        Returns:
            Dict[str, Any]: Objeto InstrumentoModel con la información de las cotizaciones operables
        """
        params = {
            "cotizacionInstrumentoModel.instrumento": instrumento,
            "cotizacionInstrumentoModel.pais": pais
        }
        return await self.get(f"/api/v2/cotizaciones-orleans-panel/{instrumento}/{pais}/Operables", params=params)
        
    async def obtener_cotizacion_detalle_mobile(
        self,
        mercado: str,
        simbolo: str,
        plazo: str
    ) -> Dict[str, Any]:
        """
        Obtiene el detalle de cotización para móvil de un título
        
        Args:
            mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
            simbolo: Símbolo del título
            plazo: Plazo de la cotización (t0, t1, t2, t3)
            
        Returns:
            Dict[str, Any]: Objeto CotizacionDetalleMobileModel con la información detallada
        """
        return await self.get(f"/api/v2/{mercado}/Titulos/{simbolo}/CotizacionDetalleMobile/{plazo}")
        
    async def obtener_cotizacion_serie_historica(
        self,
        mercado: str,
        simbolo: str,
        fecha_desde: str,
        fecha_hasta: str,
        ajustada: str
    ) -> List[Dict[str, Any]]:
        """
        Obtiene la serie histórica de cotizaciones de un título
        
        Args:
            mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
            simbolo: Símbolo del título
            fecha_desde: Fecha desde en formato ISO
            fecha_hasta: Fecha hasta en formato ISO
            ajustada: Indica si los datos deben estar ajustados (ajustada, sinAjustar)
            
        Returns:
            List[Dict[str, Any]]: Lista de objetos CotizacionModel con la información histórica
        """
        return await self.get(f"/api/v2/{mercado}/Titulos/{simbolo}/Cotizacion/seriehistorica/{fecha_desde}/{fecha_hasta}/{ajustada}") 