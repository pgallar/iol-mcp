from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import MiCuentaClient

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
            name="obtener_saldos",
            description="Obtener saldos del usuario",
            tags=["mi_cuenta", "saldos"]
        )
        async def obtener_saldos() -> Dict[str, Any]:
            """
            Obtiene los saldos del usuario
            """
            try:
                result = await self.client.obtener_saldos()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo saldos: {str(e)}"}

        @mcp.tool(
            name="obtener_movimientos",
            description="Obtener movimientos de cuenta del usuario",
            tags=["mi_cuenta", "movimientos"]
        )
        async def obtener_movimientos(
            pais: Optional[str] = Field(default=None, description="País de los movimientos (argentina, estados_unidos, etc)"),
            tipo_movimiento: Optional[str] = Field(default=None, description="Tipo de movimiento (deposito, extraccion, etc)"),
            fecha_desde: Optional[str] = Field(default=None, description="Fecha de inicio en formato YYYY-MM-DD"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha de fin en formato YYYY-MM-DD")
        ) -> Dict[str, Any]:
            """
            Obtiene los movimientos de cuenta del usuario
            
            Args:
                pais: País de los movimientos (argentina, estados_unidos, etc)
                tipo_movimiento: Tipo de movimiento (deposito, extraccion, etc)
                fecha_desde: Fecha de inicio en formato YYYY-MM-DD
                fecha_hasta: Fecha de fin en formato YYYY-MM-DD
            """
            try:
                result = await self.client.obtener_movimientos(
                    pais=pais,
                    tipo_movimiento=tipo_movimiento,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo movimientos: {str(e)}"}

        @mcp.tool(
            name="obtener_movimientos_fondos",
            description="Obtener movimientos de fondos del usuario",
            tags=["mi_cuenta", "movimientos", "fondos"]
        )
        async def obtener_movimientos_fondos(
            pais: Optional[str] = Field(default=None, description="País de los movimientos (argentina, estados_unidos, etc)"),
            tipo_movimiento: Optional[str] = Field(default=None, description="Tipo de movimiento (deposito, extraccion, etc)"),
            fecha_desde: Optional[str] = Field(default=None, description="Fecha de inicio en formato YYYY-MM-DD"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha de fin en formato YYYY-MM-DD")
        ) -> Dict[str, Any]:
            """
            Obtiene los movimientos de fondos del usuario
            
            Args:
                pais: País de los movimientos (argentina, estados_unidos, etc)
                tipo_movimiento: Tipo de movimiento (deposito, extraccion, etc)
                fecha_desde: Fecha de inicio en formato YYYY-MM-DD
                fecha_hasta: Fecha de fin en formato YYYY-MM-DD
            """
            try:
                result = await self.client.obtener_movimientos_fondos(
                    pais=pais,
                    tipo_movimiento=tipo_movimiento,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo movimientos de fondos: {str(e)}"}

        @mcp.tool(
            name="obtener_movimientos_fci",
            description="Obtener movimientos de FCI del usuario",
            tags=["mi_cuenta", "movimientos", "fci"]
        )
        async def obtener_movimientos_fci(
            pais: Optional[str] = Field(default=None, description="País de los movimientos (argentina, estados_unidos, etc)"),
            tipo_movimiento: Optional[str] = Field(default=None, description="Tipo de movimiento (suscripcion, rescate, etc)"),
            fecha_desde: Optional[str] = Field(default=None, description="Fecha de inicio en formato YYYY-MM-DD"),
            fecha_hasta: Optional[str] = Field(default=None, description="Fecha de fin en formato YYYY-MM-DD")
        ) -> Dict[str, Any]:
            """
            Obtiene los movimientos de FCI del usuario
            
            Args:
                pais: País de los movimientos (argentina, estados_unidos, etc)
                tipo_movimiento: Tipo de movimiento (suscripcion, rescate, etc)
                fecha_desde: Fecha de inicio en formato YYYY-MM-DD
                fecha_hasta: Fecha de fin en formato YYYY-MM-DD
            """
            try:
                result = await self.client.obtener_movimientos_fci(
                    pais=pais,
                    tipo_movimiento=tipo_movimiento,
                    fecha_desde=fecha_desde,
                    fecha_hasta=fecha_hasta
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo movimientos de FCI: {str(e)}"}
                
        @mcp.tool(
            name="obtener_cuentas_bancarias",
            description="Obtener cuentas bancarias del usuario",
            tags=["mi_cuenta", "cuentas"]
        )
        async def obtener_cuentas_bancarias() -> Dict[str, Any]:
            """
            Obtiene las cuentas bancarias del usuario
            """
            try:
                result = await self.client.obtener_cuentas_bancarias()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo cuentas bancarias: {str(e)}"}
                
        @mcp.tool(
            name="obtener_cuentas_comitentes",
            description="Obtener cuentas comitentes del usuario",
            tags=["mi_cuenta", "cuentas"]
        )
        async def obtener_cuentas_comitentes() -> Dict[str, Any]:
            """
            Obtiene las cuentas comitentes del usuario
            """
            try:
                result = await self.client.obtener_cuentas_comitentes()
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo cuentas comitentes: {str(e)}"}
                
        @mcp.tool(
            name="obtener_resumen_cuenta",
            description="Obtener resumen de cuenta del usuario",
            tags=["mi_cuenta", "resumen"]
        )
        async def obtener_resumen_cuenta(
            pais: Optional[str] = Field(default=None, description="País del resumen (argentina, estados_unidos, etc)")
        ) -> Dict[str, Any]:
            """
            Obtiene el resumen de cuenta del usuario
            
            Args:
                pais: País del resumen (argentina, estados_unidos, etc)
            """
            try:
                result = await self.client.obtener_resumen_cuenta(pais=pais)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo resumen de cuenta: {str(e)}"}
                
        @mcp.tool(
            name="obtener_detalle_movimiento",
            description="Obtener detalle de un movimiento específico",
            tags=["mi_cuenta", "movimientos", "detalle"]
        )
        async def obtener_detalle_movimiento(
            id_movimiento: int = Field(description="ID del movimiento")
        ) -> Dict[str, Any]:
            """
            Obtiene el detalle de un movimiento específico
            
            Args:
                id_movimiento: ID del movimiento
            """
            try:
                result = await self.client.obtener_detalle_movimiento(id_movimiento=id_movimiento)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo detalle del movimiento: {str(e)}"}
                
        @mcp.tool(
            name="solicitar_extraccion",
            description="Solicitar una extracción de fondos",
            tags=["mi_cuenta", "extraccion"]
        )
        async def solicitar_extraccion(
            monto: float = Field(description="Monto a extraer"),
            id_cuenta_bancaria: int = Field(description="ID de la cuenta bancaria destino"),
            moneda: str = Field(description="Moneda de la extracción (ARS, USD, etc)")
        ) -> Dict[str, Any]:
            """
            Solicita una extracción de fondos
            
            Args:
                monto: Monto a extraer
                id_cuenta_bancaria: ID de la cuenta bancaria destino
                moneda: Moneda de la extracción (ARS, USD, etc)
            """
            try:
                result = await self.client.solicitar_extraccion(
                    monto=monto,
                    id_cuenta_bancaria=id_cuenta_bancaria,
                    moneda=moneda
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error solicitando extracción: {str(e)}"} 