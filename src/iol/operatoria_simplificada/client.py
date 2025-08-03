from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class OperatoriaSimplificadaClient(IOLAPIClient):
    async def obtener_montos_estimados(
        self,
        monto: float
    ) -> Dict[str, Any]:
        """
        Obtiene los montos estimados para una operación simplificada
        
        Args:
            monto: Monto de la operación
            
        Returns:
            Dict[str, Any]: Objeto MontosEstimadosDTO con la información de los montos estimados
        """
        return await self.get(f"/api/v2/OperatoriaSimplificada/MontosEstimados/{monto}")
    
    async def obtener_parametros_operatoria(
        self,
        id_tipo_operatoria: int
    ) -> Dict[str, Any]:
        """
        Obtiene los parámetros para un tipo de operatoria simplificada
        
        Args:
            id_tipo_operatoria: ID del tipo de operatoria
            
        Returns:
            Dict[str, Any]: Objeto ParametrosMepSimpleDTO con la información de los parámetros
        """
        return await self.get(f"/api/v2/OperatoriaSimplificada/{id_tipo_operatoria}/Parametros")
    
    async def validar_operatoria(
        self,
        monto: float,
        id_tipo_operatoria: int
    ) -> Dict[str, Any]:
        """
        Valida una operación simplificada
        
        Args:
            monto: Monto de la operación
            id_tipo_operatoria: ID del tipo de operatoria
            
        Returns:
            Dict[str, Any]: Objeto ResponseModel con el resultado de la validación
        """
        return await self.get(f"/api/v2/OperatoriaSimplificada/Validar/{monto}/{id_tipo_operatoria}")
    
    async def obtener_montos_estimados_venta_mep(
        self,
        monto: float
    ) -> Dict[str, Any]:
        """
        Obtiene los montos estimados para una venta MEP simple
        
        Args:
            monto: Monto de la operación
            
        Returns:
            Dict[str, Any]: Objeto MontosEstimadosVentaMepDTO con la información de los montos estimados
        """
        return await self.get(f"/api/v2/OperatoriaSimplificada/VentaMepSimple/MontosEstimados/{monto}")
        
    async def obtener_valor_referencia_mep(
        self,
        simbolo: str,
        id_plazo_operatoria_compra: int,
        id_plazo_operatoria_venta: int
    ) -> float:
        """
        Obtiene el valor de referencia MEP para una cotización
        
        Args:
            simbolo: Símbolo del título
            id_plazo_operatoria_compra: ID del plazo de operatoria de compra
            id_plazo_operatoria_venta: ID del plazo de operatoria de venta
            
        Returns:
            float: Valor de referencia MEP
        """
        data = {
            "simbolo": simbolo,
            "idPlazoOperatoriaCompra": id_plazo_operatoria_compra,
            "idPlazoOperatoriaVenta": id_plazo_operatoria_venta
        }
        return await self.post("/api/v2/Cotizaciones/MEP", json=data)
        
    async def crear_compra_operatoria_simplificada(
        self,
        monto: float,
        id_tipo_operatoria_simplificada: int,
        id_cuenta_bancaria: int
    ) -> Dict[str, Any]:
        """
        Crea una compra de operatoria simplificada
        
        Args:
            monto: Monto de la operación
            id_tipo_operatoria_simplificada: ID del tipo de operatoria simplificada
            id_cuenta_bancaria: ID de la cuenta bancaria
            
        Returns:
            Dict[str, Any]: Objeto ResponseModel con el resultado de la operación
        """
        data = {
            "monto": monto,
            "idTipoOperatoriaSimplificada": id_tipo_operatoria_simplificada,
            "idCuentaBancaria": id_cuenta_bancaria
        }
        return await self.post("/api/v2/OperatoriaSimplificada/Comprar", json=data) 