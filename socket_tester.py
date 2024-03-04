from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtGui

from src.socket_tester_window import Ui_MainWindow
import qdarkstyle
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
        self.setWindowIcon(QtGui.QIcon('./static/icon.png'))
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