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
            simbolo: Símbolo del título
            mercado: Mercado del título (bcba, nyse, nasdaq, etc)
            plazo: Plazo de la cotización (t0, t1, t2)
        """
        endpoint = f"/api/v2/{mercado}/Titulos/{simbolo}/Cotizacion"
        if plazo:
            endpoint += f"/{plazo}"
        return await self.get(endpoint)

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

    async def obtener_puntas(
        self,
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
        endpoint = f"/api/v2/{mercado}/Titulos/{simbolo}/Puntas"
        if plazo:
            endpoint += f"/{plazo}"
        return await self.get(endpoint)
        
    async def obtener_datos_historicos(
        self,
        simbolo: str,
        mercado: str,
        desde: str,
        hasta: str,
        ajustado: bool = True
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
        endpoint = f"/api/v2/{mercado}/Titulos/{simbolo}/Cotizacion/Historico"
        params = {
            "fechaDesde": desde,
            "fechaHasta": hasta,
            "ajustado": str(ajustado).lower()
        }
        return await self.get(endpoint, params=params)
        
    async def buscar_titulos(
        self,
        filtro: str,
        mercado: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Busca títulos por nombre o símbolo
        
        Args:
            filtro: Texto a buscar
            mercado: Mercado del título (bcba, nyse, nasdaq, etc)
        """
        endpoint = f"/api/v2/Titulos/Buscar"
        params = {"filtro": filtro}
        if mercado:
            params["mercado"] = mercado
        return await self.get(endpoint, params=params)
        
    async def obtener_detalle_titulo(
        self,
        simbolo: str,
        mercado: str
    ) -> Dict[str, Any]:
        """
        Obtiene información detallada de un título
        
        Args:
            simbolo: Símbolo del título
            mercado: Mercado del título (bcba, nyse, nasdaq, etc)
        """
        return await self.get(f"/api/v2/{mercado}/Titulos/{simbolo}/Detalle")

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
        
    async def obtener_administradoras(self) -> Dict[str, Any]:
        """
        Obtiene las administradoras de fondos
        """
        return await self.get("/api/v2/Titulos/FCI/Administradoras")
        
    async def obtener_tipos_fondos_por_administradora(
        self,
        administradora: str
    ) -> Dict[str, Any]:
        """
        Obtiene los tipos de fondos por administradora
        
        Args:
            administradora: Nombre de la administradora
        """
        return await self.get(f"/api/v2/Titulos/FCI/Administradoras/{administradora}/TipoFondos")
        
    async def obtener_fondos_por_administradora_y_tipo(
        self,
        administradora: str,
        tipo_fondo: str
    ) -> Dict[str, Any]:
        """
        Obtiene los fondos por administradora y tipo
        
        Args:
            administradora: Nombre de la administradora
            tipo_fondo: Tipo de fondo
        """
        return await self.get(f"/api/v2/Titulos/FCI/Administradoras/{administradora}/TipoFondos/{tipo_fondo}") 