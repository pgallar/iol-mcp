from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class AsesoresTestInversorClient(IOLAPIClient):
    async def obtener_test_inversor(self) -> Dict[str, Any]:
        """
        Obtiene las preguntas del test de inversor para asesores
        
        Returns:
            Dict[str, Any]: Objeto PreguntasAsesoresTestInversorResponseModel con las preguntas del test
        """
        return await self.get("/api/v2/asesores/test-inversor")
    
    async def calcular_perfil_sin_guardar(
        self,
        respuesta_inversor: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Calcula el perfil del inversor sin guardar los resultados
        
        Args:
            respuesta_inversor: Objeto RespuestasAsesorTestInversorBindingModel con las respuestas del test
            
        Returns:
            Dict[str, Any]: Objeto PerfilCalculadoResponseModel con el perfil calculado
        """
        return await self.post("/api/v2/asesores/test-inversor", json=respuesta_inversor)
    
    async def calcular_perfil(
        self,
        id_cliente_asesorado: int,
        respuesta_inversor: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Calcula y guarda el perfil del inversor para un cliente asesorado
        
        Args:
            id_cliente_asesorado: ID del cliente asesorado
            respuesta_inversor: Objeto RespuestasAsesorTestInversorBindingModel con las respuestas del test
            
        Returns:
            Dict[str, Any]: Objeto PerfilCalculadoResponseModel con el perfil calculado
        """
        return await self.post(f"/api/v2/asesores/test-inversor/{id_cliente_asesorado}", json=respuesta_inversor) 