from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class PortafolioClient(IOLAPIClient):
    async def obtener_portafolio(
        self,
        pais: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene el portafolio del usuario
        
        Args:
            pais: Filtrar por país (argentina, estados_unidos, etc)
        """
        params = {"pais": pais} if pais else None
        return await self.get("/portafolio", params=params)

    async def obtener_operaciones(
        self,
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
        params = {
            "filtro": filtro,
            "pais": pais,
            "estado": estado,
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta,
            "numero": numero
        }
        # Eliminar parámetros None
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get("/operaciones", params=params) 