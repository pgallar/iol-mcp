from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class PerfilClient(IOLAPIClient):
    async def obtener_datos_perfil(self) -> Dict[str, Any]:
        """
        Obtiene los datos del perfil del cliente
        
        Returns:
            Dict[str, Any]: Objeto PerfilClienteModel con la información del perfil
        """
        return await self.get("/api/v2/datos-perfil") 