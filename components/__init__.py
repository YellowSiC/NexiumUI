import pydantic as p
from typing import Union, Literal, Optional,Dict,Any, Callable,List
from pydantic import BaseModel, Field
from typing import List, Optional, Union
from ..ui_props.props import G2PlotProps




class Button(p.BaseModel, extra='forbid'):
    component:Literal['Button'] = 'Button'
    content:str
    props: Dict[str,Any] = {}
     




class Sider(p.BaseModel, extra='forbid'):
    component:Literal['Sider'] = 'Sider'
    content:Any
    props: Dict[str,Any] = {}
     


class Content(p.BaseModel, extra='forbid'):
    component:Literal['Content'] = 'Content'
    content:Any
    props: Dict[str,Any] = {}
     

class Footer(p.BaseModel, extra='forbid'):
    component:Literal['Footer'] = 'Footer'
    content:Any
    props: Dict[str,Any] = {}
     


class Header(p.BaseModel, extra='forbid'):
    component:Literal['Header'] = 'Header'
    content:str
    props: Dict[str,Any] = {}
     



class Title(p.BaseModel, extra='forbid'):
    component:Literal['Title'] = 'Title'
    content:str
    props: Dict[str,Any] = {}
     

class G2Plot(p.BaseModel, extra='forbid'):
    component:Literal['NexiumUIChart'] = 'NexiumUIChart'
    props: G2PlotProps 


class G2PlotRealTimeChart(p.BaseModel, extra='forbid'):
    component:Literal['NexiumUIRealTimeChart'] = 'NexiumUIRealTimeChart'
    props: G2PlotProps 





class FloatButton(p.BaseModel, extra='forbid'):
    component:Literal['FloatButton'] = 'FloatButton'
    content:str
    props: Dict[str,Any] = {}
     


class Typography(p.BaseModel, extra='forbid'):
    component:Literal['Typography'] = 'Typography'
    content:str
    props: Dict[str,Any] = {}
     


class Icon(p.BaseModel, extra='forbid'):
    component:Literal['Icon'] = 'Icon'
    content:str
    props: Dict[str,Any] = {}
     


class Layout(p.BaseModel, extra='forbid'):
    component:Literal['Layout'] = 'Layout'
    content:Any
    props: Dict[str,Any] = {}
     



class ReactNode(p.BaseModel, extra='forbid'):
    component:str
    content:Any
    props: Dict[str,Any] = {}


class AntdIcon(p.BaseModel, extra='forbid'):
    component:str
    content:Any
    props: Dict[str,Any] = {}




class Divider(p.BaseModel, extra='forbid'):
    component:Literal['Divider'] = 'Divider'
    content:Any
    props: Dict[str,Any] = {}
     


class Flex(p.BaseModel, extra='forbid'):
    component:Literal['Flex'] = 'Flex'
    content:Any
    props: Dict[str,Any] = {}
     


class Grid(p.BaseModel, extra='forbid'):
    component:Literal['Grid'] = 'Grid'
    content:Any
    props: Dict[str,Any] = {}
     


class Space(p.BaseModel, extra='forbid'):
    component:Literal['Space'] = 'Space'
    content:Any
    props: Dict[str,Any] = {}
     



class Anchor(p.BaseModel, extra='forbid'):
    component:Literal['Anchor'] = 'Anchor'
    content:Any
    props: Dict[str,Any] = {}
     


class Breadcrumb(p.BaseModel, extra='forbid'):
    component:Literal['Breadcrumb'] = 'Breadcrumb'
    content:Any
    props: Dict[str,Any] = {}
     


class Dropdown(p.BaseModel, extra='forbid'):
    component:Literal['Dropdown'] = 'Dropdown'
    content:Any
    props: Dict[str,Any] = {}
     


class Menu(p.BaseModel, extra='forbid'):
    component:Literal['Menu'] = 'Menu'
    content:Any
    props: Dict[str,Any] = {}
     


class Pagination(p.BaseModel, extra='forbid'):
    component:Literal['Pagination'] = 'Pagination'
    content:Any
    props: Dict[str,Any] = {}
     


class Steps(p.BaseModel, extra='forbid'):
    component:Literal['Steps'] = 'Steps'
    content:Any
    props: Dict[str,Any] = {}
     


