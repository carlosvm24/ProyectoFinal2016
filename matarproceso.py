import os
import signal
print("Dame el PID del proceso que quieres matar")
numero_de_proceso = int(raw_input())
os.kill(numero_de_proceso, signal.SIGKILL)
