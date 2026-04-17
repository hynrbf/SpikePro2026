from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Icon, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from colorcontroller import ColorController, MatColor
from shared import Shared, Speed


class WheelController:
    __wheel_diameter_in_mm = float(56)
    __axle_track_in_mm = float(145)

    __left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    __right_motor = Motor(Port.B)

    @staticmethod
    async def reset():
        await WheelController.__left_motor.run_target(Speed.Fast, 0)
        await WheelController.__right_motor.run_target(Speed.Fast, 0)
        await wait(100)

        state = WheelController.__object().state()
        print("State of robot is: ", state)

    @staticmethod
    async def move_forward(distance_in_mm: float, speed: float = Speed.Fast,
                           with_brake: bool = False):
        Shared.hub().display.icon(Icon.ARROW_DOWN)
        wheel_controller = WheelController.__object()

        if speed == Speed.Straight:
            # reset to None when moving straight, otherwise the yaw angle becomes not good
            wheel_controller.settings(straight_speed=None, straight_acceleration=None, turn_rate=None,
                                      turn_acceleration=None)
            # print("Straight only")
        elif speed == Speed.Fast:
            pass  # print("Faster forward")
        else:
            wheel_controller.settings(straight_speed=speed, straight_acceleration=None, turn_rate=None,
                                      turn_acceleration=None)

        if with_brake:
            await wheel_controller.straight(distance=distance_in_mm, then=Stop.BRAKE)
        else:
            await wheel_controller.straight(distance_in_mm)

        # travelled_distance = WheelController.__get_distance_in_mm()
        # print("Travelled distance in mm: ", travelled_distance)

    @staticmethod
    async def follow_the_line():
        speed = Speed.Medium
        lm = speed
        rm = speed
        #at speed 250 the fastest is 0.05
        #at speed 400 the fastest is 0.08
        kp = 0.20
        correction = round(speed * kp, 0)

        while True:
            color_int = await ColorController.get_mat_color()
            print("follow line color: ", color_int)

            if color_int == MatColor.White:
                lm = speed
                rm = speed
            # Drifted right → steer left
            elif color_int == MatColor.Black:
                lm = speed - correction
                rm = speed + correction
                # Drifted left → steer right
            elif color_int == MatColor.Others:
                lm = speed + correction
                rm = speed - correction

            print(f"lm {lm}, rm {rm}")
            WheelController.__left_motor.run(lm)
            WheelController.__right_motor.run(rm)
            await wait(10)

    @staticmethod
    async def move_backward(distance_in_mm: float, speed: float = Speed.Fast,
                            with_brake: bool = False):
        Shared.hub().display.icon(Icon.ARROW_UP)
        distance_in_mm = distance_in_mm * -1
        wheel_controller = WheelController.__object()

        if speed == Speed.Straight:
            # reset to None when moving straight, otherwise the yaw angle becomes not good
            wheel_controller.settings(straight_speed=None, straight_acceleration=None, turn_rate=None,
                                      turn_acceleration=None)
        elif speed == Speed.Fast:
            pass  # print("Faster backward")
        else:
            wheel_controller.settings(straight_speed=speed, straight_acceleration=None, turn_rate=None,
                                      turn_acceleration=None)

        if with_brake:
            await wheel_controller.straight(distance=distance_in_mm, then=Stop.BRAKE)
        else:
            await wheel_controller.straight(distance_in_mm)

        # travelled_distance = WheelController.__get_distance_in_mm()
        # print("Travelled distance in mm: ", travelled_distance)

    @staticmethod
    async def right_turn(angle_degrees: float = 90):
        if angle_degrees < 0:
            angle_degrees = angle_degrees * -1

        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(angle_degrees)

    @staticmethod
    async def right_u_turn(fast_turn: bool = True):
        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()

        if not fast_turn:
            wheel_controller = WheelController.__object_slow_turn()

        await wheel_controller.turn(180)

    @staticmethod
    async def left_turn(angle_degrees: float = 90):
        angle_degrees = angle_degrees * -1
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(angle_degrees)

    @staticmethod
    async def left_u_turn(fast_turn: bool = True):
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()

        if not fast_turn:
            wheel_controller = WheelController.__object_slow_turn()

        await wheel_controller.turn(-180)

    # debugging while wheels moving
    @staticmethod
    async def debug():
        hub = Shared.hub()

        while True:
            if hub.imu.stationary():
                hub.light.on(Color.BLUE)
            else:
                hub.light.on(Color.GREEN)

            yaw_angle = hub.imu.heading()
            heading_angle = WheelController.__get_heading_angle(yaw_angle)
            hub.display.number(round(yaw_angle))
            print('yaw_angle= ', "{:.1f}".format(yaw_angle), 'heading_angle= ', "{:.1f}".format(heading_angle))
            await wait(25)

            # # You can easily reset the heading to arbitrary values.
            # # No special wait operations are required here. Just reset and go.
            # if hub.buttons.pressed():
            #     hub.imu.reset_heading(0)

    @staticmethod
    def __get_heading_angle(yaw_angle):
        if yaw_angle <= 0:
            heading_angle = (-yaw_angle % 360)
        else:
            heading_angle = 360 - (yaw_angle % 360)

        return heading_angle

    @staticmethod
    def __get_distance_in_mm() -> int:
        wheel_controller = WheelController.__object()
        return wheel_controller.distance()

    @staticmethod
    def __object() -> DriveBase:
        return Shared.wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                       WheelController.__wheel_diameter_in_mm,
                                       WheelController.__axle_track_in_mm)

    @staticmethod
    def __object_slow_turn() -> DriveBase:
        return Shared.wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                       WheelController.__wheel_diameter_in_mm,
                                       WheelController.__axle_track_in_mm, 90)