class AutoComplete(p.BaseModel, extra='forbid'):
    component:Literal['AutoComplete'] = 'AutoComplete'
    content:Any
    props: Dict[str,Any] = {}
     


class Cascader(p.BaseModel, extra='forbid'):
    component:Literal['Cascader'] = 'Cascader'
    content:Any
    props: Dict[str,Any] = {}
     


class Checkbox(p.BaseModel, extra='forbid'):
    component:Literal['Checkbox'] = 'Checkbox'
    content:str
    props: Dict[str,Any] = {}
     


class ColorPicker(p.BaseModel, extra='forbid'):
    component:Literal['ColorPicker'] = 'ColorPicker'
    props: Dict[str,Any] = {}
     


class DatePicker(p.BaseModel, extra='forbid'):
    component:Literal['DatePicker'] = 'DatePicker'
    content:str
    props: Dict[str,Any] = {}
     


class Form(p.BaseModel, extra='forbid'):
    component:Literal['Form'] = 'Form'
    content:Any
    props: Dict[str,Any] = {}
     


class Input(p.BaseModel, extra='forbid'):
    component:Literal['Input'] = 'Input'
    props: Dict[str,Any] = {}
     


class InputNumber(p.BaseModel, extra='forbid'):
    component:Literal['InputNumber'] = 'InputNumber'
    props: Dict[str,Any] = {}
     


class Mentions(p.BaseModel, extra='forbid'):
    component:Literal['Mentions'] = 'Mentions'
    content:str
    props: Dict[str,Any] = {}
     


class Radio(p.BaseModel, extra='forbid'):
    component:Literal['Radio'] = 'Radio'
    props: Dict[str,Any] = {}
     


class Rate(p.BaseModel, extra='forbid'):
    component:Literal['Rate'] = 'Rate'
    content:str
    props: Dict[str,Any] = {}
     


class Select(p.BaseModel, extra='forbid'):
    component:Literal['Select'] = 'Select'
    content:Any
    props: Dict[str,Any] = {}
     


class Slider(p.BaseModel, extra='forbid'):
    component:Literal['Slider'] = 'Slider'
    props: Dict[str,Any] = {}
     


class Switch(p.BaseModel, extra='forbid'):
    component:Literal['Switch'] = 'Switch'
    content:str
    props: Dict[str,Any] = {}
     


class TimePicker(p.BaseModel, extra='forbid'):
    component:Literal['TimePicker'] = 'TimePicker'
    content:str
    props: Dict[str,Any] = {}
     


class Transfer(p.BaseModel, extra='forbid'):
    component:Literal['Transfer'] = 'Transfer'
    content:Any
    props: Dict[str,Any] = {}
     


class TreeSelect(p.BaseModel, extra='forbid'):
    component:Literal['TreeSelect'] = 'TreeSelect'
    content:str
    props: Dict[str,Any] = {}
     


class Upload(p.BaseModel, extra='forbid'):
    component:Literal['Upload'] = 'Upload'
    content:Any
    props: Dict[str,Any] = {}
     


class Avatar(p.BaseModel, extra='forbid'):
    component:Literal['Avatar'] = 'Avatar'
    content:Any
    props: Dict[str,Any] = {}
     


class Badge(p.BaseModel, extra='forbid'):
    component:Literal['Badge'] = 'Badge'
    content:Any
    props: Dict[str,Any] = {}
     


class Calendar(p.BaseModel, extra='forbid'):
    component:Literal['Calendar'] = 'Calendar'
    content:str
    props: Dict[str,Any] = {}
     


class Card(p.BaseModel, extra='forbid'):
    component:Literal['Card'] = 'Card'
    content:Any
    props: Dict[str,Any] = {}
     


class Carousel(p.BaseModel, extra='forbid'):
    component:Literal['Carousel'] = 'Carousel'
    content:str
    props: Dict[str,Any] = {}
     


class Collapse(p.BaseModel, extra='forbid'):
    component:Literal['Collapse'] = 'Collapse'
    content:Any
    props: Dict[str,Any] = {}
     


class Descriptions(p.BaseModel, extra='forbid'):
    component:Literal['Descriptions'] = 'Descriptions'
    content:Any
    props: Dict[str,Any] = {}
     


class Empty(p.BaseModel, extra='forbid'):
    component:Literal['Empty'] = 'Empty'
    content:Any
    props: Dict[str,Any] = {}
     


