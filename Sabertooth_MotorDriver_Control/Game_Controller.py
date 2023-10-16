import pygame
import sys
import time
import serial as sl

motor_driver = sl.serial("/dev/ttyUSB0")

def controller():
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        print("No game controllers found")
        pygame.quit()
        sys.exit(1)

    controller = pygame.joystick.Joystick(0)
    controller.init()

    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            left_stick = (controller.get_axis(0), controller.get_axis(1))
            #right_stick = (controller.get_axis(2), controller.get_axis(3))

            print(f"Left: {left_stick}")
            #print(f"Right: {right_stick}")

            return left_stick

    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()

def map_range(value, from_low, from_high, to_low, to_high):

    value = int(value)

    normalized_value = (value - from_low)/(from_high - from_low)

    mapped_value = round(to_low + normalized_value * (to_high - to_low))

    return max(to_low, min(to_high, mapped_value))

while True:
    controlValue = controller()
    print(controlValue)

    #Forward (0, 1)
    M1_forward = map_range(controlValue[0], 0, 1, 64, 127)
    M2_forward = map_range(controlValue[0], 0, 1, 192, 255)
    f_data = bytes([M1_forward, M2_forward])
    motor_driver.write(f_data)

    #Backward (-1, 0)
    M1_backward = map_range(controlValue[0], -1, 0, 1, 64)
    M2_backward = map_range(controlValue[0], -1, 0, 128, 192)
    b_data = bytes([M1_backward, M2_backward])
    motor_driver.write(b_data)

    #Left (-1, 0)
    M1_backward = map_range(controlValue[1], -1, 0, , ) #Left Motor
    M2_backward = map_range(controlValue[1], -1, 0, , ) #Right Motor

    #Right (0, 1)
    M1_backward = map_range(controlValue[1], 0, 1, , ) #Left Motor
    M2_backward = map_range(controlValue[1], 0, 1, , ) #Right Motor

    time.sleep(0.01)
