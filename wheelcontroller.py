from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from colorcontroller import ColorController
from shared import Shared, Speed


class WheelController:
    __wheel_diameter_in_mm = float(60)  # float(56)
    __axle_track_in_mm = float(162.5)  # float(163)  # float(160)  # float(145)

    __left_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE)
    __right_motor = Motor(Port.B)

    @staticmethod
    async def reset():
        await WheelController.__left_motor.run_target(Speed.Fast, 0)
        await WheelController.__right_motor.run_target(Speed.Fast, 0)

    @staticmethod
    async def move_forward(distance_in_mm: float, speed: float = Speed.Fast,
                           with_brake: bool = False):
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
            wheel_controller.reset()
            wheel_controller.drive(speed=speed, turn_rate=0)

            while True:
                if WheelController.__left_motor.stalled() or WheelController.__right_motor.stalled():
                    wheel_controller.stop()
                    break

                if wheel_controller.distance() >= distance_in_mm:
                    wheel_controller.stop()
                    break

            await wait(100)
            # await wheel_controller.straight(distance=distance_in_mm, then=Stop.BRAKE)
        else:
            await wheel_controller.straight(distance_in_mm)

    @staticmethod
    async def move_backward(distance_in_mm: float, speed: float = Speed.Fast,
                            with_brake: bool = False):
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
            # await wheel_controller.straight(distance=distance_in_mm, then=Stop.BRAKE)

            wheel_controller.reset()
            wheel_controller.drive(speed=-speed, turn_rate=0)

            while True:
                if WheelController.__left_motor.stalled() or WheelController.__right_motor.stalled():
                    wheel_controller.stop()
                    break

                if wheel_controller.distance() <= distance_in_mm:
                    wheel_controller.stop()
                    break

            await wait(100)
        else:
            await wheel_controller.straight(distance_in_mm)

    @staticmethod
    async def right_turn(angle_degrees: float = 90, turn_speed: float = 180):
        if angle_degrees < 0:
            angle_degrees = angle_degrees * -1

        wheel_controller = WheelController.__object(turn_speed=turn_speed)
        await wheel_controller.turn(angle_degrees)

    @staticmethod
    async def left_turn(angle_degrees: float = 90, turn_speed: float = 180):
        angle_degrees = angle_degrees * -1
        wheel_controller = WheelController.__object(turn_speed=turn_speed)
        await wheel_controller.turn(angle_degrees)

    @staticmethod
    async def move_towards_mat_color(mat_color_range: int, mat_color_range_alt: int = -1, speed: float = Speed.Slow,
                                     is_print: bool = False, is_hsv: bool = True, mat_color_range_alt_2: int = -1,
                                     mat_color_range_alt_3: int = -1):
        wheel_controller = WheelController.__object()
        count = 1

        while True:
            if is_hsv:
                color = await ColorController.mat_sensor.hsv()
            else:
                color = await ColorController.mat_sensor.color()

            color_int = color.h

            if ((mat_color_range - 2) <= color_int <= (mat_color_range + 2)) or count > 1000:
                if is_print:
                    print("mat color (DETECTED): ", color_int)
                    Shared.hub().speaker.beep(frequency=1000, duration=200)

                wheel_controller.stop()
                break
            elif mat_color_range_alt > -1 and (
                    (mat_color_range_alt - 2) <= color_int <= (mat_color_range_alt + 2)) or count > 1000:
                if is_print:
                    print("mat color (DETECTED): ", color_int)
                    Shared.hub().speaker.beep(frequency=1000, duration=200)

                wheel_controller.stop()
                break
            elif mat_color_range_alt_2 > -1 and (
                    (mat_color_range_alt_2 - 2) <= color_int <= (mat_color_range_alt_2 + 2)) or count > 1000:
                if is_print:
                    print("mat color (DETECTED): ", color_int)
                    Shared.hub().speaker.beep(frequency=1000, duration=200)

                wheel_controller.stop()
                break
            elif mat_color_range_alt_3 > -1 and (
                    (mat_color_range_alt_3 - 2) <= color_int <= (mat_color_range_alt_3 + 2)) or count > 1000:
                if is_print:
                    print("mat color (DETECTED): ", color_int)
                    Shared.hub().speaker.beep(frequency=1000, duration=200)

                wheel_controller.stop()
                break
            else:
                if is_print:
                    print("mat color: ", color_int)

                # you can be fast here otherwise bump the element, same as Medium Fast
                wheel_controller.drive(speed, 0)

            # print("moving: ", count)
            count = count + 1
            await wait(10)

        wheel_controller.stop()

    @staticmethod
    async def move_towards_mat_color_alt(mat_color_range: int, speed: float = Speed.Slow):
        wheel_controller = WheelController.__object()
        count = 1

        while True:
            color = await ColorController.mat_sensor.color()
            color_int = color.h
            print("mat color: ", color_int)

            if ((mat_color_range - 0) <= color_int <= (mat_color_range + 0)) or count > 1000:
                wheel_controller.stop()
                break
            else:
                # you can be fast here otherwise bump the element, same as Medium Fast
                wheel_controller.drive(speed, 0)

            # print("moving: ", count)
            count = count + 1
            await wait(10)

        wheel_controller.stop()

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
    def __object(turn_speed: float = 180) -> DriveBase:
        return Shared.wheels_with_gyro(WheelController.__left_motor, WheelController.__right_motor,
                                       WheelController.__wheel_diameter_in_mm,
                                       WheelController.__axle_track_in_mm, turn_speed)
