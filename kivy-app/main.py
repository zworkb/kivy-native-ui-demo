from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
import asyncio
import websockets
import jnius

package_name='org.kivy.kivynativeactivity'

async def response(websocket, path):
    msg = await websocket.recv()
    print("msg:", msg)
    await websocket.send("ok from local")

def start_native_activity():
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
        id:status
        text:'please start service'
    Button:
        id: btn_start_native
        text:'start native interface'
        on_release: root.on_start_native_activity()
    Button:
        id: btn_start_service
        text:'start service'
        on_release: root.on_start_service()
""")

class MainWindow(BoxLayout):
    """"""
    service_started = BooleanProperty(None)
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.bind(service_started=self.on_service_started)
        self.service_started = False
        
    def on_start_native_activity(self):
        start_native_activity()

    def on_start_service(self):
        start_service('Websockets')
        self.service_started = True

    def on_service_started(self, widget, started):
        self.ids.status.text='service started' if started else 'not started'
        self.ids.btn_start_native.opacity = 1 if started else .3
        self.ids.btn_start_service.opacity = .3 if started else 1
        


class LibTesterApp(App):
    def build(self):
        
        # start_server()
        # start_kotlin_activity()
        return MainWindow()

if __name__ == '__main__':
    LibTesterApp().run()
