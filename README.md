# NexiumUI foundation 

<img src="https://github.com/YellowSiC/PyNexumJS/blob/main/logo.png" width="100%"/>
<p align="center">
  <a href="https://ant.design">
    <img width="100" src="https://gw.alipayobjects.com/zos/rmsportal/KDpgvguMpGfqaHPjicRK.svg">
  </a>
</p>

<h3 align="center">NexiumUI with Ant Design UI</h1>

<p align="center">Create an efficient and enjoyable work experience</p>

![](https://gw.alipayobjects.com/mdn/rms_08e378/afts/img/A*zx7LTI_ECSAAAAAAAAAAAABkARQnAQ)
<p>NexiumUI empowers developers to effortlessly build real-time web, mobile, and desktop applications in Python, without requiring prior frontend experience.</p>
<p>It is an incredibly powerful Python library that allows you to create cross-platform graphical user interface and Web applications with ease, similar to Electronjs, but with an integrated React  and Ant Design user interface.</p>



## ⚡ From idea to app in minutes
<p>This feature makes NexiumUI an ideal choice for creating sophisticated and comprehensive applications, catering to even the most demanding use cases.</p>
<p>At the heart of NexiumUI's architecture are cutting-edge technologies such as React, FastAPI, Pydantic, Chrome, and Uvicorn, providing an excellent platform for building high-quality applications that seamlessly blend into any environment.</p>
<p>NexiumUI also supports the Python ZVT 700 electronic cash register interface, allowing for seamless integration of other transactions into your applications. Additionally, NexiumUI supports PWA Progressive Web Applications, enabling easy installation of your app on IOS and Android operating systems.</p>




## 🔋 Batteries included
<p>If you're looking for a robust and versatile library to create visually stunning applications, then NexiumUI is undoubtedly the right choice. Explore the full potential of this exceptional library by giving it a try today!</p>
<a href="https://badge.fury.io/py/NexiumUI"><img src="https://badge.fury.io/py/NexiumUI.svg" alt="PyPI version" height="18"></a>
<a href='https://NexiumUI-document.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/NexiumUI-document/badge/?version=latest' alt='Documentation Status' />
</a>

## 📐 Simple architecture

No more complex architecture with JavaScript frontend, REST API backend, database, cache, etc. With NexiumUI you just write a monolith stateful app in Python only and get multi-user, realtime Single-Page Application (SPA).
## ✨ Features

- browser-based graphical user interface
- standard GUI elements like label, button, checkbox, switch, slider, input, file upload, ...
- simple grouping with rows, columns, cards and dialogs
- general-purpose HTML and Markdown elements
- powerful high-level elements to
  - plot graphs and charts,
  - render 3D scenes,
  - get steering events via virtual joysticks
  - annotate and overlay images
  - interact with tables
  - navigate foldable tree structures
- notifications, dialogs and menus to provide state of the art user interaction
- shared and individual web pages
- ability to add custom routes and data responses
- capture keyboard input for global shortcuts etc.
- customize look by defining primary, secondary and accent colors
- live-cycle events and session data




  ![](https://user-images.githubusercontent.com/507615/209472919-6f7e8561-be8c-4b0b-9976-eb3c692aa20a.png)

   ![](https://caphe.sfo2.cdn.digitaloceanspaces.com/assets/images/ant-design-1.jpg)


## 🖥 Environment Support

- Modern browsers
- Client-side Rendering

## Browsers support

| [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png" alt="IE / Edge" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>IE / Edge | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png" alt="Firefox" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Firefox | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" alt="Chrome" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Chrome | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png" alt="Safari" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Safari | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari-ios/safari-ios_48x48.png" alt="iOS Safari" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>iOS Safari | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/samsung-internet/samsung-internet_48x48.png" alt="Samsung" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Samsung | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/opera/opera_48x48.png" alt="Opera" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br/>Opera |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| IE11, Edge| last 2 versions| last 2 versions| last 2 versions| last 2 versions| last 2 versions| last 2 versions 


## 📦 Install

```bash
pip install nexium
```
## 🔨 Usage

Write your NexiumUI UI:

```python


from fastapi import FastAPI
from nexium import ui , NexiumUI, e









api = FastAPI()
client = NexiumUI()
client.init(app=api)
api.include_router(client)





page = {
    'display': 'flex',
    'flexDirection': 'column',
    'alignItems': 'center',
    'justifyContent': 'center',
    'height': '80vh',  # Vollständige Bildschirmhöhe
}

nav = {
    'fontSize': '100px',
    'fontWeight': 'bold',
    'color': '#E50914',  # Netflix-Rot
    'cursor': 'pointer',
    'marginBottom': '10px',  # Abstand zwischen Nexium und Beschreibung
}

description = {
    'fontSize': '14px',
    'color': '#555',
    'textAlign': 'center',  # Zentrierung des Textes
}


d ="""
Nexium empowers developers to effortlessly build real-time web, mobile, and desktop applications in Python, without requiring prior frontend experience.

It is an incredibly powerful Python library that allows you to create cross-platform graphical user interface and Web applications with ease, similar to Electronjs, but with an integrated React and Ant Design user interface.
"""

@api.get("/")
async def read_root():
  """ Nexium First API Endpoint """
  return ui.Layout(
    content=[
      ui.Content(style=page, content=[
        ui.Title(content='Nexium', style=nav),
        ui.Title(content='Nexium with Ant Design UI', style=description),
        ui.Text(content=d, style=description),
      ]),
      ui.Footer(
        content=[
          ui.ReactNode(component='h4', content='Nexium ©2024 Created by Malek Ali at Yellow-SiC Development'),
          ],
        style={
          'display': 'flex',
          'justifyContent': 'center',
          'alignItems': 'center',
          'fontSize': '13px',
          'color': '#333',  
          'margin':'15px'
        }
      )
    ],
      style = {
      'height':'100%'
      }
  )



   
```


### In January 2024, NexiumUI has just been publicly released by software architecture Malek Ali at Yellow-SiC and is in Alpha Stage.
Anyone can install and use NexiumUI. There may be issues, but we are actively working to resolve them.


## 🤝 Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
