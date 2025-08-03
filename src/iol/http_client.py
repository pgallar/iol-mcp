from typing import Dict, Any, Optional
import os
import logging
import aiohttp
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class IOLAPIClient:
    """Cliente base para la API de InvertirOnline"""
    
    def __init__(self):
        """Inicializa el cliente de la API"""
        self.base_url = "https://api.invertironline.com"
        self.access_token = None
        self.token_expiry = None
        self.username = os.getenv('IOL_USERNAME')
        self.password = os.getenv('IOL_PASSWORD')

    async def ensure_token(self) -> None:
        """Asegura que haya un token válido para las llamadas a la API"""
        if not self.access_token or not self.token_expiry or datetime.now() >= self.token_expiry:
            await self.authenticate()

    async def authenticate(self) -> None:
        """Obtiene un nuevo token de acceso"""
        auth_data = {
            "username": self.username,
            "password": self.password,
            "grant_type": "password"
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/token",
                    data=auth_data,
                    headers={"Content-Type": "application/x-www-form-urlencoded"}
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        logger.error(f"Error de autenticación: {response.status} - {error_text}")
                        raise Exception(f"Error de autenticación: {response.status}")
                        
                    data = await response.json()
                    self.access_token = data["access_token"]
                    # Restamos 5 minutos para asegurar renovación antes de expiración
                    self.token_expiry = datetime.now() + timedelta(seconds=int(data["expires_in"])) - timedelta(minutes=5)
                    logger.info("Token de acceso obtenido exitosamente")
        except Exception as e:
            logger.error(f"Error durante la autenticación: {str(e)}")
            raise

    def get_auth_headers(self) -> Dict[str, str]:
        """
        Obtiene los headers de autenticación
        
        Returns:
            Dict[str, str]: Headers de autenticación
        """
        if not self.access_token:
            raise ValueError("No hay token de acceso disponible")
            
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    async def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Realiza una petición a la API
        
        Args:
            method: Método HTTP
            endpoint: Endpoint de la API
            params: Parámetros de la petición
            json: Datos JSON de la petición
            
        Returns:
            Dict[str, Any]: Respuesta de la API
        """
        await self.ensure_token()
        
        # Asegurarse de que el endpoint comience con /
        if not endpoint.startswith("/"):
            endpoint = f"/{endpoint}"
            
        url = f"{self.base_url}{endpoint}"
        headers = self.get_auth_headers()
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.request(
                    method,
                    url,
                    headers=headers,
                    params=params,
                    json=json
                ) as response:
                    if response.status == 401:
                        # Token expirado, renovar y reintentar
                        logger.info("Token expirado, renovando...")
                        await self.authenticate()
                        headers = self.get_auth_headers()
                        async with session.request(
                            method,
                            url,
                            headers=headers,
                            params=params,
                            json=json
                        ) as retry_response:
                            if retry_response.status not in [200, 201]:
                                error_text = await retry_response.text()
                                logger.error(f"Error en la petición: {retry_response.status} - {error_text}")
                                raise Exception(f"Error en la petición: {retry_response.status} - {error_text}")
                            return await retry_response.json()
                            
                    if response.status not in [200, 201]:
                        error_text = await response.text()
                        logger.error(f"Error en la petición: {response.status} - {error_text}")
                        raise Exception(f"Error en la petición: {response.status} - {error_text}")
                        
                    return await response.json()
        except Exception as e:
            logger.error(f"Error realizando petición: {str(e)}")
            raise

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Realiza una petición GET"""
        return await self._make_request("GET", endpoint, params=params)

    async def post(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        """Realiza una petición POST"""
        return await self._make_request("POST", endpoint, json=json)

    async def put(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        """Realiza una petición PUT"""
        return await self._make_request("PUT", endpoint, json=json)

    async def delete(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Realiza una petición DELETE"""
        return await self._make_request("DELETE", endpoint, params=params) 