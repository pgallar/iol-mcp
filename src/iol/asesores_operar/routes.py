from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import AsesoresOperarClient

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

class AsesoresOperarRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = AsesoresOperarClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="asesores_obtener_ordenes_pendientes",  # Prefijo para evitar duplicados
            description="Obtener órdenes pendientes de un cliente",
            tags=["asesores", "operar", "ordenes"]
        )
        async def obtener_ordenes_pendientes(
            id_cliente: int,
            fecha_desde: Optional[str] = None,
            fecha_hasta: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene las órdenes pendientes de un cliente
            
            Args:
                id_cliente: ID del cliente
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_ordenes_pendientes(
                    id_cliente=id_cliente,
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
            name="asesores_obtener_ordenes_finalizadas",  # Prefijo para evitar duplicados
            description="Obtener órdenes finalizadas de un cliente",
            tags=["asesores", "operar", "ordenes"]
        )
        async def obtener_ordenes_finalizadas(
            id_cliente: int,
            fecha_desde: Optional[str] = None,
            fecha_hasta: Optional[str] = None
        ) -> Dict[str, Any]:
            """
            Obtiene las órdenes finalizadas de un cliente
            
            Args:
                id_cliente: ID del cliente
                fecha_desde: Fecha desde (YYYY-MM-DD)
                fecha_hasta: Fecha hasta (YYYY-MM-DD)
            """
            try:
                result = await self.client.obtener_ordenes_finalizadas(
                    id_cliente=id_cliente,
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
            name="operar_comprar",
            description="Realizar operación de compra para un cliente",
            tags=["asesores", "operar", "compra"]
        )
        async def operar_comprar(
            id_cliente: int,
            orden: OrdenOperacion = Field(
                description="Datos de la orden de compra",
                example={
                    "simbolo": "GGAL",
                    "cantidad": 100,
                    "precio": 250.50,
                    "validez": "dia",
                    "mercado": "bcba",
                    "plazo": "t2"
                }
            )
        ) -> Dict[str, Any]:
            """
            Realiza una operación de compra para un cliente
            
            Args:
                id_cliente: ID del cliente
                orden: Datos de la orden de compra
            """
            try:
                result = await self.client.operar_comprar(
                    id_cliente=id_cliente,
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
            name="operar_vender",
            description="Realizar operación de venta para un cliente",
            tags=["asesores", "operar", "venta"]
        )
        async def operar_vender(
            id_cliente: int,
            orden: OrdenOperacion = Field(
                description="Datos de la orden de venta",
                example={
                    "simbolo": "GGAL",
                    "cantidad": 100,
                    "precio": 250.50,
                    "validez": "dia",
                    "mercado": "bcba",
                    "plazo": "t2"
                }
            )
        ) -> Dict[str, Any]:
            """
            Realiza una operación de venta para un cliente
            
            Args:
                id_cliente: ID del cliente
                orden: Datos de la orden de venta
            """
            try:
                result = await self.client.operar_vender(
                    id_cliente=id_cliente,
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
            name="asesores_cancelar_orden",  # Prefijo para evitar duplicados
            description="Cancelar orden pendiente de un cliente",
            tags=["asesores", "operar", "cancelar"]
        )
        async def cancelar_orden(
            id_cliente: int,
            numero: str
        ) -> Dict[str, Any]:
            """
            Cancela una orden pendiente de un cliente
            
            Args:
                id_cliente: ID del cliente
                numero: Número de orden a cancelar
            """
            try:
                result = await self.client.cancelar_orden(
                    id_cliente=id_cliente,
                    numero=numero
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error cancelando orden: {str(e)}"} 