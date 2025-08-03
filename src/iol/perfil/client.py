from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class PerfilClient(IOLAPIClient):
    async def obtener_perfil(self) -> Dict[str, Any]:
        """Obtiene el perfil del usuario"""
        return await self.get("/api/v2/Perfil")

    async def obtener_test_inversor(self) -> Dict[str, Any]:
        """Obtiene el test de inversor del usuario"""
        return await self.get("/api/v2/Perfil/TestInversor")

    async def guardar_test_inversor(
        self,
        respuestas: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Guarda las respuestas del test de inversor
        
        Args:
            respuestas: Lista de respuestas del test
        """
        return await self.post("/api/v2/Perfil/TestInversor", json=respuestas)

    async def obtener_preguntas_test_inversor(self) -> Dict[str, Any]:
        """Obtiene las preguntas del test de inversor"""
        return await self.get("/api/v2/Perfil/TestInversor/Preguntas")
        
    async def actualizar_perfil(
        self,
        datos_perfil: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Actualiza el perfil del usuario
        
        Args:
            datos_perfil: Datos del perfil a actualizar
        """
        return await self.put("/api/v2/Perfil", json=datos_perfil)
        
    async def cambiar_clave(
        self,
        clave_actual: str,
        clave_nueva: str
    ) -> Dict[str, Any]:
        """
        Cambia la clave del usuario
        
        Args:
            clave_actual: Clave actual
            clave_nueva: Nueva clave
        """
        data = {
            "claveActual": clave_actual,
            "claveNueva": clave_nueva
        }
        return await self.post("/api/v2/Perfil/CambiarClave", json=data) 