from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class AsesoresTestInversorClient(IOLAPIClient):
    async def obtener_test_inversor(self, id_cliente: int) -> Dict[str, Any]:
        """Obtiene el test de inversor de un cliente"""
        return await self.get(f"/api/v2/AsesoresTestInversor/Clientes/{id_cliente}")

    async def obtener_preguntas(self) -> Dict[str, Any]:
        """Obtiene las preguntas del test de inversor"""
        return await self.get("/api/v2/AsesoresTestInversor/Preguntas")

    async def guardar_test_inversor(
        self,
        id_cliente: int,
        respuestas: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Guarda las respuestas del test de inversor de un cliente"""
        return await self.post(f"/api/v2/AsesoresTestInversor/Clientes/{id_cliente}", json=respuestas) 