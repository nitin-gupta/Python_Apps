import sys
import threading
import time, datetime
from threading import Event, Thread

g_state_flag: bool
g_state_ctr: int