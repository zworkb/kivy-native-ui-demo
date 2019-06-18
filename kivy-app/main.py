from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import asyncio
import websockets
import jnius


async def response(websocket, path):
    msg = await websocket.recv()
    print("msg:", msg)
    await websocket.send("ok from local")


def start_server():
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ staarting server")
    server = websockets.serve(response, '*', 8077)
    asyncio.get_event_loop().run_until_complete(server)
    print("$$$$$$$$$$$$$$$$ finish server")


def start_kotlin_activity():
    print("start_kotlin_activity")
    # PythonActivity=jnius.autoclass("org.kivy.android.SpecialActivity")
    PythonActivity=jnius.autoclass("org.kivy.android.PythonActivity")
    print("PythonActivity:", PythonActivity)
    Compat = jnius.autoclass('android.support.v4.content.ContextCompat')
    print("Compat:", Compat)
    # currentActivity = jnius.cast('android.app.Activity', PythonActivity.mActivity)
    currentActivity = jnius.cast('org.kivy.android.SpecialActivity', PythonActivity.mActivity)
    print("current:", currentActivity)
    # activity=klass.mActivity
    currentActivity.startKotlinActivity()


def start_service(name):
    print("before loading service class")
    service = jnius.autoclass('org.bd.libtester.Service%s' % name)
    mActivity = jnius.autoclass('org.kivy.android.PythonActivity').mActivity
    # print('trying permissions')
    # mActivity.requestPermissions(['READ_EXTERNAL_STORAGE','WRITE_EXTERNAL_STORAGE'])
    argument = 'test argument ok'
    print('------before start')
    service.start(mActivity, argument)
    print('------after start')


Builder.load_string("""
<MainWindow>:
    orientation:'vertical'
    Label:
        text:'hello 9'
    Button:
        text:'start kotlin'
        on_release: root.on_start_kotlin_activity()
    Button:
        text:'start server'
        on_release: root.on_start_server()
    Button:
        text:'start service'
        on_release: root.on_start_service()
""")

class MainWindow(BoxLayout):
    """"""
    def on_start_kotlin_activity(self):
        start_kotlin_activity()

    def on_start_server(self):
        start_server()

    def on_start_service(self):
        start_service('Websockets')


class LibTesterApp(App):
    def build(self):
        
        # start_server()
        # start_kotlin_activity()
        return MainWindow()

if __name__ == '__main__':
    LibTesterApp().run()
