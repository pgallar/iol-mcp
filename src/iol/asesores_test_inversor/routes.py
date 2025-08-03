from typing import Dict, Any, Optional, List, Union
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import AsesoresTestInversorClient

class RespuestasAsesorTestInversorBindingModel(BaseModel):
    """Modelo para las respuestas del test de inversor para asesores"""
    enviarEmailCliente: Optional[bool] = Field(default=None, description="Indica si se debe enviar email al cliente")
    instrumentosInvertidosAnteriormente: Optional[List[int]] = Field(default=None, description="IDs de instrumentos invertidos anteriormente")
    nivelesConocimientoInstrumentos: Optional[List[int]] = Field(default=None, description="IDs de niveles de conocimiento de instrumentos")
    idPlazoElegido: int = Field(description="ID del plazo elegido")
    idEdadElegida: int = Field(description="ID de la edad elegida")
    idObjetivoInversionElegida: int = Field(description="ID del objetivo de inversión elegido")
    idPolizaElegida: int = Field(description="ID de la póliza elegida")
    idCapacidadAhorroElegida: int = Field(description="ID de la capacidad de ahorro elegida")
    idPorcentajePatrimonioDedicado: int = Field(description="ID del porcentaje de patrimonio dedicado")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class AsesoresTestInversorRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = AsesoresTestInversorClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_test_inversor_asesor",
            description="Obtener preguntas del test de inversor para asesores",
            tags=["asesores", "test_inversor"]
        )
        async def obtener_test_inversor() -> Dict[str, Any]:
            """
            Obtiene las preguntas del test de inversor para asesores
            
            Returns:
                Dict[str, Any]: Objeto con las preguntas del test
            """
            try:
                result = await self.client.obtener_test_inversor()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo preguntas del test de inversor: {str(e)}"}
                
        @mcp.tool(
            name="calcular_perfil_sin_guardar",
            description="Calcular perfil del inversor sin guardar los resultados",
            tags=["asesores", "test_inversor", "perfil"]
        )
        async def calcular_perfil_sin_guardar(
            request: RespuestasAsesorTestInversorBindingModel = Field(
                description="Datos con las respuestas del test de inversor",
                example={
                    "enviarEmailCliente": True,
                    "instrumentosInvertidosAnteriormente": [1, 2, 3],
                    "nivelesConocimientoInstrumentos": [1, 2, 3],
                    "idPlazoElegido": 1,
                    "idEdadElegida": 2,
                    "idObjetivoInversionElegida": 3,
                    "idPolizaElegida": 1,
                    "idCapacidadAhorroElegida": 2,
                    "idPorcentajePatrimonioDedicado": 3
                }
            )
        ) -> Dict[str, Any]:
            """
            Calcula el perfil del inversor sin guardar los resultados
            
            Args:
                request: Datos con las respuestas del test de inversor
                
            Returns:
                Dict[str, Any]: Objeto con el perfil calculado
            """
            try:
                result = await self.client.calcular_perfil_sin_guardar(
                    respuesta_inversor=request.model_dump(exclude_none=True)
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error calculando perfil sin guardar: {str(e)}"}
                
        @mcp.tool(
            name="calcular_perfil_asesorado",
            description="Calcular y guardar perfil del inversor para un cliente asesorado",
            tags=["asesores", "test_inversor", "perfil"]
        )
        async def calcular_perfil(
            id_cliente_asesorado: int = Field(description="ID del cliente asesorado"),
            request: RespuestasAsesorTestInversorBindingModel = Field(
                description="Datos con las respuestas del test de inversor",
                example={
                    "enviarEmailCliente": True,
                    "instrumentosInvertidosAnteriormente": [1, 2, 3],
                    "nivelesConocimientoInstrumentos": [1, 2, 3],
                    "idPlazoElegido": 1,
                    "idEdadElegida": 2,
                    "idObjetivoInversionElegida": 3,
                    "idPolizaElegida": 1,
                    "idCapacidadAhorroElegida": 2,
                    "idPorcentajePatrimonioDedicado": 3
                }
            )
        ) -> Dict[str, Any]:
            """
            Calcula y guarda el perfil del inversor para un cliente asesorado
            
            Args:
                id_cliente_asesorado: ID del cliente asesorado
                request: Datos con las respuestas del test de inversor
                
            Returns:
                Dict[str, Any]: Objeto con el perfil calculado
            """
            try:
                result = await self.client.calcular_perfil(
                    id_cliente_asesorado=id_cliente_asesorado,
                    respuesta_inversor=request.model_dump(exclude_none=True)
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error calculando perfil: {str(e)}"} 