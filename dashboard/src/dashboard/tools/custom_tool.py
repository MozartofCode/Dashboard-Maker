from typing import Type
from crewai_tools import BaseTool
from pydantic import BaseModel, Field

class PieGraphInput(BaseModel):
    """Input schema for PieGraph."""
    data: dict = Field(..., description="Data to be plotted in the pie graph.")

class PieGraph(BaseTool):
    name: str = "Pie Graph"
    description: str = "A tool to plot pie graphs."
    args_schema: Type[BaseModel] = PieGraphInput

    def _run(self, data: dict) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
