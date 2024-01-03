

def genericEventHandler()->str:
    te = """
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
    """
    return te



