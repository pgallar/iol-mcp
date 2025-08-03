from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import OperatoriaSimplificadaClient

class OperatoriaSimplificadaRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = OperatoriaSimplificadaClient()

    def register_tools(self, mcp: FastMCP):
        pass 