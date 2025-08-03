from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class OperarClient(IOLAPIClient):
    async def obtener_ordenes_pendientes(
        self,
        pais: Optional[str] = None,
        mercado: Optional[str] = None,
        simbolo: Optional[str] = None,
        tipo_orden: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene las órdenes pendientes del usuario
        
        Args:
            pais: País de las órdenes (argentina, estados_unidos, etc)
            mercado: Mercado de las órdenes (bcba, nyse, nasdaq, etc)
            simbolo: Símbolo del título
            tipo_orden: Tipo de orden (compra, venta)
        """
        endpoint = "/api/v2/Operar/OrdenesPendientes"
        params = {}
        if pais:
            params["pais"] = pais
        if mercado:
            params["mercado"] = mercado
        if simbolo:
            params["simbolo"] = simbolo
        if tipo_orden:
            params["tipoOrden"] = tipo_orden
        return await self.get(endpoint, params=params)

    async def obtener_ordenes_finalizadas(
        self,
        pais: Optional[str] = None,
        mercado: Optional[str] = None,
        simbolo: Optional[str] = None,
        tipo_orden: Optional[str] = None,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None,
        estado: Optional[str] = None
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
        endpoint = "/api/v2/Operar/OrdenesFinalizadas"
        params = {}
        if pais:
            params["pais"] = pais
        if mercado:
            params["mercado"] = mercado
        if simbolo:
            params["simbolo"] = simbolo
        if tipo_orden:
            params["tipoOrden"] = tipo_orden
        if fecha_desde:
            params["fechaDesde"] = fecha_desde
        if fecha_hasta:
            params["fechaHasta"] = fecha_hasta
        if estado:
            params["estado"] = estado
        return await self.get(endpoint, params=params)

    async def comprar(
        self,
        mercado: str,
        simbolo: str,
        cantidad: float,
        precio: float,
        plazo: str,
        validez: Optional[str] = None
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
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "plazo": plazo,
        }
        if validez:
            data["validez"] = validez
        return await self.post("/api/v2/Operar/Comprar", json=data)

    async def vender(
        self,
        mercado: str,
        simbolo: str,
        cantidad: float,
        precio: float,
        plazo: str,
        validez: Optional[str] = None
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
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "plazo": plazo,
        }
        if validez:
            data["validez"] = validez
        return await self.post("/api/v2/Operar/Vender", json=data)

    async def cancelar_orden(
        self,
        numero: str
    ) -> Dict[str, Any]:
        """
        Cancela una orden
        
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
        
    async def obtener_plazos(
        self,
        mercado: str,
        simbolo: str
    ) -> Dict[str, Any]:
        """
        Obtiene los plazos disponibles para operar un título
        
        Args:
            mercado: Mercado del título (bcba, nyse, nasdaq, etc)
            simbolo: Símbolo del título
        """
        endpoint = f"/api/v2/Operar/Plazos/{mercado}/{simbolo}"
        return await self.get(endpoint)
        
    async def obtener_panel_operaciones(
        self,
        instrumento: str,
        pais: str
    ) -> Dict[str, Any]:
        """
        Obtiene el panel de operaciones para un instrumento
        
        Args:
            instrumento: Tipo de instrumento (Acciones, Bonos, Opciones, etc)
            pais: País del panel (argentina, estados_unidos, etc)
        """
        endpoint = f"/api/v2/Operar/PanelOperaciones/{instrumento}/{pais}"
        return await self.get(endpoint)
        
    async def comprar_valor_efectivo(
        self,
        mercado: str,
        simbolo: str,
        monto: float,
        precio: float,
        plazo: str,
        validez: Optional[str] = None
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
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "monto": monto,
            "precio": precio,
            "plazo": plazo,
        }
        if validez:
            data["validez"] = validez
        return await self.post("/api/v2/Operar/ComprarValorEfectivo", json=data)
        
    async def vender_valor_nominal(
        self,
        mercado: str,
        simbolo: str,
        valor_nominal: float,
        precio: float,
        plazo: str,
        validez: Optional[str] = None
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
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "valorNominal": valor_nominal,
            "precio": precio,
            "plazo": plazo,
        }
        if validez:
            data["validez"] = validez
        return await self.post("/api/v2/Operar/VenderValorNominal", json=data) 