from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class MiCuentaClient(IOLAPIClient):
    async def obtener_estado_cuenta(self) -> Dict[str, Any]:
        """
        Obtiene el estado de cuenta del usuario
        
        Returns:
            Dict[str, Any]: Objeto EstadoCuentaModel con información de cuentas, estadísticas y total en pesos
        """
        return await self.get("/api/v2/estadocuenta")
        
    async def obtener_portafolio(
        self,
        pais: str
    ) -> Dict[str, Any]:
        """
        Obtiene el portafolio del usuario para un país específico
        
        Args:
            pais: País del portafolio (argentina, estados_unidos)
            
        Returns:
            Dict[str, Any]: Objeto PortafolioModel con la información del portafolio
        """
        return await self.get(f"/api/v2/portafolio/{pais}")
        
    async def obtener_operacion(
        self,
        numero: int
    ) -> Dict[str, Any]:
        """
        Obtiene el detalle de una operación específica
        
        Args:
            numero: Número de la operación
            
        Returns:
            Dict[str, Any]: Objeto OperacionDetalleModel con el detalle de la operación
        """
        return await self.get(f"/api/v2/operaciones/{numero}")
        
    async def cancelar_operacion(
        self,
        numero: int
    ) -> Dict[str, Any]:
        """
        Cancela una operación específica
        
        Args:
            numero: Número de la operación a cancelar
            
        Returns:
            Dict[str, Any]: Objeto ResponseModel con el resultado de la cancelación
        """
        return await self.delete(f"/api/v2/operaciones/{numero}")
        
    async def obtener_operaciones(
        self,
        numero: Optional[int] = None,
        estado: Optional[str] = None,
        fecha_desde: Optional[str] = None,
        fecha_hasta: Optional[str] = None,
        pais: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Obtiene las operaciones del usuario según los filtros especificados
        
        Args:
            numero: Número de operación para filtrar
            estado: Estado de las operaciones (todas, pendientes, terminadas, canceladas)
            fecha_desde: Fecha desde en formato ISO
            fecha_hasta: Fecha hasta en formato ISO
            pais: País de las operaciones (argentina, estados_unidos)
            
        Returns:
            List[Dict[str, Any]]: Lista de objetos OperacionModel con las operaciones
        """
        params = {}
        if numero is not None:
            params["filtro.numero"] = numero
        if estado:
            params["filtro.estado"] = estado
        if fecha_desde:
            params["filtro.fechaDesde"] = fecha_desde
        if fecha_hasta:
            params["filtro.fechaHasta"] = fecha_hasta
        if pais:
            params["filtro.pais"] = pais
            
        return await self.get("/api/v2/operaciones", params=params) 