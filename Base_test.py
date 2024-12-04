from Solution.Base import *
import time

if __name__ == '__main__':
    base = Base()
    # base.GPIO_Init(Pin='P0', Mode='OpenDrain',PuPD=GPIO_PUPD_NOPULL)
    # base.GPIO_Write(Pin='P0', level=1)
    # print(base.GPIO_Read(Pin='P0'))
    base.PWM_Init('P0',Prescaler=20000,Pulse=30)
    base.PWM_Start('P0',0)
    time.sleep(5)
    base.PWM_SetPulse('P0',Pulse=[12,50,50,50,50,50,50,50])
