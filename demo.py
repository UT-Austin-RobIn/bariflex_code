import odrive
import time

# Due to lower gains we can get more back-drivability
def set_gripper_to_off_state(odrv0):
    odrv0.axis0.controller.config.pos_gain = 3.0
    odrv0.axis0.controller.config.vel_gain = 0.13
    odrv0.axis0.controller.config.vel_integrator_gain = 0.1

def set_gripper_to_on_state(odrv0):
    odrv0.axis0.controller.config.pos_gain = 29.966
    odrv0.axis0.controller.config.vel_gain = 0.297
    odrv0.axis0.controller.config.vel_integrator_gain = 0.333

# min and max gripper values: [-0.03, 0.21]
def open_gripper(odrv0):
    if odrv0.axis0.current_state != 8:
        odrv0.axis0.requested_state = 8
    time.sleep(0.1) 
    set_gripper_to_on_state(odrv0)
    odrv0.axis0.controller.input_pos = 0.15

def close_gripper(odrv0):
    if odrv0.axis0.current_state != 8:
        odrv0.axis0.requested_state = 8
    time.sleep(0.1) 
    set_gripper_to_on_state(odrv0)
    odrv0.axis0.controller.input_pos = -0.01


# find the gripper
odrv0 = odrive.find_any()

# print out some gripper specific values to double check
print("Voltage: ", str(odrv0.vbus_voltage))
print("Current pos: ", odrv0.axis0.pos_vel_mapper.pos_rel)
print("Pos gain: ", odrv0.axis0.controller.config.pos_gain)
print("Vel gain: ", odrv0.axis0.controller.config.vel_gain)
print("Vel integrator gain: ", odrv0.axis0.controller.config.vel_integrator_gain)
print("Current state: ", odrv0.axis0.current_state)
print("speed: ", odrv0.axis0.controller.config.input_filter_bandwidth)

# open the gripper
open_gripper(odrv0)

# close the gripper
close_gripper(odrv0)