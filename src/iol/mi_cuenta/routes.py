from typing import Dict, Any, List, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import MiCuentaClient

class CuentaModel(BaseModel):
    """Modelo para representar una cuenta según el esquema EstadoCuentaModel"""
    # Aquí se definirían los campos específicos de CuentaModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)

class EstadisticaModel(BaseModel):
    """Modelo para representar una estadística según el esquema EstadoCuentaModel"""
    # Aquí se definirían los campos específicos de EstadisticaModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)

class EstadoCuentaModel(BaseModel):
    """Modelo para representar el estado de cuenta según el swagger"""
    cuentas: Optional[List[CuentaModel]] = Field(default=None, description="Lista de cuentas del usuario")
    estadisticas: Optional[List[EstadisticaModel]] = Field(default=None, description="Lista de estadísticas de la cuenta")
    totalEnPesos: Optional[float] = Field(default=None, description="Total en pesos")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class PortafolioModel(BaseModel):
    """Modelo para representar el portafolio según el swagger"""
    # Aquí se definirían los campos específicos de PortafolioModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)

class OperacionDetalleModel(BaseModel):
    """Modelo para representar el detalle de una operación según el swagger"""
    # Aquí se definirían los campos específicos de OperacionDetalleModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)

class ResponseModel(BaseModel):
    """Modelo para representar la respuesta de cancelación según el swagger"""
    # Aquí se definirían los campos específicos de ResponseModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)

class OperacionModel(BaseModel):
    """Modelo para representar una operación según el swagger"""
    # Aquí se definirían los campos específicos de OperacionModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)

class MiCuentaRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = MiCuentaClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_estado_cuenta",
            description="Obtener estado de cuenta del usuario",
            tags=["mi_cuenta", "estado"]
        )
        async def obtener_estado_cuenta() -> Dict[str, Any]:
            """
            Obtiene el estado de cuenta del usuario
            
            Returns:
                Dict[str, Any]: Objeto con información de cuentas, estadísticas y total en pesos
            """
            try:
                result = await self.client.obtener_estado_cuenta()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo estado de cuenta: {str(e)}"}
                
        @mcp.tool(
            name="obtener_portafolio",
            description="Obtener portafolio del usuario para un país específico",
            tags=["mi_cuenta", "portafolio"]
        )
        async def obtener_portafolio(
            pais: str = Field(description="País del portafolio", enum=["argentina", "estados_unidos"])
        ) -> Dict[str, Any]:
            """
            Obtiene el portafolio del usuario para un país específico
            
            Args:
                pais: País del portafolio (argentina, estados_unidos)
                
            Returns:
                Dict[str, Any]: Objeto con la información del portafolio
            """
            try:
                result = await self.client.obtener_portafolio(pais=pais)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo portafolio: {str(e)}"}
                
        @mcp.tool(
            name="obtener_operacion",
            description="Obtener detalle de una operación específica",
            tags=["mi_cuenta", "operaciones"]
        )
        async def obtener_operacion(
            numero: int = Field(description="Número de la operación")
        ) -> Dict[str, Any]:
            """
            Obtiene el detalle de una operación específica
            
            Args:
                numero: Número de la operación
                
            Returns:
                Dict[str, Any]: Objeto con el detalle de la operación
            """
            try:
                result = await self.client.obtener_operacion(numero=numero)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo operación: {str(e)}"}
                
        @mcp.tool(
            name="cancelar_operacion",
            description="Cancelar una operación específica",
            tags=["mi_cuenta", "operaciones", "cancelar"]
        )
        async def cancelar_operacion(
            numero: int = Field(description="Número de la operación a cancelar")
        ) -> Dict[str, Any]:
            """
            Cancela una operación específica
            
            Args:
                numero: Número de la operación a cancelar
                
            Returns:
                Dict[str, Any]: Objeto con el resultado de la cancelación
            """
            try:
                result = await self.client.cancelar_operacion(numero=numero)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error cancelando operación: {str(e)}"}
                
        @mcp.tool(
            name="obtener_operaciones",
            description="Obtener operaciones del usuario según filtros",
            tags=["mi_cuenta", "operaciones", "filtros"]
        )
        async def obtener_operaciones(
            numero: Optional[int] = Field(default=None, description="Número de operación para filtrar"),
            estado: Optional[str] = Field(default=None, description="Estado de las operaciones", enum=["todas", "pendientes", "terminadas", "canceladas"]),
            fecha_desde: Optional[str] = Field(default=None, description="Fecha desde en formato ISO (YYYY-MM-DD)"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha hasta en formato ISO (YYYY-MM-DD)"),
            pais: Optional[str] = Field(default=None, description="País de las operaciones", enum=["argentina", "estados_unidos"])
        ) -> Dict[str, Any]:
            """
            Obtiene las operaciones del usuario según los filtros especificados
            
            Args:
                numero: Número de operación para filtrar
                estado: Estado de las operaciones (todas, pendientes, terminadas, canceladas)
                fecha_desde: Fecha desde en formato ISO
                fecha_hasta: Fecha hasta en formato ISO
                pais: País de las operaciones (argentina, estados_unidos)
                
            Returns:
                Dict[str, Any]: Lista de objetos con las operaciones
            """
            try:
                result = await self.client.obtener_operaciones(
                    numero=numero,
                    estado=estado,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta,
                    pais=pais
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo operaciones: {str(e)}"} 