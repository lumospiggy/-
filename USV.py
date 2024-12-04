from Solution.Base import *
import time
from ctypes import *
from time import sleep
import threading
import serial
from geographiclib.geodesic import Geodesic

class USV_Misson(object):   
    def __init__(self):
        super().__init__()
        # self.usb = USB()
        # self.base = Base()
        self.ser = serial.Serial('COM7', 115200, timeout=1)
        if not self.ser.is_open:
            self.ser.open()
        self.GPS_DATA = [0,0,0,0] # [longitude, latitude, heading, speed]
        self.TargetLon= 0.0
        self.TargetLat= 0.0
        self.running = True 

    def GPS_Task(self):
        try:
            while self.running:
                data = self.ser.readline().decode('utf-8').strip()
                if data.startswith("$KSXT"):
                    parts = data.split(',')  
                    self.GPS_DATA[0] = float(parts[2])
                    self.GPS_DATA[1] = float(parts[3])
                    self.GPS_DATA[2] = float(parts[7])
                    self.GPS_DATA[3] = float(parts[8])
                    # print(f"Longitude: {self.GPS_DATA[0]}, Latitude: {self.GPS_DATA[1]}, Heading: {self.GPS_DATA[2]}, Speed: {self.GPS_DATA[3]} km/h")
        except serial.SerialTimeoutException:
            print("Serial timeout")
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
        finally:
            self.ser.close()

    def Navi_Task(self):
        while self.running:
            if self.GPS_DATA[0] != 0 and self.GPS_DATA[1] != 0:
                geodict = Geodesic.WGS84.Inverse(self.GPS_DATA[1], self.GPS_DATA[0], self.TargetLat, self.TargetLon)
                distance = geodict['s12']  # 距离，单位为米
                az = geodict['azi1']      # 方位角，从当前位置到目标位置的角度，单位为度
                

    def start_threads(self):
        threading.Thread(target=self.GPS_Task).start()
        threading.Thread(target=self.Navi_Task).start()

    def stop_threads(self):
        self.running = False

if __name__ == '__main__':
    USV = USV_Misson()
    USV.start_threads()
    sleep(3) 
    USV.stop_threads()