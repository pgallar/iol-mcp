from typing import Dict, Any, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field, field_validator, ConfigDict
from ..base_routes import BaseRoutes
from .client import AsesoresOperarClient

class AsesoresOperarRoutes(BaseRoutes):
    def __init__(self):
        super().__init__()
        self.client = AsesoresOperarClient()

    def register_tools(self, mcp: FastMCP):
        pass 