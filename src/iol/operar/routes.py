from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import OperarClient

class OrdenOperacion(BaseModel):
    simbolo: str = Field(description="Símbolo del instrumento")
    cantidad: int = Field(description="Cantidad a operar")
    precio: float = Field(description="Precio de la operación")
    validez: str = Field(description="Validez de la orden")
    mercado: str = Field(description="Mercado donde operar")
    plazo: str = Field(description="Plazo de la operación")

    model_config = ConfigDict(extra="ignore", validate_assignment=True)

    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class OperarRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = OperarClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_ordenes_pendientes",
            description="Obtener órdenes pendientes",
            tags=["operar", "ordenes"]
        )
        async def obtener_ordenes_pendientes(
            fecha_desde: Optional[str] = None,
            fecha_hasta: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene las órdenes pendientes
            
            Args:
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_ordenes_pendientes(
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo órdenes pendientes: {str(e)}"}

        @mcp.tool(
            name="obtener_ordenes_finalizadas",
            description="Obtener órdenes finalizadas",
            tags=["operar", "ordenes"]
        )
        async def obtener_ordenes_finalizadas(
            fecha_desde: Optional[str] = None,
            fecha_hasta: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene las órdenes finalizadas
            
            Args:
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_ordenes_finalizadas(
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo órdenes finalizadas: {str(e)}"}

        @mcp.tool(
            name="comprar",
            description="Realizar operación de compra",
            tags=["operar", "compra"]
        )
        async def comprar(
            orden: OrdenOperacion
        ) -> Dict[str, Any]:
            """
            Realiza una operación de compra
            
            Args:
                orden: Datos de la orden de compra
            """
            try:
                result = await self.client.comprar(
                    simbolo=orden.simbolo,
                    cantidad=orden.cantidad,
                    precio=orden.precio,
                    validez=orden.validez,
                    mercado=orden.mercado,
                    plazo=orden.plazo
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error realizando compra: {str(e)}"}

        @mcp.tool(
            name="vender",
            description="Realizar operación de venta",
            tags=["operar", "venta"]
        )
        async def vender(
            orden: OrdenOperacion
        ) -> Dict[str, Any]:
            """
            Realiza una operación de venta
            
            Args:
                orden: Datos de la orden de venta
            """
            try:
                result = await self.client.vender(
                    simbolo=orden.simbolo,
                    cantidad=orden.cantidad,
                    precio=orden.precio,
                    validez=orden.validez,
                    mercado=orden.mercado,
                    plazo=orden.plazo
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error realizando venta: {str(e)}"}

        @mcp.tool(
            name="cancelar_orden",
            description="Cancelar orden pendiente",
            tags=["operar", "cancelar"]
        )
        async def cancelar_orden(
            numero: str
        ) -> Dict[str, Any]:
            """
            Cancela una orden pendiente
            
            Args:
                numero: Número de orden
            """
            try:
                result = await self.client.cancelar_orden(numero)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error cancelando orden: {str(e)}"}

        @mcp.tool(
            name="obtener_estado_orden",
            description="Obtener estado de una orden",
            tags=["operar", "consulta"]
        )
        async def obtener_estado_orden(
            numero: str
        ) -> Dict[str, Any]:
            """
            Obtiene el estado de una orden
            
            Args:
                numero: Número de orden
            """
            try:
                result = await self.client.obtener_estado_orden(numero)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo estado de orden: {str(e)}"} 