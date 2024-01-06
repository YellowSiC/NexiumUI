from inspect import signature 
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, Callable, Dict, Any, List, Set, Tuple
from .client.react import generate_react_component
from .client.utils import create_html_file

class Page(BaseModel):
    name: str
    url: str
    auth_needed: Optional[str] = None
    language: str
    builder: Optional[Callable] = None
    registered_pages: Set[Tuple[str, str]] = set()

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

        page_info = (self.name, self.url)

        if page_info not in self.registered_pages:
            react_component_html = generate_react_component(self.name, call_builder(), path=self.url, language=self.language, registered_pages=self.registered_pages)
            create_html_file('ddd.html', html_content=react_component_html)
            self.registered_pages.add(page_info)
            return HTMLResponse(content=react_component_html)
        else:
            self.registered_pages.remove(page_info)
            self.registered_pages.add(page_info)
            print(self.registered_pages)
            react_component_html = generate_react_component(self.name, call_builder(), path=self.url, language=self.language, registered_pages=self.registered_pages)
            create_html_file('ddd.html', html_content=react_component_html)
            return HTMLResponse(content=react_component_html)

        #return {
            #'content':call_builder()
        #}
