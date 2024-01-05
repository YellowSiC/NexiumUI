import pydantic as p
from typing import Union, Literal, Optional,Dict,Any, Callable,List
from pydantic import BaseModel, Field
from typing import List, Optional, Union




class G2PlotProps(BaseModel):
    style:  Dict[str,Any] = {}
    chartType: str
    container_id: str
    data: List[dict]
    xField: str
    yField: str
    width: int
    height: int
    title: Dict[str,Any] = {}
    descriptionText: str = "Default Description Text"
    theme: str = "dark"
    legend_position: str = "top"
    xAxis:  Dict[str,Any] = {}
    yAxis:  Dict[str,Any] = {}
    binNumber: int = 10
    color: str = "white"
    min: int = 0
    max: int = 100
    tooltip:   Dict[str,Any] = {}
    realTime: bool = False
    fontSize: Optional[int] = 12
