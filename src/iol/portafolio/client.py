from typing import Dict, Any, Optional
from ..http_client import IOLAPIClient

class PortafolioClient(IOLAPIClient):
    async def obtener_portafolio(
        self,
        pais: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene el portafolio del usuario
        
        Args:
            pais: País del portafolio (argentina, estados_unidos, etc)
        """
        endpoint = "/api/v2/Portafolio"
        params = {}
        if pais:
            params["pais"] = pais
        return await self.get(endpoint, params=params)

    async def obtener_operaciones(
        self,
        pais: Optional[str] = None,
        estado: Optional[str] = None,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene las operaciones del usuario
        
        Args:
            pais: País de las operaciones (argentina, estados_unidos, etc)
            estado: Estado de las operaciones (todas, pendientes, terminadas, canceladas)
            fecha_desde: Fecha de inicio en formato YYYY-MM-DD
            fecha_hasta: Fecha de fin en formato YYYY-MM-DD
        """
        endpoint = "/api/v2/Operaciones"
        params = {}
        if pais:
            params["pais"] = pais
        if estado:
            params["estado"] = estado
        if fecha_desde:
            params["fechaDesde"] = fecha_desde
        if fecha_hasta:
            params["fechaHasta"] = fecha_hasta
        return await self.get(endpoint, params=params)
        
    async def obtener_portafolio_valorizado(
        self,
        pais: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene el portafolio valorizado del usuario
        
        Args:
            pais: País del portafolio (argentina, estados_unidos, etc)
        """
        endpoint = "/api/v2/Portafolio/Valorizado"
        params = {}
        if pais:
            params["pais"] = pais
        return await self.get(endpoint, params=params)
        
    async def obtener_rendimiento_historico(
        self,
        pais: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene el rendimiento histórico del portafolio
        
        Args:
            pais: País del portafolio (argentina, estados_unidos, etc)
        """
        endpoint = "/api/v2/Portafolio/Rendimiento"
        params = {}
        if pais:
            params["pais"] = pais
        return await self.get(endpoint, params=params)
        
    async def obtener_composicion_portafolio(
        self,
        pais: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene la composición del portafolio por tipo de instrumento
        
        Args:
            pais: País del portafolio (argentina, estados_unidos, etc)
        """
        endpoint = "/api/v2/Portafolio/Composicion"
        params = {}
        if pais:
            params["pais"] = pais
        return await self.get(endpoint, params=params) 