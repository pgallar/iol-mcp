from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class OperatoriaSimplificadaClient(IOLAPIClient):
    async def obtener_operatoria_simplificada(self) -> Dict[str, Any]:
        """Obtiene la configuración de operatoria simplificada"""
        return await self.get("/api/v2/OperatoriaSimplificada")

    async def actualizar_operatoria_simplificada(
        self,
        operatoria_simplificada: bool
    ) -> Dict[str, Any]:
        """
        Actualiza la configuración de operatoria simplificada
        
        Args:
            operatoria_simplificada: Estado de la operatoria simplificada
        """
        data = {
            "operatoriaSimplificada": operatoria_simplificada
        }
        return await self.put("/api/v2/OperatoriaSimplificada", json=data) 