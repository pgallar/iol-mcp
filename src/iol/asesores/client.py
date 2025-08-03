from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class AsesoresClient(IOLAPIClient):
    async def guardar_movimientos_historicos(
        self,
        clientes: Optional[List[int]] = None,
        fecha_desde: str = None,
        fecha_hasta: str = None,
        tipo_fecha: str = None,
        estado: str = None,
        tipo: Optional[str] = None,
        pais: str = None,
        moneda: Optional[str] = None,
        cuenta_comitente: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Guarda o consulta los movimientos históricos de clientes asesorados
        
        Args:
            clientes: Lista de IDs de clientes asesorados
            fecha_desde: Fecha desde en formato ISO (requerido)
            fecha_hasta: Fecha hasta en formato ISO (requerido)
            tipo_fecha: Tipo de fecha para filtrar (requerido)
            estado: Estado de los movimientos (requerido)
            tipo: Tipo de movimiento (opcional)
            pais: País de los movimientos (requerido)
            moneda: Moneda de los movimientos (opcional)
            cuenta_comitente: Cuenta comitente (opcional)
        """
        request_model = {
            "from": fecha_desde,
            "to": fecha_hasta,
            "dateType": tipo_fecha,
            "status": estado,
            "country": pais
        }
        
        if clientes:
            request_model["clientes"] = clientes
        if tipo:
            request_model["type"] = tipo
        if moneda:
            request_model["currency"] = moneda
        if cuenta_comitente:
            request_model["cuentaComitente"] = cuenta_comitente
            
        return await self.post("/api/v2/Asesor/Movimientos", json=request_model) 