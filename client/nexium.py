html = """

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
<body>
    <div id="root"></div>
    <script type="text/babel">
        const {            Button,
            FloatButton,
            Typography,
            Divider,
            Flex,
            Grid,
            Layout,
            Space,
            Anchor,
            Breadcrumb,
            Dropdown,
            Menu,
            Pagination,
            Steps,
            AutoComplete,
            Cascader,
            Checkbox,
            ColorPicker,
            DatePicker,
            Form,
            Input,
            InputNumber,
            Mentions,
            Radio,
            Rate,
            Select,
            Slider,
            Switch,
            TimePicker,
            Transfer,
            TreeSelect,
            Upload,
            Avatar,
            Badge,
            Calendar,
            Card,
            Carousel,
            Collapse,
            Descriptions,
            Empty,
            Image,
            List,
            Popover,
            QRCode,
            Segmented,
            Statistic,
            Table,
            Tabs,
            Tag,
            Timeline,
            Tooltip,
            Tour,
            Tree,
            Alert,
            Drawer,
            Message,
            Modal,
            Notification,
            Popconfirm,
            Progress,
            Result,
            Skeleton,
            Spin,
            Watermark,
            Affix,
            App,
            ConfigProvider } = antd;
        const { Header, Content, Sider, Footer } = Layout;
        const antdComponents = {
            Header, 
            Content, 
            Sider, 
            Footer,
            Button,
            FloatButton,
            Typography,
            Divider,
            Flex,
            Grid,
            Layout,
            Space,
            Anchor,
            Breadcrumb,
            Dropdown,
            Menu,
            Pagination,
            Steps,
            AutoComplete,
            Cascader,
            Checkbox,
            ColorPicker,
            DatePicker,
            Form,
            Input,
            InputNumber,
            Mentions,
            Radio,
            Rate,
            Select,
            Slider,
            Switch,
            TimePicker,
            Transfer,
            TreeSelect,
            Upload,
            Avatar,
            Badge,
            Calendar,
            Card,
            Carousel,
            Collapse,
            Descriptions,
            Empty,
            Image,
            List,
            Popover,
            QRCode,
            Segmented,
            Statistic,
            Table,
            Tabs,
            Tag,
            Timeline,
            Tooltip,
            Tour,
            Tree,
            Alert,
            Drawer,
            Message,
            Modal,
            Notification,
            Popconfirm,
            Progress,
            Result,
            Skeleton,
            Spin,
            Watermark,
            Affix,
            App,
            ConfigProvider
        }



        const eventtypelist = ["onClick", "onChange"];

        const genericEventHandler = (event, e) => {
            if (!event || !event.event_type) return;

            switch (event.event_type) {
                case 'NavigateToEvent':
                    // window.location.host = 'https://example.com';
                    alert(e);
                    console.log(event.event_type, e);
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
                default:
                    break;
            }
        };
        const iteratePropsAndAttachEventHandler = (props) => {
            const updatedProps = { ...props };
            for (const propName in updatedProps) {
                if (eventtypelist.includes(propName)) {
                    const eventTypeValue = updatedProps[propName];
                    updatedProps[propName] = (e) => genericEventHandler(eventTypeValue, e);
                }
            }
            return updatedProps;
        };

        const convertJsonToAntdUi = (json) => {
            if (!json || !json.component) return null;
            const { component, content, props } = json;
            const updatedProps = iteratePropsAndAttachEventHandler(props);

            const Component = antdComponents[component];

            return (
                <Component {...updatedProps}>
                    {content && (
                        Array.isArray(content)
                            ? content.map((item, index) => (
                                <div key={index}>{convertJsonToAntdUi(item)}</div>
                            ))
                            : content
                    )}
                </Component>
            );
        };

        const AntdUiFromJson = ({ json }) => (
            <div>{convertJsonToAntdUi(json)}</div>
        );

        const Render = () => {
            const [jsonData, setJsonData] = React.useState({});

            React.useEffect(() => {
                axios.get('http://localhost:8000/api/page_layout')
                    .then(response => setJsonData(JSON.parse(response.data)))
                    .catch(error => console.error('Error fetching data:', error));
            }, []);

            return <AntdUiFromJson json={jsonData} />;
        };

        ReactDOM.render(
            <Render />,
            document.querySelector('#root'),
        );
    </script>
</body>
</html>






"""

