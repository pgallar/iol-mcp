from typing import Dict, Any, Optional
from ..http_client import IOLAPIClient

class MiCuentaClient(IOLAPIClient):
    async def obtener_estado_cuenta(self) -> Dict[str, Any]:
        """
        Obtiene el estado de cuenta del usuario
        """
        return await self.get("/api/v2/MiCuenta/EstadoCuenta")

    async def obtener_saldos(self) -> Dict[str, Any]:
        """
        Obtiene los saldos del usuario
        """
        return await self.get("/api/v2/MiCuenta/Saldos")

    async def obtener_movimientos(
        self,
        pais: Optional[str] = None,
        tipo_movimiento: Optional[str] = None,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene los movimientos de cuenta del usuario
        
        Args:
            pais: País de los movimientos (argentina, estados_unidos, etc)
            tipo_movimiento: Tipo de movimiento (deposito, extraccion, etc)
            fecha_desde: Fecha de inicio en formato YYYY-MM-DD
            fecha_hasta: Fecha de fin en formato YYYY-MM-DD
        """
        endpoint = "/api/v2/MiCuenta/Movimientos"
        params = {}
        if pais:
            params["pais"] = pais
        if tipo_movimiento:
            params["tipoMovimiento"] = tipo_movimiento
        if fecha_desde:
            params["fechaDesde"] = fecha_desde
        if fecha_hasta:
            params["fechaHasta"] = fecha_hasta
        return await self.get(endpoint, params=params)

    async def obtener_movimientos_fondos(
        self,
        pais: Optional[str] = None,
        tipo_movimiento: Optional[str] = None,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene los movimientos de fondos del usuario
        
        Args:
            pais: País de los movimientos (argentina, estados_unidos, etc)
            tipo_movimiento: Tipo de movimiento (deposito, extraccion, etc)
            fecha_desde: Fecha de inicio en formato YYYY-MM-DD
            fecha_hasta: Fecha de fin en formato YYYY-MM-DD
        """
        endpoint = "/api/v2/MiCuenta/Movimientos/Fondos"
        params = {}
        if pais:
            params["pais"] = pais
        if tipo_movimiento:
            params["tipoMovimiento"] = tipo_movimiento
        if fecha_desde:
            params["fechaDesde"] = fecha_desde
        if fecha_hasta:
            params["fechaHasta"] = fecha_hasta
        return await self.get(endpoint, params=params)

    async def obtener_movimientos_fci(
        self,
        pais: Optional[str] = None,
        tipo_movimiento: Optional[str] = None,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene los movimientos de FCI del usuario
        
        Args:
            pais: País de los movimientos (argentina, estados_unidos, etc)
            tipo_movimiento: Tipo de movimiento (suscripcion, rescate, etc)
            fecha_desde: Fecha de inicio en formato YYYY-MM-DD
            fecha_hasta: Fecha de fin en formato YYYY-MM-DD
        """
        endpoint = "/api/v2/MiCuenta/Movimientos/FCI"
        params = {}
        if pais:
            params["pais"] = pais
        if tipo_movimiento:
            params["tipoMovimiento"] = tipo_movimiento
        if fecha_desde:
            params["fechaDesde"] = fecha_desde
        if fecha_hasta:
            params["fechaHasta"] = fecha_hasta
        return await self.get(endpoint, params=params)
        
    async def obtener_cuentas_bancarias(self) -> Dict[str, Any]:
        """
        Obtiene las cuentas bancarias del usuario
        """
        return await self.get("/api/v2/MiCuenta/CuentasBancarias")
        
    async def obtener_cuentas_comitentes(self) -> Dict[str, Any]:
        """
        Obtiene las cuentas comitentes del usuario
        """
        return await self.get("/api/v2/MiCuenta/CuentasComitentes")
        
    async def obtener_resumen_cuenta(
        self,
        pais: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene el resumen de cuenta del usuario
        
        Args:
            pais: País del resumen (argentina, estados_unidos, etc)
        """
        endpoint = "/api/v2/MiCuenta/ResumenCuenta"
        params = {}
        if pais:
            params["pais"] = pais
        return await self.get(endpoint, params=params)
        
    async def obtener_detalle_movimiento(
        self,
        id_movimiento: int
    ) -> Dict[str, Any]:
        """
        Obtiene el detalle de un movimiento específico
        
        Args:
            id_movimiento: ID del movimiento
        """
        return await self.get(f"/api/v2/MiCuenta/Movimientos/{id_movimiento}")
        
    async def solicitar_extraccion(
        self,
        monto: float,
        id_cuenta_bancaria: int,
        moneda: str
    ) -> Dict[str, Any]:
        """
        Solicita una extracción de fondos
        
        Args:
            monto: Monto a extraer
            id_cuenta_bancaria: ID de la cuenta bancaria destino
            moneda: Moneda de la extracción (ARS, USD, etc)
        """
        data = {
            "monto": monto,
            "idCuentaBancaria": id_cuenta_bancaria,
            "moneda": moneda
        }
        return await self.post("/api/v2/MiCuenta/SolicitarExtraccion", json=data) 