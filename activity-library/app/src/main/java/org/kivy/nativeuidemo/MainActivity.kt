package org.kivy.nativeuidemo

import androidx.appcompat.app.AppCompatActivity

import android.os.Bundle
import android.view.View
import io.ktor.client.HttpClient
import io.ktor.client.features.websocket.WebSockets
import io.ktor.client.features.websocket.ws
import io.ktor.http.HttpMethod
import io.ktor.http.cio.websocket.Frame
import io.ktor.http.cio.websocket.readText
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking

class MainActivity : AppCompatActivity() {
    val client = HttpClient {
        install(WebSockets)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun testConnection(ip: String, port: Int) {
        runBlocking {
            println("################ starting client")
            client.ws(
                method = HttpMethod.Get,
                host = ip,
                port = port, path = "/"
            ) {
                // Send text frame.
//                send("Hello, TextView frame")
                println("###########sending")

                // Send text frame.
                send(Frame.Text("Howdi"))

                // Send binary frame.
//                send(Frame.Binary(...))

                // Receive frame.
                val frame = incoming.receive()
                when (frame) {
                    is Frame.Text -> txtOutput.text=frame.readText()
//                    is Frame.Binary -> println(frame.readBytes())
                }
            }
        }
    }

    fun onSend(v: View){

        GlobalScope.launch(Dispatchers.IO) {
            testConnection("localhost", 8077)
        }
    }
}
