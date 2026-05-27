from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Icon, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# from colorcontroller import ColorController, MatColor
from shared import Shared, Speed


class WheelController:
    __wheel_diameter_in_mm = float(60)  # float(56)
    __axle_track_in_mm = float(160)  # float(145)

    __left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
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

    @staticmethod
    async def right_turn(angle_degrees: float = 90):
        if angle_degrees < 0:
            angle_degrees = angle_degrees * -1

        Shared.hub().display.icon(Icon.ARROW_LEFT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(angle_degrees)

    @staticmethod
    async def left_turn(angle_degrees: float = 90):
        angle_degrees = angle_degrees * -1
        Shared.hub().display.icon(Icon.ARROW_RIGHT)
        wheel_controller = WheelController.__object()
        await wheel_controller.turn(angle_degrees)

    # @staticmethod
    # async def follow_the_line(count: int, kp: float = 0.30):
    #     speed = Speed.Medium
    #     lm = speed
    #     rm = speed
    #     # at speed 250 the fastest is 0.30, but in the part of very curvy is 0.90
    #     # at speed 400 the fastest is 0.08
    #     local_kp = kp
    #     correction = round(speed * local_kp, 0)
    #     local_count = 0
    #
    #     while True:
    #         if local_count > count:
    #             WheelController.__left_motor.stop()
    #             WheelController.__right_motor.stop()
    #             break
    #
    #         color_int = await ColorController.get_mat_color()
    #         print("follow line color: ", color_int)
    #
    #         if color_int == MatColor.White:
    #             lm = speed
    #             rm = speed
    #         # Drifted left → steer right
    #         elif color_int == MatColor.Others:
    #             lm = speed + correction
    #             rm = speed - correction
    #         # Drifted right → steer left
    #         elif color_int == MatColor.Black:
    #             lm = speed - correction
    #             rm = speed + correction
    #
    #         print(f"lm {lm}, rm {rm}")
    #         WheelController.__left_motor.run(lm)
    #         WheelController.__right_motor.run(rm)
    #         local_count += 1
    #         await wait(10)

    @staticmethod
    def __object() -> DriveBase:
        return Shared.wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                       WheelController.__wheel_diameter_in_mm,
                                       WheelController.__axle_track_in_mm)
