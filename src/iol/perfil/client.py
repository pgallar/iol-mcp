from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class PerfilClient(IOLAPIClient):
    async def obtener_perfil(self) -> Dict[str, Any]:
        """Obtiene el perfil del usuario"""
        return await self.get("/Perfil")

    async def obtener_test_inversor(self) -> Dict[str, Any]:
        """Obtiene el test de inversor del usuario"""
        return await self.get("/Perfil/TestInversor")

    async def guardar_test_inversor(
        self,
        respuestas: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Guarda las respuestas del test de inversor
        
        Args:
            respuestas: Lista de respuestas del test
        """
        return await self.post("/Perfil/TestInversor", json=respuestas)

    async def obtener_preguntas_test_inversor(self) -> Dict[str, Any]:
        """Obtiene las preguntas del test de inversor"""
        return await self.get("/Perfil/TestInversor/Preguntas") 