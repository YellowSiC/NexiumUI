


def convertJsonToAntdUi_()->str:
    te = """
            function ReactNode({ component, props, content }) {
                const Element = component;

                return <Element {...props}>{
                content && (
                    Array.isArray(content)
                        ? content.map((item, index) => (
                            <div key={index}>{convertJsonToAntdUi(item)}</div>
                        ))
                        : <div>{content}</div>
                    )
                }</Element>;
            }
            
            const convertJsonToAntdUi = (json) => {
            if (!json || !json.component) return null;

            const { component, content, props } = json;
            const Component = antdComponents[component];
            const updatedProps = iteratePropsAndAttachEventHandler(props);

            if (!Component) {
                return ReactNode({component, props:updatedProps, content})
            }

            return (
                <Component {...updatedProps}>
                    {content && (
                        Array.isArray(content)
                            ? content.map((item, index) => (
                                <div key={index}>{convertJsonToAntdUi(item)}</div>
                            ))
                            : <div>{content}</div>
                    )}
                </Component>
            );
        };


    """
    return te