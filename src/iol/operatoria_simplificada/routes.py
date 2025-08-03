from typing import Dict, Any, Optional, List
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import OperatoriaSimplificadaClient

class MontosEstimadosDTO(BaseModel):
    """Modelo para representar montos estimados según el swagger"""
    # Aquí se definirían los campos específicos de MontosEstimadosDTO
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class ParametrosMepSimpleDTO(BaseModel):
    """Modelo para representar parámetros de operatoria MEP simple según el swagger"""
    # Aquí se definirían los campos específicos de ParametrosMepSimpleDTO
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class ResponseModel(BaseModel):
    """Modelo para representar la respuesta de validación según el swagger"""
    # Aquí se definirían los campos específicos de ResponseModel
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class MontosEstimadosVentaMepDTO(BaseModel):
    """Modelo para representar montos estimados de venta MEP según el swagger"""
    # Aquí se definirían los campos específicos de MontosEstimadosVentaMepDTO
    # pero no se proporcionan en la especificación del swagger
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class CotizacionMepOperatoriaSimplificadaModel(BaseModel):
    """Modelo para representar una cotización MEP para operatoria simplificada según el swagger"""
    simbolo: str = Field(description="Símbolo del título")
    idPlazoOperatoriaCompra: int = Field(description="ID del plazo de operatoria de compra")
    idPlazoOperatoriaVenta: int = Field(description="ID del plazo de operatoria de venta")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class CompraOperatoriaSimplificadModel(BaseModel):
    """Modelo para representar una compra de operatoria simplificada según el swagger"""
    monto: float = Field(description="Monto de la operación")
    idTipoOperatoriaSimplificada: int = Field(description="ID del tipo de operatoria simplificada")
    idCuentaBancaria: int = Field(description="ID de la cuenta bancaria")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class OperatoriaSimplificadaRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = OperatoriaSimplificadaClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="obtener_montos_estimados",
            description="Obtener montos estimados para una operación simplificada",
            tags=["operatoria_simplificada", "montos"]
        )
        async def obtener_montos_estimados(
            monto: float = Field(description="Monto de la operación")
        ) -> Dict[str, Any]:
            """
            Obtiene los montos estimados para una operación simplificada
            
            Args:
                monto: Monto de la operación
            """
            try:
                result = await self.client.obtener_montos_estimados(monto=monto)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo montos estimados: {str(e)}"}
                
        @mcp.tool(
            name="obtener_parametros_operatoria",
            description="Obtener parámetros para un tipo de operatoria simplificada",
            tags=["operatoria_simplificada", "parametros"]
        )
        async def obtener_parametros_operatoria(
            id_tipo_operatoria: int = Field(description="ID del tipo de operatoria")
        ) -> Dict[str, Any]:
            """
            Obtiene los parámetros para un tipo de operatoria simplificada
            
            Args:
                id_tipo_operatoria: ID del tipo de operatoria
            """
            try:
                result = await self.client.obtener_parametros_operatoria(id_tipo_operatoria=id_tipo_operatoria)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo parámetros de operatoria: {str(e)}"}
                
        @mcp.tool(
            name="validar_operatoria",
            description="Validar una operación simplificada",
            tags=["operatoria_simplificada", "validar"]
        )
        async def validar_operatoria(
            monto: float = Field(description="Monto de la operación"),
            id_tipo_operatoria: int = Field(description="ID del tipo de operatoria")
        ) -> Dict[str, Any]:
            """
            Valida una operación simplificada
            
            Args:
                monto: Monto de la operación
                id_tipo_operatoria: ID del tipo de operatoria
            """
            try:
                result = await self.client.validar_operatoria(monto=monto, id_tipo_operatoria=id_tipo_operatoria)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error validando operatoria: {str(e)}"}
                
        @mcp.tool(
            name="obtener_montos_estimados_venta_mep",
            description="Obtener montos estimados para una venta MEP simple",
            tags=["operatoria_simplificada", "montos", "venta_mep"]
        )
        async def obtener_montos_estimados_venta_mep(
            monto: float = Field(description="Monto de la operación")
        ) -> Dict[str, Any]:
            """
            Obtiene los montos estimados para una venta MEP simple
            
            Args:
                monto: Monto de la operación
            """
            try:
                result = await self.client.obtener_montos_estimados_venta_mep(monto=monto)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo montos estimados de venta MEP: {str(e)}"}
                
        @mcp.tool(
            name="obtener_valor_referencia_mep",
            description="Obtener valor de referencia MEP para una cotización",
            tags=["operatoria_simplificada", "cotizaciones", "mep"]
        )
        async def obtener_valor_referencia_mep(
            request: CotizacionMepOperatoriaSimplificadaModel = Field(
                description="Datos para obtener la cotización MEP",
                example={
                    "simbolo": "AL30",
                    "idPlazoOperatoriaCompra": 1,
                    "idPlazoOperatoriaVenta": 2
                }
            )
        ) -> Dict[str, Any]:
            """
            Obtiene el valor de referencia MEP para una cotización
            
            Args:
                request: Datos para obtener la cotización MEP
            """
            try:
                result = await self.client.obtener_valor_referencia_mep(
                    simbolo=request.simbolo,
                    id_plazo_operatoria_compra=request.idPlazoOperatoriaCompra,
                    id_plazo_operatoria_venta=request.idPlazoOperatoriaVenta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo valor de referencia MEP: {str(e)}"}
                
        @mcp.tool(
            name="crear_compra_operatoria_simplificada",
            description="Crear una compra de operatoria simplificada",
            tags=["operatoria_simplificada", "compra"]
        )
        async def crear_compra_operatoria_simplificada(
            request: CompraOperatoriaSimplificadModel = Field(
                description="Datos para la compra de operatoria simplificada",
                example={
                    "monto": 10000,
                    "idTipoOperatoriaSimplificada": 1,
                    "idCuentaBancaria": 12345
                }
            )
        ) -> Dict[str, Any]:
            """
            Crea una compra de operatoria simplificada
            
            Args:
                request: Datos para la compra de operatoria simplificada
            """
            try:
                result = await self.client.crear_compra_operatoria_simplificada(
                    monto=request.monto,
                    id_tipo_operatoria_simplificada=request.idTipoOperatoriaSimplificada,
                    id_cuenta_bancaria=request.idCuentaBancaria
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando compra de operatoria simplificada: {str(e)}"} 