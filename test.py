from ctypes import *
from time import sleep
import time
from Component.USB_class import *
            
if __name__ == '__main__':
    USB = USB()
    USB.device_init()
    time.sleep(1)
    # USB.GPIO_SetOpenDrain(0xFFFF,GPIO_PUPD_NOPULL)

    USB.PWM_Init(0xFF,[1,1,1,1,1,1,1,1],[20000,10,10,10,10,10,10,10],[15,30,30,30,30,30,30,30])
    USB.PWM_Start(0xFF,2000000)
    time.sleep(2)
    USB.PWM_SetPulse(0xFF,[18,50,50,50,50,50,50,50])
    USB.PWM_Start(0xFF,0)
    time.sleep(5)
    USB.PWM_SetPulse(0xFF,[12,50,50,50,50,50,50,50])

    # USB.GPIO_Write(0xFFFF,0xFFF2)
    # # GPIO_Read用法，还没有优化，但能用了
    # pin_value = c_ushort()
    # # 读取所有GPIO引脚的状态
    # USB.GPIO_Read(0xFFFF, byref(pin_value))
    # # 将16位值分解为16个独立的GPIO引脚状态,for循环后pinValue[i]即为Pin i的状态
    # pinValue = [0] * 16
    # for i in range(16):
    #     pinValue[i] = (pin_value.value >> i) & 1
    #     print(f"GPIO Pin {i} Value: {pinValue[i]}")

    # UART Test
    # UARTIndex = 0
    # UARTConfig = UART_CONFIG()
    # UARTConfig.BaudRate = 115200
    # UARTConfig.WordLength = UART_WORD_LENGTH_8BIT
    # UARTConfig.StopBits = UART_STOP_BITS_1
    # UARTConfig.Parity = UART_PARITY_NO
    # UARTConfig.TEPolarity = UART_TE_DISEN
    # USB.UART_Init(UARTIndex, UARTConfig)
    # WriteBuffer = (c_byte * 128)()
    # for i in range(0,len(WriteBuffer)):
    #     WriteBuffer[i] = i
    # USB.UART_WriteBytes(UARTIndex, "WriteBuffer") # 这里还不确定发过来是不是真正的“WriteBuffer”,商家提供的版本是ctype,具体可以在函数实现里改成py或ctype
    # ReadBuffer = (c_byte * 10240)()#接收数据缓冲区可以尽量大一点，以免缓冲区溢出
    # USB.UART_ReadBytes(UARTIndex, ReadBuffer, 1000) # 读取数据，超时时间1000ms

              
