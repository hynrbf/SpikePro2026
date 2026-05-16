from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop

from shared import Speed


class GripperController:
    __front_motor = Motor(Port.E)
    __back_motor = Motor(Port.F)

    # 88 to 90
    __grip_turn_angle = 200

    @staticmethod
    async def close():
        cur_val = GripperController.__grip_turn_angle + 30
        await GripperController.__front_motor.run_target(Speed.Slow, cur_val, Stop.COAST)

    @staticmethod
    async def opening():
        cur_val = GripperController.__grip_turn_angle - 30
        await GripperController.__front_motor.run_target(Speed.Slow, cur_val, Stop.COAST)

    @staticmethod
    async def reset():
        cur_val = GripperController.__grip_turn_angle * -1
        print(cur_val)
        GripperController.__grip_turn_angle = cur_val
        await GripperController.__front_motor.run_target(Speed.Slow, cur_val, Stop.COAST)

    @staticmethod
    async def up():
        await GripperController.__back_motor.run_angle(Speed.Medium, 200, Stop.COAST)

    @staticmethod
    async def down():
        await GripperController.__back_motor.run_target(Speed.Slow, -600, Stop.COAST)

    # @staticmethod
    # async def reset():
    #     await multitask(GripperController.__front_motor.run_target(Speed.Fast, 180, Stop.COAST),
    #                     GripperController.__back_motor.run_target(Speed.Fast, 0, Stop.COAST)
    #                     )
    #
    # @staticmethod
    # async def un_reset():
    #     await multitask(GripperController.__front_motor.run_target(Speed.Fast, 0, Stop.COAST),
    #                     GripperController.__back_motor.run_target(Speed.Fast, -45, Stop.COAST)
    #                     )

    @staticmethod
    async def front_hook(angle_degrees: float = 110, speed: int = Speed.Medium):
        await GripperController.__front_motor.run_target(speed, angle_degrees, Stop.HOLD)

    @staticmethod
    async def front_hook_down(angle_degrees: float = 0, speed: int = Speed.Slow):
        await GripperController.__front_motor.run_target(speed, angle_degrees, Stop.HOLD)

    @staticmethod
    async def back_grip():
        await GripperController.__back_motor.run_target(Speed.Fast, 0, Stop.BRAKE)

    @staticmethod
    async def back_grip_up(angle_degrees: float = 90):
        angle_degrees = angle_degrees * -1
        await GripperController.__back_motor.run_target(Speed.Fast, angle_degrees, Stop.COAST)

    @staticmethod
    def __get_right_arm_angle() -> int:
        current_angle = GripperController.__front_motor.angle()
        print("right arm current angle", current_angle)
        return current_angle

    @staticmethod
    def __get_left_arm_angle() -> int:
        current_angle = GripperController.__back_motor.angle()
        print("left arm current angle", current_angle)
        return current_angle
