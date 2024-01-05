



def useref()->str:
    t ="""
        function LogRefValue ({ id, useRefProp }) {
            const targetElement = document.getElementById(id);
            console.log('hallo')
                if (targetElement && targetElement[useRefProp]) {
                    console.log(`Ref property "${useRefProp}" of element with ID "${id}":`, targetElement[useRefProp]);
                } else {
                    console.error(`Element with ID "${id}" or ref property "${useRefProp}" not found.`);
                }
        };
    """
    return t



def create_html_file(file_path, html_content):
    try:
        with open(file_path, 'w') as html_file:
            html_file.write(html_content)
        print(f'Die HTML-Datei wurde erfolgreich erstellt: {file_path}')
    except Exception as e:
        print(f'Fehler beim Erstellen der HTML-Datei: {e}')