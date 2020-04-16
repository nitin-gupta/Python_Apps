import sys
import threading
import time, datetime
from threading import Event, Thread
import serial

# Global Variable for serial port
g_serial_port_connect_flag: bool
g_serial_port_tx_flag: bool
g_serial_port_rx_flag:bool
g_serial_port_rx_data:str
g_serial_port_tx_data:str


g_state_flag: bool
g_state_ctr: int
