import asyncio
import websockets
from PySide6.QtCore import QObject, Signal




class WebSocketServer(QObject):
    connected = Signal(str)
    change_url = Signal(str)
    browse_url = Signal(str)
    change_text = Signal(str)
    next_event = Signal()
    next_spende = Signal()
    change_screen = Signal(str)
    
    def __init__(self):
        super().__init__()
        self.host = ""
        self.port = 8001
        self.loop = None

    async def handler(self, websocket, path):
        print(f"Client connected from {websocket.remote_address}")
        self.connected.emit(websocket.remote_address)
        try:
            while True:
                message = await websocket.recv()
                print(message)
                cmd,value = self.getCommand(message)
                if cmd in ["izr","prayer","app"]:
                    self.change_url.emit(cmd)
                    self.change_screen.emit(cmd)
                elif cmd == "url":
                    self.browse_url.emit(value)
                    self.change_screen.emit(cmd)
                elif cmd == "next_event":
                    self.next_event.emit()
                    self.change_screen.emit(cmd)
                elif cmd == "text":
                    self.change_text.emit(value)
                    self.change_screen.emit(cmd)
                elif cmd == "next_spende":
                    self.next_spende.emit(value)
                    self.change_screen.emit(cmd)
                else:
                    None
        except websockets.exceptions.ConnectionClosed:
            print(f"Client {websocket.remote_address} disconnected")
    def getCommand(self,str):
        words = str.split("?")
        if len(words) == 2:
            cmd = words[0].strip()
            value = words[1].strip()
            return cmd, value
        else:
            cmd = words[0].strip()
            value = ""
            return cmd,value  # Return None if input format is incorrect
    def start(self):
        async def _start_server():
            async with websockets.serve(self.handler, self.host, self.port):
                await asyncio.Future()  # run forever
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.create_task(_start_server())
        self.loop.run_forever()

    def stop(self):
        print("stopping")
        if self.loop and not self.loop.is_closed():
            self.loop.stop()
            self.loop.close()
        else:
            print("Event loop is not running or already closed.")