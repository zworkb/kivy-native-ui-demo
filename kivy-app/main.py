from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import asyncio
import websockets
import jnius

package_name='org.kivy.kivynativeactivity'

async def response(websocket, path):
    msg = await websocket.recv()
    print("msg:", msg)
    await websocket.send("ok from local")

def start_kotlin_activity():
    print("start_kotlin_activity")
    # PythonActivity=jnius.autoclass("org.kivy.android.SpecialActivity")
    PythonActivity=jnius.autoclass("org.kivy.android.PythonActivity")
    print("PythonActivity:", PythonActivity)
    currentActivity = jnius.cast('org.kivy.android.SpecialActivity', PythonActivity.mActivity)
    print("current:", currentActivity)
    # activity=klass.mActivity
    currentActivity.startKotlinActivity()


def start_service(name):
    print("before loading service class")
    service = jnius.autoclass('%s.Service%s' % (package_name,name))
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
