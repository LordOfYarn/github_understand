
from pylablib.core.gui.utils import get_relative_position
from pylablib.devices import Thorlabs
import pylablib as pll
from pylablib.devices.Thorlabs import kinesis
from pylablib.devices.Thorlabs import TLCamera
from pylablib.devices import uc480

print(Thorlabs.list_kinesis_devices())
print(uc480.list_cameras())
#print(list_instruments())

#cam =Thorlabs.ThorlabsTLCamera(serial="4103252793")
cam = uc480.UC480Camera(cam_id=1)
img = cam.snap()

#basically stops the motors from runnign while I am working on the camera
temp=False
while(temp==True):
    motorx = kinesis.KinesisMotor(27002966) # the brush motor Id would need to
    motory = kinesis.KinesisMotor(27002991)# be changed if the motors get replaced

    #move to zero zero before moving to start position
    motorx.home(0)
    motory.home(0)
    motorx.wait_for_stop()
    motory.wait_for_stop()

    print("currently at (",motorx.get_position(),",",motory.get_position(),")")

    motorx.move_to(9)
    motory.move_to(9)
    motorx.wait_for_stop()
    motory.wait_for_stop()
    print("currently at (",motorx.get_position(),",",motory.get_position(),",")

    print(Thorlabs.list_kinesis_devices())

    print(motorx.get_position(),motory.get_position())
