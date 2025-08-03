from typing import Dict, Any, Optional, List
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import AsesoresClient

class MovementBindingModel(BaseModel):
    """Modelo para la consulta de movimientos históricos según el swagger de IOL"""
    clientes: Optional[List[int]] = Field(default=None, description="Lista de IDs de clientes asesorados")
    from_: str = Field(alias="from", description="Fecha desde en formato ISO")
    to: str = Field(description="Fecha hasta en formato ISO")
    dateType: str = Field(description="Tipo de fecha para filtrar")
    status: str = Field(description="Estado de los movimientos")
    type: Optional[str] = Field(default=None, description="Tipo de movimiento")
    country: str = Field(description="País de los movimientos")
    currency: Optional[str] = Field(default=None, description="Moneda de los movimientos")
    cuentaComitente: Optional[str] = Field(default=None, description="Cuenta comitente")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True, populate_by_name=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class AsesoresRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = AsesoresClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="guardar_movimientos_historicos_asesor",
            description="Consultar o guardar movimientos históricos de clientes asesorados",
            tags=["asesores", "movimientos", "historicos"]
        )
        async def guardar_movimientos_historicos(
            request: MovementBindingModel = Field(
                description="Datos para consultar o guardar los movimientos históricos",
                example={
                    "clientes": [12345, 67890],
                    "from": "2023-01-01T00:00:00",
                    "to": "2023-12-31T23:59:59",
                    "dateType": "Operacion",
                    "status": "Todos",
                    "type": "Compra",
                    "country": "argentina",
                    "currency": "ARS",
                    "cuentaComitente": "123456"
                }
            )
        ) -> Dict[str, Any]:
            """
            Consulta o guarda los movimientos históricos de clientes asesorados
            
            Args:
                request: Datos para consultar o guardar los movimientos históricos
            """
            try:
                # Convertir el modelo a diccionario y manejar el campo 'from_'
                request_dict = request.model_dump(exclude_none=True, by_alias=True)
                
                result = await self.client.guardar_movimientos_historicos(
                    clientes=request.clientes,
                    fecha_desde=getattr(request, 'from_'),
                    fecha_hasta=request.to,
                    tipo_fecha=request.dateType,
                    estado=request.status,
                    tipo=request.type,
                    pais=request.country,
                    moneda=request.currency,
                    cuenta_comitente=request.cuentaComitente
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error procesando movimientos históricos: {str(e)}"} 