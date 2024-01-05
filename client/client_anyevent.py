

def iteratePropsAndAttachEventHandler()->str:
    te = """
        const react_node_as_props = ["subTitle","title"];

        const iteratePropsAndAttachEventHandler = (props) => {
            const updatedProps = { ...props };
            for (const propName in updatedProps) {
                if (eventtypelist.includes(propName)) {
                    const eventTypeValue = updatedProps[propName];
                    updatedProps[propName] = (e) => genericEventHandler(eventTypeValue, e);
                }
                if (react_node_as_props.includes(propName)) {
                    console.log(propName)
                    const reactNodeValue = updatedProps[propName];
                    updatedProps[propName] = convertJsonToAntdUi(reactNodeValue);
                }
            }

            // Gib das modifizierte props-Objekt zurück
            return updatedProps;
        };

    
    """
    return te
