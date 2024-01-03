

def iteratePropsAndAttachEventHandler()->str:
    te = """

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
    
    """
    return te
