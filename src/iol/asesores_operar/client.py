from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class AsesoresOperarClient(IOLAPIClient):
    async def obtener_ordenes_pendientes(
        self,
        id_cliente: int,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtiene las órdenes pendientes de un cliente"""
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get(f"/AsesoresOperar/Clientes/{id_cliente}/OrdenesPendientes", params=params)

    async def obtener_ordenes_finalizadas(
        self,
        id_cliente: int,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtiene las órdenes finalizadas de un cliente"""
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get(f"/AsesoresOperar/Clientes/{id_cliente}/OrdenesFinalizadas", params=params)

    async def operar_comprar(
        self,
        id_cliente: int,
        simbolo: str,
        cantidad: int,
        precio: float,
        validez: str,
        mercado: str,
        plazo: str
    ) -> Dict[str, Any]:
        """Realiza una operación de compra para un cliente"""
        data = {
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "validez": validez,
            "mercado": mercado,
            "plazo": plazo
        }
        return await self.post(f"/AsesoresOperar/Clientes/{id_cliente}/Comprar", json=data)

    async def operar_vender(
        self,
        id_cliente: int,
        simbolo: str,
        cantidad: int,
        precio: float,
        validez: str,
        mercado: str,
        plazo: str
    ) -> Dict[str, Any]:
        """Realiza una operación de venta para un cliente"""
        data = {
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "validez": validez,
            "mercado": mercado,
            "plazo": plazo
        }
        return await self.post(f"/AsesoresOperar/Clientes/{id_cliente}/Vender", json=data)

    async def cancelar_orden(
        self,
        id_cliente: int,
        numero: str
    ) -> Dict[str, Any]:
        """Cancela una orden pendiente de un cliente"""
        return await self.delete(f"/AsesoresOperar/Clientes/{id_cliente}/CancelarOrden/{numero}") 