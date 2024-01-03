


def convertJsonToAntdUi_()->str:
    te = """
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
    """
    return te