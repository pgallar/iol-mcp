from typing import Dict, Any, Optional, List, Union
from datetime import datetime, timedelta
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import OperarClient

class ComprarDetalleModel(BaseModel):
    """Modelo para el detalle de una operación de compra"""
    simbolo: str = Field(description="Símbolo del título")
    cantidad: float = Field(description="Cantidad a comprar")
    mercado: str = Field(description="Mercado del título", enum=["bCBA", "nYSE", "nASDAQ", "aMEX", "bCS", "rOFX"])
    tipoPrecio: Optional[str] = Field(default=None, description="Tipo de precio (L para límite)")
    precio: Optional[float] = Field(default=None, description="Precio de compra")
    plazo: Optional[str] = Field(default=None, description="Plazo de la operación", enum=["t0", "t1", "t2", "t3"])

    model_config = ConfigDict(extra="ignore", validate_assignment=True)

    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class ComprarRequestModel(BaseModel):
    """Modelo para la solicitud de compra múltiple"""
    tipoOperacion: str = Field(description="Tipo de operación (C para compra)")
    detalle: List[ComprarDetalleModel] = Field(description="Detalle de las operaciones de compra")

    model_config = ConfigDict(extra="ignore", validate_assignment=True)

    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class ComprarBindingModel(BaseModel):
    """Modelo para la operación de compra según el swagger"""
    mercado: str = Field(description="Mercado del título", enum=["bCBA", "nYSE", "nASDAQ", "aMEX", "bCS", "rOFX"])
    simbolo: str = Field(description="Símbolo del título")
    precio: float = Field(description="Precio de compra")
    plazo: str = Field(description="Plazo de la operación", enum=["t0", "t1", "t2", "t3"])
    validez: Optional[str] = Field(default=None, description="Fecha de validez de la orden en formato ISO (por defecto: 3 meses)")
    cantidad: Optional[float] = Field(default=None, description="Cantidad a comprar")
    tipoOrden: Optional[str] = Field(default=None, description="Tipo de orden", enum=["precioLimite", "precioMercado"])
    monto: Optional[float] = Field(default=None, description="Monto efectivo a invertir")
    idFuente: Optional[int] = Field(default=None, description="ID de la fuente")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class VenderBindingModel(BaseModel):
    """Modelo para la operación de venta según el swagger"""
    mercado: str = Field(description="Mercado del título", enum=["bCBA", "nYSE", "nASDAQ", "aMEX", "bCS", "rOFX"])
    simbolo: str = Field(description="Símbolo del título")
    cantidad: float = Field(description="Cantidad a vender")
    precio: float = Field(description="Precio de venta")
    validez: str = Field(description="Fecha de validez de la orden en formato ISO")
    tipoOrden: Optional[str] = Field(default=None, description="Tipo de orden", enum=["precioLimite", "precioMercado"])
    plazo: Optional[str] = Field(default=None, description="Plazo de la operación", enum=["t0", "t1", "t2", "t3"])
    idFuente: Optional[int] = Field(default=None, description="ID de la fuente")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class SuscripcionFCIBindingModel(BaseModel):
    """Modelo para la suscripción de FCI según el swagger"""
    simbolo: str = Field(description="Símbolo del FCI")
    monto: float = Field(description="Monto a suscribir")
    soloValidar: Optional[bool] = Field(default=None, description="Indica si solo se debe validar la operación sin ejecutarla")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class RescateFCIBindingModel(BaseModel):
    """Modelo para el rescate de FCI según el swagger"""
    simbolo: str = Field(description="Símbolo del FCI")
    cantidad: float = Field(description="Cantidad a rescatar")
    soloValidar: Optional[bool] = Field(default=None, description="Indica si solo se debe validar la operación sin ejecutarla")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class CPDBindingModel(BaseModel):
    """Modelo para la operación con cheques de pago diferido según el swagger"""
    idSubasta: int = Field(description="ID de la subasta")
    tasa: float = Field(description="Tasa de descuento")
    fuente: str = Field(
        description="Fuente de la operación",
        enum=[
            "compra_Venta_Por_Web", "compra_Venta_Por_Celular", "venta_De_Opciones_Por_Web_Lanzamiento",
            "asesores_IOL", "compra_Venta_Por_Web_V6", "venta_De_Opciones_Por_Asesores_IOL_Lanzamiento",
            "suscripcion_Cuenta_Facil", "compra_Venta_Por_Mobile", "asesores_IOL_Mobile",
            "quick_Trade_Dock", "asesores_Quick_Trade_Dock", "aPI", "cARGA_CHEQUE_IOLNET_Manual",
            "cARGA_CHEQUE_IOLNET_EXCEL", "cARGA_CHEQUE_IOLV6", "cARGA_CHEQUE_IOLNET_TTR",
            "operatoria_Android", "operatoria_iOS", "generada_Completadas_Manualmente_SENEBI",
            "dolar_Bolsa", "contado_Con_Liqui", "asesores_IOL_API", "aPP_MOBILE_ANDROID", "aPP_MOBILE_IOS"
        ]
    )
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class RequestTokenDDJJDTO(BaseModel):
    """Modelo para la solicitud de token según el swagger"""
    mercado: Optional[str] = Field(default=None, description="Mercado del título", enum=["bCBA", "nYSE", "nASDAQ", "aMEX", "bCS", "rOFX"])
    simbolo: Optional[str] = Field(default=None, description="Símbolo del título")
    cantidad: Optional[float] = Field(default=None, description="Cantidad")
    monto: Optional[float] = Field(default=None, description="Monto")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class VenderDBindingModel(BaseModel):
    """Modelo para la venta de especie D según el swagger"""
    mercado: str = Field(description="Mercado del título", enum=["bCBA", "nYSE", "nASDAQ", "aMEX", "bCS", "rOFX"])
    simbolo: str = Field(description="Símbolo del título")
    cantidad: float = Field(description="Cantidad a vender")
    precio: float = Field(description="Precio de venta")
    validez: str = Field(description="Fecha de validez de la orden en formato ISO")
    idCuentaBancaria: int = Field(description="ID de la cuenta bancaria")
    tipoOrden: Optional[str] = Field(default=None, description="Tipo de orden", enum=["precioLimite", "precioMercado"])
    plazo: Optional[str] = Field(default=None, description="Plazo de la operación", enum=["t0", "t1", "t2", "t3"])
    idFuente: Optional[int] = Field(default=None, description="ID de la fuente")
    
    model_config = ConfigDict(extra="ignore", validate_assignment=True)
    
    @field_validator('*', mode='before')
    @classmethod
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class OperarRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = OperarClient()

    def register_tools(self, mcp: FastMCP):
        @mcp.tool(
            name="comprar",
            description="Crear una orden de compra",
            tags=["operar", "compra"]
        )
        async def comprar(
            request: Union[ComprarBindingModel, ComprarRequestModel] = Field(
                description="Datos para la orden de compra",
                examples=[
                    {
                        "mercado": "bCBA",
                        "simbolo": "GGAL",
                        "precio": 100.5,
                        "plazo": "t2",
                        "validez": "2023-12-31T23:59:59",
                        "cantidad": 10,
                        "tipoOrden": "precioLimite"
                    },
                    {
                        "tipoOperacion": "C",
                        "detalle": [
                            {
                                "simbolo": "GRIM",
                                "cantidad": 22,
                                "mercado": "bCBA"
                            },
                            {
                                "simbolo": "CEPU",
                                "cantidad": 30,
                                "mercado": "bCBA"
                            }
                        ]
                    }
                ]
            )
        ) -> Dict[str, Any]:
            """
            Crea una orden de compra
            
            Args:
                request: Datos para la orden de compra. Puede ser un objeto ComprarBindingModel para una única compra
                         o un objeto ComprarRequestModel para múltiples compras.
            """
            try:
                # Verificar si es una solicitud de compra múltiple
                if hasattr(request, "tipoOperacion") and hasattr(request, "detalle"):
                    # Procesar compra múltiple
                    resultados = []
                    for detalle in request.detalle:
                        # Usamos los valores proporcionados en el detalle o valores por defecto
                        from datetime import datetime, timedelta
                        
                        precio = detalle.precio if hasattr(detalle, "precio") and detalle.precio is not None else 0
                        plazo = detalle.plazo if hasattr(detalle, "plazo") and detalle.plazo is not None else "t2"
                        # Fecha de validez por defecto: 3 meses a partir de la fecha actual
                        validez = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%dT23:59:59")
                        
                        resultado = await self.client.comprar(
                            mercado=detalle.mercado,
                            simbolo=detalle.simbolo,
                            cantidad=detalle.cantidad,
                            precio=precio,
                            plazo=plazo,
                            validez=validez
                        )
                        resultados.append(resultado)
                    return {
                        "success": True,
                        "result": resultados
                    }
                else:
                    # Procesar compra individual
                    # Si no se proporciona validez, usar fecha a 3 meses
                    validez = request.validez
                    if validez is None:
                        validez = (datetime.now() + timedelta(days=90)).strftime("%Y-%m-%dT23:59:59")
                    
                    result = await self.client.comprar(
                        mercado=request.mercado,
                        simbolo=request.simbolo,
                        precio=request.precio,
                        plazo=request.plazo,
                        validez=validez,
                        cantidad=request.cantidad,
                        tipo_orden=request.tipoOrden,
                        monto=request.monto,
                        id_fuente=request.idFuente
                    )
                    return {
                        "success": True,
                        "result": result
                    }
            except Exception as e:
                return {"error": f"Error creando orden de compra: {str(e)}"}

        @mcp.tool(
            name="vender",
            description="Crear una orden de venta",
            tags=["operar", "venta"]
        )
        async def vender(
            request: VenderBindingModel = Field(
                description="Datos para la orden de venta",
                example={
                    "mercado": "bCBA",
                    "simbolo": "GGAL",
                    "cantidad": 10,
                    "precio": 100.5,
                    "validez": "2023-12-31T23:59:59",
                    "tipoOrden": "precioLimite",
                    "plazo": "t2"
                }
            )
        ) -> Dict[str, Any]:
            """
            Crea una orden de venta
            
            Args:
                request: Datos para la orden de venta
            """
            try:
                result = await self.client.vender(
                    mercado=request.mercado,
                    simbolo=request.simbolo,
                    cantidad=request.cantidad,
                    precio=request.precio,
                    validez=request.validez,
                    tipo_orden=request.tipoOrden,
                    plazo=request.plazo,
                    id_fuente=request.idFuente
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando orden de venta: {str(e)}"}
                
        @mcp.tool(
            name="suscribir_fci",
            description="Suscribir un FCI",
            tags=["operar", "fci"]
        )
        async def suscribir_fci(
            request: SuscripcionFCIBindingModel = Field(
                description="Datos para la suscripción del FCI",
                example={
                    "simbolo": "PIONERO_RENTA",
                    "monto": 1000,
                    "soloValidar": False
                }
            )
        ) -> Dict[str, Any]:
            """
            Suscribe un FCI
            
            Args:
                request: Datos para la suscripción del FCI
            """
            try:
                result = await self.client.suscribir_fci(
                    simbolo=request.simbolo,
                    monto=request.monto,
                    solo_validar=request.soloValidar
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error suscribiendo FCI: {str(e)}"}
                
        @mcp.tool(
            name="rescatar_fci",
            description="Rescatar un FCI",
            tags=["operar", "fci"]
        )
        async def rescatar_fci(
            request: RescateFCIBindingModel = Field(
                description="Datos para el rescate del FCI",
                example={
                    "simbolo": "PIONERO_RENTA",
                    "cantidad": 10,
                    "soloValidar": False
                }
            )
        ) -> Dict[str, Any]:
            """
            Rescata un FCI
            
            Args:
                request: Datos para el rescate del FCI
            """
            try:
                result = await self.client.rescatar_fci(
                    simbolo=request.simbolo,
                    cantidad=request.cantidad,
                    solo_validar=request.soloValidar
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error rescatando FCI: {str(e)}"}
                
        @mcp.tool(
            name="cpd_puede_operar",
            description="Verificar si el usuario puede operar con cheques de pago diferido",
            tags=["operar", "cpd"]
        )
        async def cpd_puede_operar() -> Dict[str, Any]:
            """
            Verifica si el usuario puede operar con cheques de pago diferido
            
            Returns:
                Dict[str, Any]: Información sobre si puede operar con CPD
            """
            try:
                result = await self.client.cpd_puede_operar()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error verificando si puede operar con CPD: {str(e)}"}
                
        @mcp.tool(
            name="obtener_cpd",
            description="Obtener cheques de pago diferido según estado y segmento",
            tags=["operar", "cpd"]
        )
        async def obtener_cpd(
            estado: str = Field(description="Estado de los cheques"),
            segmento: str = Field(description="Segmento de los cheques")
        ) -> Dict[str, Any]:
            """
            Obtiene los cheques de pago diferido según estado y segmento
            
            Args:
                estado: Estado de los cheques
                segmento: Segmento de los cheques
                
            Returns:
                Dict[str, Any]: Información de los cheques
            """
            try:
                result = await self.client.obtener_cpd(estado=estado, segmento=segmento)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo CPD: {str(e)}"}
                
        @mcp.tool(
            name="calcular_comisiones_cpd",
            description="Calcular comisiones para un cheque de pago diferido",
            tags=["operar", "cpd", "comisiones"]
        )
        async def calcular_comisiones_cpd(
            importe: float = Field(description="Importe del cheque"),
            plazo: int = Field(description="Plazo en días"),
            tasa: float = Field(description="Tasa de descuento")
        ) -> Dict[str, Any]:
            """
            Calcula las comisiones para un cheque de pago diferido
            
            Args:
                importe: Importe del cheque
                plazo: Plazo en días
                tasa: Tasa de descuento
                
            Returns:
                Dict[str, Any]: Información de las comisiones
            """
            try:
                result = await self.client.calcular_comisiones_cpd(
                    importe=importe,
                    plazo=plazo,
                    tasa=tasa
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error calculando comisiones CPD: {str(e)}"}
                
        @mcp.tool(
            name="operar_cpd",
            description="Realizar una operación con un cheque de pago diferido",
            tags=["operar", "cpd"]
        )
        async def operar_cpd(
            request: CPDBindingModel = Field(
                description="Datos para la operación con CPD",
                example={
                    "idSubasta": 12345,
                    "tasa": 35.5,
                    "fuente": "compra_Venta_Por_Web"
                }
            )
        ) -> Dict[str, Any]:
            """
            Realiza una operación con un cheque de pago diferido
            
            Args:
                request: Datos para la operación con CPD
                
            Returns:
                Dict[str, Any]: Resultado de la operación
            """
            try:
                result = await self.client.operar_cpd(
                    id_subasta=request.idSubasta,
                    tasa=request.tasa,
                    fuente=request.fuente
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error operando CPD: {str(e)}"}
                
        @mcp.tool(
            name="generar_token",
            description="Generar un token para operaciones",
            tags=["operar", "token"]
        )
        async def generar_token(
            request: RequestTokenDDJJDTO = Field(
                description="Datos para la generación del token",
                example={
                    "mercado": "bCBA",
                    "simbolo": "GGAL",
                    "cantidad": 10,
                    "monto": 1000
                }
            )
        ) -> Dict[str, Any]:
            """
            Genera un token para operaciones
            
            Args:
                request: Datos para la generación del token
                
            Returns:
                Dict[str, Any]: Token generado
            """
            try:
                result = await self.client.generar_token(
                    mercado=request.mercado,
                    simbolo=request.simbolo,
                    cantidad=request.cantidad,
                    monto=request.monto
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error generando token: {str(e)}"}
                
        @mcp.tool(
            name="vender_especie_d",
            description="Crear una orden de venta de especie D",
            tags=["operar", "venta", "especie_d"]
        )
        async def vender_especie_d(
            request: VenderDBindingModel = Field(
                description="Datos para la orden de venta de especie D",
                example={
                    "mercado": "bCBA",
                    "simbolo": "GGAL",
                    "cantidad": 10,
                    "precio": 100.5,
                    "validez": "2023-12-31T23:59:59",
                    "idCuentaBancaria": 12345,
                    "tipoOrden": "precioLimite",
                    "plazo": "t2"
                }
            )
        ) -> Dict[str, Any]:
            """
            Crea una orden de venta de especie D
            
            Args:
                request: Datos para la orden de venta de especie D
                
            Returns:
                Dict[str, Any]: Resultado de la operación
            """
            try:
                result = await self.client.vender_especie_d(
                    mercado=request.mercado,
                    simbolo=request.simbolo,
                    cantidad=request.cantidad,
                    precio=request.precio,
                    validez=request.validez,
                    id_cuenta_bancaria=request.idCuentaBancaria,
                    tipo_orden=request.tipoOrden,
                    plazo=request.plazo,
                    id_fuente=request.idFuente
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando orden de venta de especie D: {str(e)}"}
                
        @mcp.tool(
            name="comprar_especie_d",
            description="Crear una orden de compra de especie D",
            tags=["operar", "compra", "especie_d"]
        )
        async def comprar_especie_d(
            request: ComprarBindingModel = Field(
                description="Datos para la orden de compra de especie D",
                example={
                    "mercado": "bCBA",
                    "simbolo": "GGAL",
                    "precio": 100.5,
                    "plazo": "t2",
                    "validez": "2023-12-31T23:59:59",
                    "cantidad": 10,
                    "tipoOrden": "precioLimite"
                }
            )
        ) -> Dict[str, Any]:
            """
            Crea una orden de compra de especie D
            
            Args:
                request: Datos para la orden de compra de especie D
                
            Returns:
                Dict[str, Any]: Resultado de la operación
            """
            try:
                result = await self.client.comprar_especie_d(
                    mercado=request.mercado,
                    simbolo=request.simbolo,
                    precio=request.precio,
                    plazo=request.plazo,
                    validez=request.validez,
                    cantidad=request.cantidad,
                    tipo_orden=request.tipoOrden,
                    monto=request.monto,
                    id_fuente=request.idFuente
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando orden de compra de especie D: {str(e)}"} 