from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon

from src.socket_tester_window import Ui_MainWindow
import base64
import socket
import sys
 
class SockerServerListener(QThread):
    finished = pyqtSignal()
    client = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super(SockerServerListener, self).__init__(parent)
        self.connection = None

    def property_value(self):
        return self.connection

    def set_property_value(self, value):
        self.connection = value
        
    def run(self):
        # Aquí va la lógica que se ejecutará en el hilo
        while True:
            if self.connection is not None:
                try:
                    self.connection.listen(1)
                    client_socket, client_address = self.connection.accept()

                    self.client.emit((client_socket, client_address))
                except Exception as e:
                    print(e)
                    self.connection = None

        self.finished.emit()
        
class SockerServerReader(QThread):
    finished = pyqtSignal()
    data_received = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super(SockerServerReader, self).__init__(parent)
        self.client = None
        
    def set_client_value(self, value):
        self.client = value
    
    def run(self):
        # Aquí va la lógica que se ejecutará en el hilo
        while True:
            conn, addr = self.client
            if conn is not None:
                try:
                    data = conn.recv(1024)
                    conn.sendall(data)
                    
                    self.data_received.emit((data.decode(), addr[0]))
                
                except Exception as e:
                    print(e)
                    self.connection = None

        self.finished.emit()

class SockerClientReader(QThread):
    finished = pyqtSignal()
    data_received = pyqtSignal(str)

    def __init__(self, parent=None):
        super(SockerClientReader, self).__init__(parent)
        self.connection = None
        
    def property_value(self):
        return self.connection

    def set_property_value(self, value):
        self.connection = value
        
    def run(self):
        # Aquí va la lógica que se ejecutará en el hilo
        while True:
            if self.connection is not None:
                try:
                    data = self.connection.recv(1024)
                    
                    self.data_received.emit(data.decode())
                
                except Exception as e:
                    print(e)
                    self.connection = None

        self.finished.emit()
        
