from fastapi.responses import HTMLResponse
from .importcomp import import_antd_component
from .import_icon import import_antd_icon_component
from .client_event_type import eventtypelist
from .antd_componentmap import antdComponents
from .client_anyevent import iteratePropsAndAttachEventHandler
from .convert_json_to_ui import convertJsonToAntdUi_
from .chart import NexiumUIChart, NexiumUIRealTimeChart
from .utils import useref
from .antd_ui import AntdUiFromJson
from pydantic import BaseModel



def EventHandler() -> str:
    te = """
        const genericEventHandler = (event, e) => {
            if (!event || !event.event_type) return;

            switch (event.event_type) {
                case 'PageNavigationEvent':
                    const loc = history.push('/api/' + event.path);
                    // window.parent.location = loc
                    window.location.reload();
                    break;
                case 'APIRequestEvent':
                    async function FetchApi() {
                        const { method, url, data, headers, auth, timeout, proxies, verify, cookies } = event;

                        if (!method || !url) {
                            console.error('Missing required properties for APIRequestEvent:', event);
                            return;
                        }

                        const axiosConfig = {
                            method,
                            url,
                            headers: {
                                'Content-Type': 'application/json',
                                ...(headers || {}),
                            },
                            data,
                            timeout: timeout || 0, // Set timeout to 0 for no timeout
                            auth,
                            proxy: proxies,
                            httpsAgent: verify ? undefined : false,
                            withCredentials: cookies ? true : false,
                        };

                        try {
                            const response = await axios(axiosConfig);

                            if (response.status === 200) {
                                console.log(response.data);
                            } else {
                                throw new Error(`Fehler bei der Anfrage: ${response.status} ${response.statusText}`);
                            }
                        } catch (error) {
                            console.error('Fehler bei der Anfrage:', error.message);
                            throw error;
                        }
                    }

                    FetchApi();
                    break;
                default:
                    break;
            }
        };
        """
    return te


async def initial_component(page_name, page_content: BaseModel,language:str):
    import_component = import_antd_component()
    import_icons = import_antd_icon_component()
    event_map = eventtypelist()
    antdComponentMap = antdComponents()
    anyevent = iteratePropsAndAttachEventHandler()
    eventhandler = EventHandler()
    convertui = convertJsonToAntdUi_()
    chart_1 = NexiumUIChart()
    chart_2 = NexiumUIRealTimeChart()
    ref = useref()
    RenderAntdUi = AntdUiFromJson(content=page_content.model_dump_json())
    import_router_dom = """const { BrowserRouter, Route, Link, useHistory } = ReactRouterDOM;"""
    react_compiler = f"""
    
        {import_component}
        {import_icons}
        {import_router_dom}
        {ref}
        {chart_1}
        {chart_2}
        const {page_name}Component = () => {{
            const history = useHistory();
            {event_map}
            {antdComponentMap}
            {eventhandler}
            {anyevent}
            {convertui}
            {RenderAntdUi}

            return(<AntdUiFromJson/>)
        }};

        ReactDOM.render(
            <BrowserRouter>
                <Route path={{window.location.pathname}} exact component={{() => <{page_name}Component />}} />
            </BrowserRouter>,
            document.getElementById('root')
        )
    """

    react_cdn = f"""
        <!DOCTYPE html>
        <html lang="{language}">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://cdn.jsdelivr.net/npm/axios@1.6.3/dist/axios.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/dayjs@1.11.10/dayjs.min.js"></script>
            <script src="https://unpkg.com/react@18/umd/react.production.min.js" crossorigin></script>
            <script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js" crossorigin></script>
            <script crossorigin src="https://unpkg.com/react-router-dom@5.3.0/umd/react-router-dom.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/antd@5.12.4/dist/antd.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@antv/g2plot@2.4.31/dist/g2plot.min.js"></script>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/antd@5.12.4/dist/reset.min.css">
            <script src="https://cdnjs.cloudflare.com/ajax/libs/ant-design-icons/4.7.0/index.umd.min.js"></script>
            <script src="https://unpkg.com/babel-standalone@latest/babel.min.js" crossorigin="anonymous"></script>
            <title>{page_name}</title>
        </head>
    """
    template = f"{react_cdn}\n<body>\n<div id='root'></div>\n<script type='text/babel'>{react_compiler}</script></body></html>"
    return HTMLResponse(content=template)