class Image(p.BaseModel, extra='forbid'):
    component:Literal['Empty'] = 'Image'
    content:str
    props: Dict[str,Any] = {}
     


class UIList(p.BaseModel, extra='forbid'):
    component:Literal['List'] = 'List'
    content:Any
    props: Dict[str,Any] = {}
     


class Popover(p.BaseModel, extra='forbid'):
    component:Literal['Popover'] = 'Popover'
    content:str
    props: Dict[str,Any] = {}
     


class QRCode(p.BaseModel, extra='forbid'):
    component:Literal['QRCode'] = 'QRCode'
    content:str
    props: Dict[str,Any] = {}
     


class Segmented(p.BaseModel, extra='forbid'):
    component:Literal['Segmented'] = 'Segmented'
    content:str
    props: Dict[str,Any] = {}
     


class Statistic(p.BaseModel, extra='forbid'):
    component:Literal['Statistic'] = 'Statistic'
    content:str
    props: Dict[str,Any] = {}
     


class Table(p.BaseModel, extra='forbid'):
    component:Literal['Table'] = 'Table'
    content:Any
    props: Dict[str,Any] = {}
     


class Tabs(p.BaseModel, extra='forbid'):
    component:Literal['Tabs'] = 'Tabs'
    content:Any
    props: Dict[str,Any] = {}
     


class Tag(p.BaseModel, extra='forbid'):
    component:Literal['Tag'] = 'Tag'
    content:str
    props: Dict[str,Any] = {}
     


class Timeline(p.BaseModel, extra='forbid'):
    component:Literal['Timeline'] = 'Timeline'
    content:str
    props: Dict[str,Any] = {}
     


class Tooltip(p.BaseModel, extra='forbid'):
    component:Literal['Tooltip'] = 'Tooltip'
    content:str
    props: Dict[str,Any] = {}
     


class Tour(p.BaseModel, extra='forbid'):
    component:Literal['Tour'] = 'Tour'
    content:str
    props: Dict[str,Any] = {}
     


class Tree(p.BaseModel, extra='forbid'):
    component:Literal['Tree'] = 'Tree'
    content:str
    props: Dict[str,Any] = {}
     


class Alert(p.BaseModel, extra='forbid'):
    component:Literal['Alert'] = 'Alert'
    content:str
    props: Dict[str,Any] = {}
     


class Drawer(p.BaseModel, extra='forbid'):
    component:Literal['Drawer'] = 'Drawer'
    content:Any
    props: Dict[str,Any] = {}
     


class Message(p.BaseModel, extra='forbid'):
    component:Literal['Message'] = 'Message'
    content:str
    props: Dict[str,Any] = {}
     


class Modal(p.BaseModel, extra='forbid'):
    component:Literal['Modal'] = 'Modal'
    content:str
    props: Dict[str,Any] = {}
     


class Notification(p.BaseModel, extra='forbid'):
    component:Literal['Notification'] = 'Notification'
    content:str
    props: Dict[str,Any] = {}
     


class Popconfirm(p.BaseModel, extra='forbid'):
    component:Literal['Popconfirm'] = 'Popconfirm'
    content:str
    props: Dict[str,Any] = {}
     


class Progress(p.BaseModel, extra='forbid'):
    component:Literal['Progress'] = 'Progress'
    content:str
    props: Dict[str,Any] = {}
     


class Result(p.BaseModel, extra='forbid'):
    component:Literal['Result'] = 'Result'
    content:str
    props: Dict[str,Any] = {}
     


class Skeleton(p.BaseModel, extra='forbid'):
    component:Literal['Skeleton'] = 'Skeleton'
    content:str
    props: Dict[str,Any] = {}
     


class Spin(p.BaseModel, extra='forbid'):
    component:Literal['Spin'] = 'Spin'
    content:str
    props: Dict[str,Any] = {}
     


class Watermark(p.BaseModel, extra='forbid'):
    component:Literal['Watermark'] = 'Watermark'
    content:str
    props: Dict[str,Any] = {}
     


class Affix(p.BaseModel, extra='forbid'):
    component:Literal['Affix'] = 'Affix'
    content:str
    props: Dict[str,Any] = {}
     
Layout

class App(p.BaseModel, extra='forbid'):
    component:Literal['App'] = 'App'
    content:Any
    props: Dict[str,Any] = {}
    props: Dict[str,Any] = {}
     


