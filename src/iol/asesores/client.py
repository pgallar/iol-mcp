from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class AsesoresClient(IOLAPIClient):
    async def obtener_asesores(self) -> Dict[str, Any]:
        """Obtiene el listado de asesores disponibles"""
        return await self.get("/api/v2/Asesores")

    async def obtener_asesor(self, id_asesor: int) -> Dict[str, Any]:
        """Obtiene la información de un asesor específico"""
        return await self.get(f"/api/v2/Asesores/{id_asesor}")

    async def obtener_clientes_asesor(self) -> Dict[str, Any]:
        """Obtiene el listado de clientes del asesor"""
        return await self.get("/api/v2/Asesores/Clientes")

    async def obtener_cliente_asesor(self, id_cliente: int) -> Dict[str, Any]:
        """Obtiene la información de un cliente específico del asesor"""
        return await self.get(f"/api/v2/Asesores/Clientes/{id_cliente}")

    async def obtener_operaciones_cliente(
        self,
        id_cliente: int,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtiene las operaciones de un cliente específico"""
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get(f"/api/v2/Asesores/Clientes/{id_cliente}/Operaciones", params=params) 