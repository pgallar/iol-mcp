from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class OperarClient(IOLAPIClient):
    async def obtener_ordenes_pendientes(
        self,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene las órdenes pendientes
        
        Args:
            fecha_desde: Fecha desde (YYYY-MM-DD)
            fecha_hasta: Fecha hasta (YYYY-MM-DD)
        """
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get("/api/v2/Operar/OrdenesPendientes", params=params)

    async def obtener_ordenes_finalizadas(
        self,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene las órdenes finalizadas
        
        Args:
            fecha_desde: Fecha desde (YYYY-MM-DD)
            fecha_hasta: Fecha hasta (YYYY-MM-DD)
        """
        params = {
            "fechaDesde": fecha_desde,
            "fechaHasta": fecha_hasta
        }
        params = {k: v for k, v in params.items() if v is not None}
        return await self.get("/api/v2/Operar/OrdenesFinalizadas", params=params)

    async def comprar(
        self,
        simbolo: str,
        cantidad: int,
        precio: float,
        validez: str,
        mercado: str,
        plazo: str
    ) -> Dict[str, Any]:
        """
        Realiza una operación de compra
        
        Args:
            simbolo: Símbolo del instrumento
            cantidad: Cantidad a comprar
            precio: Precio de compra
            validez: Validez de la orden
            mercado: Mercado donde operar
            plazo: Plazo de la operación
        """
        data = {
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "validez": validez,
            "mercado": mercado,
            "plazo": plazo
        }
        return await self.post("/api/v2/Operar/Comprar", json=data)

    async def vender(
        self,
        simbolo: str,
        cantidad: int,
        precio: float,
        validez: str,
        mercado: str,
        plazo: str
    ) -> Dict[str, Any]:
        """
        Realiza una operación de venta
        
        Args:
            simbolo: Símbolo del instrumento
            cantidad: Cantidad a vender
            precio: Precio de venta
            validez: Validez de la orden
            mercado: Mercado donde operar
            plazo: Plazo de la operación
        """
        data = {
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "validez": validez,
            "mercado": mercado,
            "plazo": plazo
        }
        return await self.post("/api/v2/Operar/Vender", json=data)

    async def cancelar_orden(
        self,
        numero: str
    ) -> Dict[str, Any]:
        """
        Cancela una orden pendiente
        
        Args:
            numero: Número de orden
        """
        return await self.delete(f"/api/v2/Operar/CancelarOrden/{numero}")

    async def obtener_estado_orden(
        self,
        numero: str
    ) -> Dict[str, Any]:
        """
        Obtiene el estado de una orden
        
        Args:
            numero: Número de orden
        """
        return await self.get(f"/api/v2/Operar/EstadoOrden/{numero}") 