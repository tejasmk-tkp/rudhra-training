import pygame
import sys
import time
import serial as sl

#motor_driver = sl.serial("/dev/ttyUSB0")

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

            #print(f"Left: {left_stick}")
            #print(f"Right: {right_stick}")

            return left_stick

    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()

def map_range(value, from_low, from_high, to_low, to_high):

    normalized_value = (value - from_low)/(from_high - from_low)

    mapped_value = round(to_low + normalized_value * (to_high - to_low))

    return max(to_low, min(to_high, mapped_value))

while True:
    controlValue = controller()
    #print(controlValue[0])

    '''#Forward and Backward (1, -1)
    M1_forward = map_range(controlValue[1], 1, -1, 1, 127)
    M2_forward = map_range(controlValue[1], 1, -1, 128, 255)
    f_data = bytes([M1_forward, M2_forward])
    print(controlValue[1], M1_forward, M2_forward, f_data)
    #motor_driver.write(f_data)'''

    #Left (-1, 0)
    M1_turn = map_range(controlValue[0], 0, -1, 64, 127) #Left Motor
    M2_turn = map_range(controlValue[0], 0, -1, 192, 255) #Right Motor
    t_data = bytes([M1_turn, M2_turn])
    print(controlValue[0], M1_turn, M2_turn, t_data)


    '''#Right (0, 1)
    M1_backward = map_range(controlValue[1], 0, 1, , ) #Left Motor
    M2_backward = map_range(controlValue[1], 0, 1, , ) #Right Motor'''

    time.sleep(0.1)
