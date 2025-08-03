from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class NotificacionClient(IOLAPIClient):
    async def obtener_notificaciones(
        self,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene las notificaciones del usuario
        
        Args:
            fecha_desde: Fecha desde (YYYY-MM-DD)
            fecha_hasta: Fecha hasta (YYYY-MM-DD)
        """
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get("/api/v2/Notificacion", params=params)

    async def marcar_notificacion_leida(
        self,
        id_notificacion: int
    ) -> Dict[str, Any]:
        """
        Marca una notificación como leída
        
        Args:
            id_notificacion: ID de la notificación
        """
        return await self.post(f"/api/v2/Notificacion/{id_notificacion}/Leida", json={}) 