


def NexiumUIChart():
    chart ="""
        function NexiumUIChart(props) {
            const {
                style,
                chartType,
                container_id,
                data,
                xField,
                yField,
                width,
                height,
                title_text,
                descriptionText,
                theme,
                legend_position,
                xAxis,
                yAxis,
                binNumber,
                color,
                min,
                max,
                tooltip_visible,
                fontSize,
            } = props;

            const plotConfig = {
                title: {
                    visible: true,
                    text: title_text,
                },
                description: {
                    visible: true,
                    text: descriptionText,
                },
                data,
                xField,
                yField,
                theme,
                width,
                height,
                legend: {
                    visible: true,
                    position: legend_position,
                },
                xAxis: {
                    ...xAxis,
                    title: {
                        ...xAxis.title,
                        style: {
                            fontSize: fontSize || 12,
                        },
                    },
                },
                yAxis: {
                    ...yAxis,
                    title: {
                        ...yAxis.title,
                        style: {
                            fontSize: fontSize || 12,
                        },
                    },
                },
                binNumber,
                color,
                min,
                max,
                tooltip: {
                    visible: tooltip_visible,
                },
            };
        // useEffect hook is not closed properly
        React.useEffect(() => {
            const Plot = new G2Plot[chartType](document.getElementById(container_id), plotConfig);

            Plot.render();

            // Aufräumen, wenn die Komponente unmounted wird
            return () => Plot.destroy();

            // Der useEffect-Hook benötigt keine Abhängigkeiten mehr, da Echtzeitaktualisierung entfernt wurde
            // eslint-disable-next-line react-hooks/exhaustive-deps
        }, [chartType, container_id, data, xField, yField, width, height, title_text, descriptionText, theme, legend_position, xAxis, yAxis, binNumber, color, min, max, tooltip_visible, fontSize]);

        return <div id={container_id} style={style} />;
        }

    """
    return chart




def NexiumUIRealTimeChart()->str:
    t = """


    function NexiumUIRealTimeChart(props) {
        const {
            style,
            chartType,
            container_id,
            xField,
            yField,
            width,
            height,
            title_text,
            descriptionText,
            theme,
            legend_position,
            xAxis,
            yAxis,
            binNumber,
            color,
            min,
            max,
            tooltip_visible,
            fontSize,
            websocketURL,
        } = props;

        const plotConfig = {
            title: {
                visible: true,
                text: title_text,
            },
            description: {
                visible: true,
                text: descriptionText,
            },
            data: [], // Start with an empty dataset
            xField,
            yField,
            theme,
            width,
            height,
            legend: {
                visible: true,
                position: legend_position,
            },
            xAxis: {
                ...xAxis,
                title: {
                    ...xAxis.title,
                    style: {
                        fontSize: fontSize || 12,
                    },
                },
            },
            yAxis: {
                ...yAxis,
                title: {
                    ...yAxis.title,
                    style: {
                        fontSize: fontSize || 12,
                    },
                },
            },
            binNumber,
            color,
            min,
            max,
            tooltip: {
                visible: tooltip_visible,
            },
        };

        React.useEffect(() => {
                const containerElement = document.getElementById(container_id);

                if (!containerElement) {
                    console.error(`Container element with id '${container_id}' not found.`);
                    return;
                }

                const Plot = new G2Plot[chartType](containerElement, plotConfig);

                const socket = new WebSocket(websocketURL);

                socket.onmessage = (event) => {
                    const newData = JSON.parse(event.data);
                    Plot.changeData(newData);
                };

                return () => {
                    socket.close();
                    Plot.destroy();
                };
            }, [chartType, container_id, /* other dependencies */]);

            return <div id={container_id} style={style} />;
        }
    """
    return t