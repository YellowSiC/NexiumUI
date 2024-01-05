from typing import Dict, Any, List, Optional
from .props import G2PlotProps

def g2plot_props(
    chartType: str,
    container_id: str,
    data: List[dict],
    xField: str,
    yField: str,
    width: int,
    height: int,
    style: Dict[str, Any] = {},
    title: Dict[str, Any] = {},
    descriptionText: str = "Default Description Text",
    theme: str = "dark",
    legend_position: str = "top",
    xAxis: Dict[str, Any] = {},
    yAxis: Dict[str, Any] = {},
    binNumber: int = 10,
    color: str = "white",
    min: int = 0,
    max: int = 100,
    tooltip: Dict[str, Any] = {},
    fontSize: Optional[int] = 12
) -> G2PlotProps:
    return G2PlotProps(
        style=style,
        chartType=chartType,
        container_id=container_id,
        data=data,
        xField=xField,
        yField=yField,
        width=width,
        height=height,
        title=title,
        descriptionText=descriptionText,
        theme=theme,
        legend_position=legend_position,
        xAxis=xAxis,
        yAxis=yAxis,
        binNumber=binNumber,
        color=color,
        min=min,
        max=max,
        tooltip=tooltip,
        fontSize=fontSize
    )