class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.window_ = Ui_MainWindow()
        self.window_.setupUi(self)
        icon_data = b'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'
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap(QtGui.QImage.fromData(base64.b64decode(icon_data))))
   
   
        self.setWindowIcon(icon)
        #self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.setWindowTitle('Socket Tester')
        
        self.window_.bind.clicked.connect(self._on_bind_server)
        self.window_.Connect.clicked.connect(self._on_connect_client)
        self.window_.send.clicked.connect(self._on_send_client)
        self.window_.disconnect_client.clicked.connect(self._on_disconnect)
        self.window_.disconnect_server.clicked.connect(self._on_disconnect)
        self.window_.send_stream.clicked.connect(self._on_send_stream_server)
        self.window_.send_to.clicked.connect(self._on_send_to_server)
        
        self._FAMILY: int = socket.AF_INET
        self._TYPE: int = socket.SOCK_STREAM
        self.connection = None
        self.client_data: str = ""
        self.clients: list = []
    
    def _on_bind_server(self) -> None:
        try:
            ip: str = self.window_.ip_server.text()
            port: int = int(self.window_.port_server.text())
            
            
            self.connection.close() if self.connection != None else ...
            
            self.connection = socket.socket(self._FAMILY, self._TYPE)
            
            self.connection.bind((ip, port))
            
            self.client_reader = SockerServerListener()
            self.client_reader.client.connect(self._on_listen_server)
            self.client_reader.set_property_value(self.connection)
            self.client_reader.start()
            
            
            self.window_.client.setEnabled(False)
            self.window_.bind.setEnabled(False)
            self.show_dialog(title='Success', msg=f'Server successfully started on {ip}:{port}')
        
        except Exception as e:
            self.show_dialog(title='Error', msg=str(e))
    
    def _on_listen_server(self, client: tuple) -> None:
        self.server_reader = SockerServerReader()
        self.server_reader.data_received.connect(self._on_read_socket_server)
        self.server_reader.set_client_value(client)
        self.server_reader.start() 
        
        self.clients.append(client)
        
    def _on_connect_client(self) -> None:
        try:
            ip: str = self.window_.ip.text()
            port: int = int(self.window_.port.text())

            self.client_reader = SockerClientReader()
            self.client_reader.data_received.connect(self._on_read_socket)
            self.client_reader.start()
        
            self.connection.close() if self.connection != None else ...
            
            self.connection = socket.socket(self._FAMILY, self._TYPE)
            
            self.connection.connect((ip, port))
            
            self.client_reader.set_property_value(self.connection)
            
            self.window_.server.setEnabled(False)
            self.window_.Connect.setEnabled(False)
            
        except Exception as e:
            self.show_dialog(title ='Error', msg=f'{e}')
            self.connection = None
    
    def _on_send_client(self) -> None:
        if self.connection is not None:
            data: str = self.window_.message.text()
            end_char: str = ''
            end_char_idx: int = self.window_.end_char.currentIndex()
            
            if end_char_idx == 0: end_char = '\n' 
            if end_char_idx == 1: end_char = '\r\n' 
            if end_char_idx == 2: end_char = '\t'  
    
            data += end_char
                        
            print(data)
            
            self.connection.sendall(data.encode())
        else:
            self.show_dialog(msg='Server is not connected')
            
    def _on_send_stream_server(self) -> None:
        try:
            if self.connection is not None:
                data: str = self.window_.message_server.text()
                end_char: str = ''
                end_char_idx: int = self.window_.end_char_server.currentIndex()

                if end_char_idx == 0: end_char = '\n' 
                if end_char_idx == 1: end_char = '\r\n' 
                if end_char_idx == 2: end_char = '\t'  

                data += end_char

                [conn.sendall(data.encode()) for conn, _ in self.clients]
                
        except Exception as e:
            self.show_dialog('Error', str(e))
            
    def _on_send_to_server(self) -> None:
        try:
            if self.connection is not None:
                data: str = self.window_.message_server.text()
                ip: str = self.window_.ip_recipient.text()
                port: str = int(self.window_.port_server.text())
                
                end_char: str = ''
                end_char_idx: int = self.window_.end_char_server.currentIndex()
                
                if end_char_idx == 0: end_char = '\n' 
                if end_char_idx == 1: end_char = '\r\n' 
                if end_char_idx == 2: end_char = '\t'  
        
                data += end_char
                            
                if ip not in [addr[0] for _, addr in self.clients]:
                    self.show_dialog('Warning', f'{ip} was not found')
                else:
                    [conn.sendall(data.encode()) for conn, addr in self.clients if addr[0] == ip]
                
                
        except Exception as e:
            self.show_dialog('Error', str(e))
            
    def _on_read_socket(self, data: str) -> None:
        self.client_data += data        
        self.window_.textEdit.setText(self.client_data)
        self.window_.textEdit.verticalScrollBar().setValue(self.window_.textEdit.verticalScrollBar().maximum())
    
    def _on_read_socket_server(self, data: tuple) -> None:
        msg, client = data
        self.client_data += f'Message from {client} -> {msg}\n'        
        self.window_.server_text.setText(self.client_data)
        self.window_.server_text.verticalScrollBar().setValue(self.window_.server_text.verticalScrollBar().maximum())
        
    def show_dialog(self, title: str = 'Warning', msg: str = ''):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.adjustSize()

        label = QLabel(msg)

        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        dialog.setLayout(dialog_layout)

        dialog.exec_()
    
    def _on_disconnect(self) -> None:
        self.client_data = ""
        
        self.connection.close()
        self.connection = None
        
        self.window_.textEdit.setText(self.client_data)
        self.window_.server_text.setText(self.client_data)
        self.window_.server_text.verticalScrollBar().setValue(self.window_.server_text.verticalScrollBar().maximum())
        
        self.window_.server.setEnabled(True)
        self.window_.client.setEnabled(True)
        self.window_.Connect.setEnabled(True)
        self.window_.bind.setEnabled(True)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())