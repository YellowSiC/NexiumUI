

def AntdUiFromJson(content)->str:
    

    te = f"""

        const AntdUiFromJson = () => {{
        const [data, setData ] = React.useState({content})
        
            return(
            
            <div>
          
            {{convertJsonToAntdUi(data)}}
            </div>
            )
        }};
    """
    return te