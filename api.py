from fastapi import APIRouter, Request,Response, FastAPI
from fastapi.responses import HTMLResponse
import json
import jwt
from pydantic import BaseModel
from .client.nexium import  html
from .page import Page



class NexiumUI(APIRouter):
    SECRET = "sic ui super &*#*$ secret"
    def __init__(self):
        super().__init__()
        self.jsonify = lambda x: Response(content=json.dumps(x), media_type='application/json')
        self.get_request_json = self.get_request_json_method
        self.get_header = lambda name, request: request.headers[name] if name in request.headers else None
        self.get_url_args = lambda request: request.query_params._dict
        self.pages = {}
        self.menu = {}
        self.on_login = {}
        self.app = None  # Store the FastAPI instance

    async def get_request_json_method(self, request: Request):
        return await request.json()
    
    def page(self, url, name, auth_needed=None):
        def decorator(func):
            new_page = Page(name=name, url=url, builder=func, auth_needed=auth_needed)
            self.pages[url] = new_page
            return new_page
        return decorator

    def login(self, method='password'):
        """Decorator: register a login handler
        """
        def decorator(func):
            self.on_login[method] = func
        return decorator
    


    def current_user(self, request=None):
        """Get the current logged in user. 
        
        Returns:
            {'display_name', 'auth', 'user_info'}: information about current logged in user
        """
        auth_header = self.get_header('Authorization', request)
        if auth_header is not None:
            return jwt.decode(bytes(auth_header, 'utf-8'), NexiumUI.SECRET, algorithms=['HS256'])
        else:
            return {'display_name': None, 'auth': [], 'user_info': None}
    
    async def serve_page(self, url='', request=None):
        def has_permission(page):
            return page.auth_needed is None or page.auth_needed in self.current_user(request)['auth']

        url_parts = url.split('/')
        full_url = '/' + url.lstrip('/')  # Füge einen führenden Slash hinzu
        base_url = '/' + url_parts[0]
        args = self.get_url_args(request)

        if full_url in self.pages:
            if has_permission(self.pages[full_url]):
                return self.pages[full_url].as_list(all_params=args)
            else: 
                return "No Permission", "Please login first or contact your administrator"
        elif base_url in self.pages and len(url_parts) > 1:
            if has_permission(self.pages[base_url]):
                return self.pages[base_url].as_list(url_parts[1], all_params=args.model_dump_json())
            else:
                return "No Permission", "Please login first or contact your administrator"
        else:
            return "Page not Found"


    async def handle_login_action(self, request=None):
        """!!! Private method, don't call. Manage user actions like button clicks
            handles /api/login
        """
       
        msg = await self.get_request_json(request)
        
        if 'password' in self.on_login:
            return self.on_login['password'](msg['username'], msg['password'])
        else:
            return "Login type not supported"
        
    def frontend(self, app:FastAPI, ui:BaseModel) -> None:
        from fastapi.middleware.cors import CORSMiddleware
        from fastapi.middleware.gzip import GZipMiddleware

        app.add_middleware(GZipMiddleware)
        app.add_middleware(
           CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.app = self.generateui(ui)

    def generateui(self,ui:BaseModel) -> APIRouter:
        @self.get("/")
        async def get_page_layout(request: Request):
            # Your implementation here
            return HTMLResponse(content=html)
        
        @self.get("/api/page_layout")
        async def get_page_layout(request: Request):
            # Your implementation here
            return ui.model_dump_json(indent=2)


        @self.get('/api/{page_path:path}')
        async def get_page_layout(page_path: str, request: Request):

            return await self.serve_page(page_path, request)
        return self.app