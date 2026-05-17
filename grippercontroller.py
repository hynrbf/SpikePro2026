from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop

from shared import Speed


class GripperController:
    __front_motor = Motor(Port.E)
    __back_motor = Motor(Port.F)

    # 88 to 90
    __grip_turn_angle = 200

    @staticmethod
    async def reset():
        await GripperController.__back_motor.run_target(Speed.Fast, 0, Stop.COAST)

    @staticmethod
    async def lift():
        await GripperController.__back_motor.run_target(Speed.Slow, 60, Stop.HOLD)

    @staticmethod
    async def down():
        await GripperController.reset()

    @staticmethod
    async def close():
        pass

    @staticmethod
    async def opening():
        pass

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
    def __get_right_arm_angle() -> int:
        current_angle = GripperController.__front_motor.angle()
        print("right arm current angle", current_angle)
        return current_angle

    @staticmethod
    def __get_left_arm_angle() -> int:
        current_angle = GripperController.__back_motor.angle()
        print("left arm current angle", current_angle)
        return current_angle
