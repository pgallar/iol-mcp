from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import OperarClient

class OperarRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = OperarClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_ordenes_pendientes",
            description="Obtener órdenes pendientes del usuario",
            tags=["operar", "ordenes"]
        )
        async def obtener_ordenes_pendientes(
            pais: Optional[str] = Field(default=None, description="País de las órdenes (argentina, estados_unidos, etc)"),
            mercado: Optional[str] = Field(default=None, description="Mercado de las órdenes (bcba, nyse, nasdaq, etc)"),
            simbolo: Optional[str] = Field(default=None, description="Símbolo del título"),
            tipo_orden: Optional[str] = Field(default=None, description="Tipo de orden (compra, venta)")
        ) -> Dict[str, Any]:
            """
            Obtiene las órdenes pendientes del usuario
            
            Args:
                pais: País de las órdenes (argentina, estados_unidos, etc)
                mercado: Mercado de las órdenes (bcba, nyse, nasdaq, etc)
                simbolo: Símbolo del título
                tipo_orden: Tipo de orden (compra, venta)
            """
            try:
                result = await self.client.obtener_ordenes_pendientes(
                    pais=pais,
                    mercado=mercado,
                    simbolo=simbolo,
                    tipo_orden=tipo_orden
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo órdenes pendientes: {str(e)}"}

        @mcp.tool(
            name="obtener_ordenes_finalizadas",
            description="Obtener órdenes finalizadas del usuario",
            tags=["operar", "ordenes"]
        )
        async def obtener_ordenes_finalizadas(
            pais: Optional[str] = Field(default=None, description="País de las órdenes (argentina, estados_unidos, etc)"),
            mercado: Optional[str] = Field(default=None, description="Mercado de las órdenes (bcba, nyse, nasdaq, etc)"),
            simbolo: Optional[str] = Field(default=None, description="Símbolo del título"),
            tipo_orden: Optional[str] = Field(default=None, description="Tipo de orden (compra, venta)"),
            fecha_desde: Optional[str] = Field(default=None, description="Fecha de inicio en formato YYYY-MM-DD"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha de fin en formato YYYY-MM-DD"),
            estado: Optional[str] = Field(default=None, description="Estado de las órdenes (todas, terminadas, canceladas)")
        ) -> Dict[str, Any]:
            """
            Obtiene las órdenes finalizadas del usuario
            
            Args:
                pais: País de las órdenes (argentina, estados_unidos, etc)
                mercado: Mercado de las órdenes (bcba, nyse, nasdaq, etc)
                simbolo: Símbolo del título
                tipo_orden: Tipo de orden (compra, venta)
                fecha_desde: Fecha de inicio en formato YYYY-MM-DD
                fecha_hasta: Fecha de fin en formato YYYY-MM-DD
                estado: Estado de las órdenes (todas, terminadas, canceladas)
            """
            try:
                result = await self.client.obtener_ordenes_finalizadas(
                    pais=pais,
                    mercado=mercado,
                    simbolo=simbolo,
                    tipo_orden=tipo_orden,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta,
                    estado=estado
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo órdenes finalizadas: {str(e)}"}

        @mcp.tool(
            name="comprar",
            description="Crear una orden de compra",
            tags=["operar", "compra"]
        )
        async def comprar(
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)"),
            simbolo: str = Field(description="Símbolo del título"),
            cantidad: float = Field(description="Cantidad a comprar"),
            precio: float = Field(description="Precio de compra"),
            plazo: str = Field(description="Plazo de la operación (t0, t1, t2)"),
            validez: Optional[str] = Field(default=None, description="Fecha de validez de la orden en formato YYYY-MM-DD")
        ) -> Dict[str, Any]:
            """
            Crea una orden de compra
            
            Args:
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
                simbolo: Símbolo del título
                cantidad: Cantidad a comprar
                precio: Precio de compra
                plazo: Plazo de la operación (t0, t1, t2)
                validez: Fecha de validez de la orden en formato YYYY-MM-DD
            """
            try:
                result = await self.client.comprar(
                    mercado=mercado,
                    simbolo=simbolo,
                    cantidad=cantidad,
                    precio=precio,
                    plazo=plazo,
                    validez=validez
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando orden de compra: {str(e)}"}

        @mcp.tool(
            name="vender",
            description="Crear una orden de venta",
            tags=["operar", "venta"]
        )
        async def vender(
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)"),
            simbolo: str = Field(description="Símbolo del título"),
            cantidad: float = Field(description="Cantidad a vender"),
            precio: float = Field(description="Precio de venta"),
            plazo: str = Field(description="Plazo de la operación (t0, t1, t2)"),
            validez: Optional[str] = Field(default=None, description="Fecha de validez de la orden en formato YYYY-MM-DD")
        ) -> Dict[str, Any]:
            """
            Crea una orden de venta
            
            Args:
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
                simbolo: Símbolo del título
                cantidad: Cantidad a vender
                precio: Precio de venta
                plazo: Plazo de la operación (t0, t1, t2)
                validez: Fecha de validez de la orden en formato YYYY-MM-DD
            """
            try:
                result = await self.client.vender(
                    mercado=mercado,
                    simbolo=simbolo,
                    cantidad=cantidad,
                    precio=precio,
                    plazo=plazo,
                    validez=validez
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando orden de venta: {str(e)}"}

        @mcp.tool(
            name="cancelar_orden",
            description="Cancelar una orden",
            tags=["operar", "cancelar"]
        )
        async def cancelar_orden(
            numero: str = Field(description="Número de orden")
        ) -> Dict[str, Any]:
            """
            Cancela una orden
            
            Args:
                numero: Número de orden
            """
            try:
                result = await self.client.cancelar_orden(numero=numero)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error cancelando orden: {str(e)}"}

        @mcp.tool(
            name="obtener_estado_orden",
            description="Obtener estado de una orden",
            tags=["operar", "estado"]
        )
        async def obtener_estado_orden(
            numero: str = Field(description="Número de orden")
        ) -> Dict[str, Any]:
            """
            Obtiene el estado de una orden
            
            Args:
                numero: Número de orden
            """
            try:
                result = await self.client.obtener_estado_orden(numero=numero)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo estado de orden: {str(e)}"}
                
        @mcp.tool(
            name="obtener_plazos",
            description="Obtener plazos disponibles para operar un título",
            tags=["operar", "plazos"]
        )
        async def obtener_plazos(
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)"),
            simbolo: str = Field(description="Símbolo del título")
        ) -> Dict[str, Any]:
            """
            Obtiene los plazos disponibles para operar un título
            
            Args:
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
                simbolo: Símbolo del título
            """
            try:
                result = await self.client.obtener_plazos(
                    mercado=mercado,
                    simbolo=simbolo
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo plazos: {str(e)}"}
                
        @mcp.tool(
            name="obtener_panel_operaciones",
            description="Obtener panel de operaciones para un instrumento",
            tags=["operar", "panel"]
        )
        async def obtener_panel_operaciones(
            instrumento: str = Field(description="Tipo de instrumento (Acciones, Bonos, Opciones, etc)"),
            pais: str = Field(description="País del panel (argentina, estados_unidos, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene el panel de operaciones para un instrumento
            
            Args:
                instrumento: Tipo de instrumento (Acciones, Bonos, Opciones, etc)
                pais: País del panel (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_panel_operaciones(
                    instrumento=instrumento,
                    pais=pais
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo panel de operaciones: {str(e)}"}
                
        @mcp.tool(
            name="comprar_valor_efectivo",
            description="Crear una orden de compra por valor efectivo",
            tags=["operar", "compra"]
        )
        async def comprar_valor_efectivo(
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)"),
            simbolo: str = Field(description="Símbolo del título"),
            monto: float = Field(description="Monto efectivo a invertir"),
            precio: float = Field(description="Precio de compra"),
            plazo: str = Field(description="Plazo de la operación (t0, t1, t2)"),
            validez: Optional[str] = Field(default=None, description="Fecha de validez de la orden en formato YYYY-MM-DD")
        ) -> Dict[str, Any]:
            """
            Crea una orden de compra por valor efectivo
            
            Args:
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
                simbolo: Símbolo del título
                monto: Monto efectivo a invertir
                precio: Precio de compra
                plazo: Plazo de la operación (t0, t1, t2)
                validez: Fecha de validez de la orden en formato YYYY-MM-DD
            """
            try:
                result = await self.client.comprar_valor_efectivo(
                    mercado=mercado,
                    simbolo=simbolo,
                    monto=monto,
                    precio=precio,
                    plazo=plazo,
                    validez=validez
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando orden de compra por valor efectivo: {str(e)}"}
                
        @mcp.tool(
            name="vender_valor_nominal",
            description="Crear una orden de venta por valor nominal",
            tags=["operar", "venta"]
        )
        async def vender_valor_nominal(
            mercado: str = Field(description="Mercado del título (bcba, nyse, nasdaq, etc)"),
            simbolo: str = Field(description="Símbolo del título"),
            valor_nominal: float = Field(description="Valor nominal a vender"),
            precio: float = Field(description="Precio de venta"),
            plazo: str = Field(description="Plazo de la operación (t0, t1, t2)"),
            validez: Optional[str] = Field(default=None, description="Fecha de validez de la orden en formato YYYY-MM-DD")
        ) -> Dict[str, Any]:
            """
            Crea una orden de venta por valor nominal
            
            Args:
                mercado: Mercado del título (bcba, nyse, nasdaq, etc)
                simbolo: Símbolo del título
                valor_nominal: Valor nominal a vender
                precio: Precio de venta
                plazo: Plazo de la operación (t0, t1, t2)
                validez: Fecha de validez de la orden en formato YYYY-MM-DD
            """
            try:
                result = await self.client.vender_valor_nominal(
                    mercado=mercado,
                    simbolo=simbolo,
                    valor_nominal=valor_nominal,
                    precio=precio,
                    plazo=plazo,
                    validez=validez
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando orden de venta por valor nominal: {str(e)}"}
                
        @mcp.tool(
            name="suscribir_fci",
            description="Suscribir un FCI",
            tags=["operar", "fci"]
        )
        async def suscribir_fci(
            simbolo: str = Field(description="Símbolo del FCI"),
            monto: float = Field(description="Monto a suscribir")
        ) -> Dict[str, Any]:
            """
            Suscribe un FCI
            
            Args:
                simbolo: Símbolo del FCI
                monto: Monto a suscribir
            """
            try:
                result = await self.client.suscribir_fci(
                    simbolo=simbolo,
                    monto=monto
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error suscribiendo FCI: {str(e)}"}
                
        @mcp.tool(
            name="rescatar_fci",
            description="Rescatar un FCI",
            tags=["operar", "fci"]
        )
        async def rescatar_fci(
            simbolo: str = Field(description="Símbolo del FCI"),
            cantidad: float = Field(description="Cantidad a rescatar")
        ) -> Dict[str, Any]:
            """
            Rescata un FCI
            
            Args:
                simbolo: Símbolo del FCI
                cantidad: Cantidad a rescatar
            """
            try:
                result = await self.client.rescatar_fci(
                    simbolo=simbolo,
                    cantidad=cantidad
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error rescatando FCI: {str(e)}"} 