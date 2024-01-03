from .importcomp import import_antd_component
from .import_icon import import_antd_icon_component
from .client_event_type import eventtypelist
from .antd_componentmap import antdComponents
from .client_anyevent import iteratePropsAndAttachEventHandler
from .client_generic_eventhandler import genericEventHandler
from .convert_json_to_ui import convertJsonToAntdUi_
from .antd_ui import AntdUiFromJson
from pydantic import BaseModel

def generate_react_component(page_name, page_content:BaseModel):
    import_component = import_antd_component()
    import_icons = import_antd_icon_component()
    event_map = eventtypelist()
    antdComponentMap = antdComponents()
    anyevent =iteratePropsAndAttachEventHandler()
    eventhandler = genericEventHandler()
    convertui = convertJsonToAntdUi_()
    RenderAntdUi =AntdUiFromJson(content=page_content.model_dump_json(indent=2))
    react_compiler = f"""
        {import_component}
        {import_icons}
        {event_map}
        {antdComponentMap}
        {eventhandler}
        {anyevent}
        {convertui}
        {RenderAntdUi}       
        const {page_name}Component = () => {{
            return(<AntdUiFromJson/>)
        }};
        ReactDOM.render(React.createElement({page_name}Component), document.getElementById('root'));
    """
    
    # React-CDN hinzufügen
    react_cdn = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://cdn.jsdelivr.net/npm/axios@1.6.3/dist/axios.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/dayjs@1.11.10/dayjs.min.js"></script>
            <script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
            <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
            <script src="https://cdn.jsdelivr.net/npm/antd@5.12.4/dist/antd.min.js"></script>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/antd@5.12.4/dist/reset.min.css">
            <script src="https://cdnjs.cloudflare.com/ajax/libs/ant-design-icons/4.7.0/index.umd.min.js"></script>
            <script src="https://unpkg.com/babel-standalone@latest/babel.min.js" crossorigin="anonymous"></script>
            <title>Document</title>
        </head>
    """
    
    return f"{react_cdn}\n<body>\n<div id='root'></div>\n<script type='text/babel'>{react_compiler}</script></body></html>"
