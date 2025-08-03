from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class MiCuentaClient(IOLAPIClient):
    async def obtener_estado_cuenta(self) -> Dict[str, Any]:
        """Obtiene el estado de cuenta del usuario"""
        return await self.get("/MiCuenta/EstadoCuenta")

    async def obtener_saldos(self) -> Dict[str, Any]:
        """Obtiene los saldos de la cuenta"""
        return await self.get("/MiCuenta/Saldos")

    async def obtener_movimientos(
        self,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtiene los movimientos de la cuenta"""
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get("/MiCuenta/Movimientos", params=params)

    async def obtener_movimientos_fondos(
        self,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtiene los movimientos de fondos"""
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get("/MiCuenta/MovimientosFondos", params=params)

    async def obtener_movimientos_fci(
        self,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtiene los movimientos de FCI"""
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get("/MiCuenta/MovimientosFCI", params=params) 