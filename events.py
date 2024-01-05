import uuid
import inspect
import os
import time
from pathlib import Path
from inspect import signature
import pydantic as p
from  typing import Optional, Any, Union, List, Literal, Callable, Dict


class BindingEvent(p.BaseModel):
    event_type: str = 'BindingEvent'
    property: str
    targest_id:str








class PageNavigationEvent(p.BaseModel):
    event_type: str = 'PageNavigationEvent'
    path: str

class CloseModalEvent(p.BaseModel):
    event_type: str = 'CloseModalEvent'
    close:bool 


class OpenModalEvent(p.BaseModel):
    event_type: str = 'OpenModalEvent'
    close:bool 

class CloseDrawerEvent(p.BaseModel):
    event_type: str = 'CloseDrawerEvent'
    close:bool 


class OpenDrawerEvent(p.BaseModel):
    event_type: str = 'OpenDrawerEvent'
    open:bool


class APIRequestEvent(p.BaseModel):
    event_type: str = 'APIRequestEvent'
    method: str
    url: str
    params: Optional[Dict[str, Any]] = None
    data: Optional[Any] = None
    headers: Optional[Dict[str, str]] = None
    auth: Optional[Dict[str, str]] = None
    timeout: Optional[float] = None
    allow_redirects: Optional[bool] = None
    proxies: Optional[Dict[str, str]] = None
    verify: Optional[bool] = None
    cookies: Optional[Dict[str, str]] = None
    hooks: Optional[Dict[str, Any]] = None
    stream: Optional[bool] = None




class APIUploadEvent(p.BaseModel):
    event_type: str = 'APIUploadEvent'
    multiple: bool = False
    url: str



""" method,
url,
params,
data,
headers,
auth,
timeout,
allow_redirects,
proxies,
verify,
cookies,
hooks,
stream, """
