from typing import Dict, Any, Optional, List
from ..http_client import IOLAPIClient

class TitulosClient(IOLAPIClient):
    async def obtener_cotizacion(
        self,
        simbolo: str,
        mercado: str,
        plazo: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene la cotización de un título
        
        Args:
            simbolo: Símbolo del título
            mercado: Mercado del título (bcba, nyse, nasdaq, etc)
            plazo: Plazo de la cotización (t0, t1, t2)
        """
        endpoint = f"/api/v2/Titulos/{mercado}/{simbolo}/cotizacion"
        if plazo:
            endpoint += f"/{plazo}"
        return await self.get(endpoint)

    async def obtener_panel(
        self,
        instrumento: str,
        panel: str,
        pais: str
    ) -> Dict[str, Any]:
        """
        Obtiene el panel de un instrumento
        
        Args:
            instrumento: Tipo de instrumento (Acciones, Bonos, Opciones, etc)
            panel: Tipo de panel (Líderes, General, etc)
            pais: País del panel (argentina, estados_unidos, etc)
        """
        return await self.get(f"/api/v2/Titulos/Cotizacion/panel/{instrumento}/{panel}/{pais}")

    async def obtener_opciones(
        self,
        simbolo: str,
        mercado: str
    ) -> Dict[str, Any]:
        """
        Obtiene las opciones de un título
        
        Args:
            simbolo: Símbolo del título
            mercado: Mercado del título (bcba, nyse, nasdaq, etc)
        """
        return await self.get(f"/api/v2/Titulos/Opciones/{mercado}/{simbolo}")

    async def obtener_puntas(
        self,
        simbolo: str,
        mercado: str,
        plazo: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Obtiene las puntas de un título
        
        Args:
            simbolo: Símbolo del título
            mercado: Mercado del título (bcba, nyse, nasdaq, etc)
            plazo: Plazo de la cotización (t0, t1, t2)
        """
        endpoint = f"/api/v2/Titulos/{mercado}/{simbolo}/Puntas"
        if plazo:
            endpoint += f"/{plazo}"
        return await self.get(endpoint) 