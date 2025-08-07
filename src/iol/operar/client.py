from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
from ..http_client import IOLAPIClient

class OperarClient(IOLAPIClient):
    async def comprar(
        self,
        mercado: str,
        simbolo: str,
        precio: float,
        plazo: str,
        validez: Optional[str] = None,
        cantidad: Optional[float] = None,
        tipo_orden: Optional[str] = None,
        monto: Optional[float] = None,
        id_fuente: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Crea una orden de compra
        
        Args:
            mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
            simbolo: Símbolo del título
            precio: Precio de compra
            plazo: Plazo de la operación (t0, t1, t2, t3)
            validez: Fecha de validez de la orden en formato ISO (por defecto: 3 meses)
            cantidad: Cantidad a comprar (opcional)
            tipo_orden: Tipo de orden (precioLimite, precioMercado) (opcional)
            monto: Monto efectivo a invertir (opcional)
            id_fuente: ID de la fuente (opcional)
        """
        # Si no se proporciona validez, usar fecha a 3 meses
        if validez is None:
            validez = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%dT23:59:59")
            
        # Si no se proporciona validez, usar fecha a 3 meses
        if validez is None:
            validez = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%dT23:59:59")
            
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "precio": precio,
            "plazo": plazo,
            "validez": validez
        }
        
        if cantidad is not None:
            data["cantidad"] = cantidad
        if tipo_orden:
            data["tipoOrden"] = tipo_orden
        if monto is not None:
            data["monto"] = monto
        if id_fuente is not None:
            data["idFuente"] = id_fuente
            
        return await self.post("/api/v2/operar/Comprar", json=data)

    async def vender(
        self,
        mercado: str,
        simbolo: str,
        cantidad: float,
        precio: float,
        validez: str,
        tipo_orden: Optional[str] = None,
        plazo: Optional[str] = None,
        id_fuente: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Crea una orden de venta
        
        Args:
            mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
            simbolo: Símbolo del título
            cantidad: Cantidad a vender
            precio: Precio de venta
            validez: Fecha de validez de la orden en formato ISO
            tipo_orden: Tipo de orden (precioLimite, precioMercado) (opcional)
            plazo: Plazo de la operación (t0, t1, t2, t3) (opcional)
            id_fuente: ID de la fuente (opcional)
        """
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "validez": validez
        }
        
        if tipo_orden:
            data["tipoOrden"] = tipo_orden
        if plazo:
            data["plazo"] = plazo
        if id_fuente is not None:
            data["idFuente"] = id_fuente
            
        return await self.post("/api/v2/operar/Vender", json=data)
        
    async def suscribir_fci(
        self,
        simbolo: str,
        monto: float,
        solo_validar: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Suscribe un FCI
        
        Args:
            simbolo: Símbolo del FCI
            monto: Monto a suscribir
            solo_validar: Indica si solo se debe validar la operación sin ejecutarla (opcional)
        """
        data = {
            "simbolo": simbolo,
            "monto": monto
        }
        
        if solo_validar is not None:
            data["soloValidar"] = solo_validar
            
        return await self.post("/api/v2/operar/suscripcion/fci", json=data)
        
    async def rescatar_fci(
        self,
        simbolo: str,
        cantidad: float,
        solo_validar: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Rescata un FCI
        
        Args:
            simbolo: Símbolo del FCI
            cantidad: Cantidad a rescatar
            solo_validar: Indica si solo se debe validar la operación sin ejecutarla (opcional)
        """
        data = {
            "simbolo": simbolo,
            "cantidad": cantidad
        }
        
        if solo_validar is not None:
            data["soloValidar"] = solo_validar
            
        return await self.post("/api/v2/operar/rescate/fci", json=data)
        
    async def cpd_puede_operar(self) -> Dict[str, Any]:
        """
        Verifica si el usuario puede operar con cheques de pago diferido
        
        Returns:
            Dict[str, Any]: Objeto CPDPuedeOperarModel con la información de si puede operar
        """
        return await self.get("/api/v2/operar/CPD/PuedeOperar")
        
    async def obtener_cpd(
        self,
        estado: str,
        segmento: str
    ) -> Dict[str, Any]:
        """
        Obtiene los cheques de pago diferido según estado y segmento
        
        Args:
            estado: Estado de los cheques
            segmento: Segmento de los cheques
            
        Returns:
            Dict[str, Any]: Objeto CPDModel con la información de los cheques
        """
        return await self.get(f"/api/v2/operar/CPD/{estado}/{segmento}")
        
    async def calcular_comisiones_cpd(
        self,
        importe: float,
        plazo: int,
        tasa: float
    ) -> Dict[str, Any]:
        """
        Calcula las comisiones para un cheque de pago diferido
        
        Args:
            importe: Importe del cheque
            plazo: Plazo en días
            tasa: Tasa de descuento
            
        Returns:
            Dict[str, Any]: Objeto ComisionCPDDTO con la información de las comisiones
        """
        return await self.get(f"/api/v2/operar/CPD/Comisiones/{importe}/{plazo}/{tasa}")
        
    async def operar_cpd(
        self,
        id_subasta: int,
        tasa: float,
        fuente: str
    ) -> Dict[str, Any]:
        """
        Realiza una operación con un cheque de pago diferido
        
        Args:
            id_subasta: ID de la subasta
            tasa: Tasa de descuento
            fuente: Fuente de la operación
            
        Returns:
            Dict[str, Any]: Objeto CPDTransaccionFinalModel con el resultado de la operación
        """
        data = {
            "idSubasta": id_subasta,
            "tasa": tasa,
            "fuente": fuente
        }
        return await self.post("/api/v2/operar/CPD", json=data)
        
    async def generar_token(
        self,
        mercado: Optional[str] = None,
        simbolo: Optional[str] = None,
        cantidad: Optional[float] = None,
        monto: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Genera un token para operaciones
        
        Args:
            mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX) (opcional)
            simbolo: Símbolo del título (opcional)
            cantidad: Cantidad (opcional)
            monto: Monto (opcional)
            
        Returns:
            Dict[str, Any]: Objeto JWTResultDTO con el token generado
        """
        data = {}
        if mercado:
            data["mercado"] = mercado
        if simbolo:
            data["simbolo"] = simbolo
        if cantidad is not None:
            data["cantidad"] = cantidad
        if monto is not None:
            data["monto"] = monto
            
        return await self.post("/api/v2/operar/Token", json=data)
        
    async def vender_especie_d(
        self,
        mercado: str,
        simbolo: str,
        cantidad: float,
        precio: float,
        validez: str,
        id_cuenta_bancaria: int,
        tipo_orden: Optional[str] = None,
        plazo: Optional[str] = None,
        id_fuente: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Crea una orden de venta de especie D
        
        Args:
            mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
            simbolo: Símbolo del título
            cantidad: Cantidad a vender
            precio: Precio de venta
            validez: Fecha de validez de la orden en formato ISO
            id_cuenta_bancaria: ID de la cuenta bancaria
            tipo_orden: Tipo de orden (precioLimite, precioMercado) (opcional)
            plazo: Plazo de la operación (t0, t1, t2, t3) (opcional)
            id_fuente: ID de la fuente (opcional)
            
        Returns:
            Dict[str, Any]: Objeto ResponseModel con el resultado de la operación
        """
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "cantidad": cantidad,
            "precio": precio,
            "validez": validez,
            "idCuentaBancaria": id_cuenta_bancaria
        }
        
        if tipo_orden:
            data["tipoOrden"] = tipo_orden
        if plazo:
            data["plazo"] = plazo
        if id_fuente is not None:
            data["idFuente"] = id_fuente
            
        return await self.post("/api/v2/operar/VenderEspecieD", json=data)
        
    async def comprar_especie_d(
        self,
        mercado: str,
        simbolo: str,
        precio: float,
        plazo: str,
        validez: Optional[str] = None,
        cantidad: Optional[float] = None,
        tipo_orden: Optional[str] = None,
        monto: Optional[float] = None,
        id_fuente: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Crea una orden de compra de especie D
        
        Args:
            mercado: Mercado del título (bCBA, nYSE, nASDAQ, aMEX, bCS, rOFX)
            simbolo: Símbolo del título
            precio: Precio de compra
            plazo: Plazo de la operación (t0, t1, t2, t3)
            validez: Fecha de validez de la orden en formato ISO
            cantidad: Cantidad a comprar (opcional)
            tipo_orden: Tipo de orden (precioLimite, precioMercado) (opcional)
            monto: Monto efectivo a invertir (opcional)
            id_fuente: ID de la fuente (opcional)
            
        Returns:
            Dict[str, Any]: Objeto ResponseModel con el resultado de la operación
        """
        # Si no se proporciona validez, usar fecha a 3 meses
        if validez is None:
            validez = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%dT23:59:59")
            
        data = {
            "mercado": mercado,
            "simbolo": simbolo,
            "precio": precio,
            "plazo": plazo,
            "validez": validez
        }
        
        if cantidad is not None:
            data["cantidad"] = cantidad
        if tipo_orden:
            data["tipoOrden"] = tipo_orden
        if monto is not None:
            data["monto"] = monto
        if id_fuente is not None:
            data["idFuente"] = id_fuente
            
        return await self.post("/api/v2/operar/ComprarEspecieD", json=data) 