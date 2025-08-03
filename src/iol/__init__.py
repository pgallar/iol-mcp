"""
IOL MCP - Cliente para la API de InvertirOnline
"""

__version__ = "1.0.0"

from .portafolio.routes import PortafolioRoutes
from .titulos.routes import TitulosRoutes
from .asesores.routes import AsesoresRoutes
from .asesores_operar.routes import AsesoresOperarRoutes
from .asesores_test_inversor.routes import AsesoresTestInversorRoutes
from .mi_cuenta.routes import MiCuentaRoutes
from .notificacion.routes import NotificacionRoutes
from .operar.routes import OperarRoutes
from .operatoria_simplificada.routes import OperatoriaSimplificadaRoutes
from .perfil.routes import PerfilRoutes

__all__ = [
    'PortafolioRoutes',
    'TitulosRoutes',
    'AsesoresRoutes',
    'AsesoresOperarRoutes',
    'AsesoresTestInversorRoutes',
    'MiCuentaRoutes',
    'NotificacionRoutes',
    'OperarRoutes',
    'OperatoriaSimplificadaRoutes',
    'PerfilRoutes'
] 