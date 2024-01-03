from inspect import signature 
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, Callable
from .client.react import generate_react_component









class Page(BaseModel):  
    name: str
    url: str
    auth_needed: Optional[str] = None
    builder: Optional[Callable] = None

    class Config:
        arbitrary_types_allowed = True
        

    def as_list(self, param='', all_params=None):
        def call_builder():
            num_func_params = len(signature(self.builder).parameters)
            if num_func_params > 1:
                return self.builder(param, all_params)
            elif num_func_params > 0:
                return self.builder(param)
            else:
                return self.builder()
            
        # Generiere die React-Komponente
        react_component_html = generate_react_component(self.name, call_builder())
        # Verwende HTMLResponse, um den HTML-Code als Antwort zu senden (
        return HTMLResponse(content=react_component_html)
        #return {
            #'content':call_builder()
        #}