from colorcontroller import ColorController, MatColor  # , # MatColor2
from handcontroller import HandController
from shared import Speed
from wheelcontroller import WheelController
from pybricks.tools import multitask, wait


class MissionRandomized:
    @staticmethod
    async def exec_mission():
        await multitask(WheelController.move_forward(450), HandController.lift_left(),
                        HandController.lift_right())
        await WheelController.left_turn()
        # First Banga
        await WheelController.move_backward(520, with_brake=True)
        await WheelController.move_forward(150, speed=Speed.Slow)
        await WheelController.right_turn()
        await WheelController.move_forward(482, speed=Speed.Medium)
        await wait(500)
        await ColorController.get_element_color()

        await WheelController.move_forward(125, speed=Speed.Medium)
        await wait(500)
        await ColorController.get_element_color()

        await multitask(WheelController.move_backward(120, speed=Speed.Medium), HandController.lift_left(),
                        HandController.lift_right())
        await WheelController.left_turn()
        await WheelController.move_forward(70)
        await multitask(WheelController.right_turn(180), HandController.lift_left(-10),
                        HandController.lift_right())
        await WheelController.move_forward(170, speed=80, with_brake=True)
        await WheelController.move_backward(10)
        await HandController.lift_left(10)
        await WheelController.move_backward(160, speed=Speed.Slow)
        await multitask(HandController.lift_right(-10), HandController.lift_left(80, speed=Speed.Slow))
        await WheelController.left_turn(2)
        await WheelController.move_forward(140, speed=80, with_brake=True)
        await WheelController.move_backward(10)
        await HandController.lift_right(10)
        await WheelController.move_backward(20, speed=Speed.Slow)
        await MissionRandomized.__slowly_turning()

        # 2nd bangga
        await WheelController.move_backward(370, speed=Speed.Medium, with_brake=True)
        await multitask(WheelController.move_forward(100), HandController.lift_right(-10),
                        HandController.lift_left(-10))
        await multitask(WheelController.move_forward(550), HandController.lift_left(10),
                        HandController.lift_right(5))
        await WheelController.move_towards_mat_color(MatColor.Maroon)
        await multitask(HandController.lift_left(10), HandController.lift_right(5),
                        WheelController.right_turn(180, turn_speed=90))
        await WheelController.move_backward(150, speed=Speed.Medium, with_brake=True)
        await WheelController.move_forward(130, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_backward(80, speed=Speed.Slow)
        await WheelController.move_towards_mat_color(MatColor.Black)

        # await MissionRandomized.__yellow_blue()
        # await MissionRandomized.__blue_yellow()
        #
        # await MissionRandomized.__green_red()
        # await MissionRandomized.__red_green()
        #
        # await MissionRandomized.__black_green()
        # await MissionRandomized.__green_black()
        #
        # await  MissionRandomized.__red_yellow()
        # await MissionRandomized.__yellow_red()
        #
        # await MissionRandomized.__black_yellow()
        # await MissionRandomized.__yellow_black()
        #
        # await MissionRandomized.__red_black()
        # await MissionRandomized.__black_red()

        # ToDo. to complete
        await MissionRandomized.__yellow_green()
        await MissionRandomized.__green_yellow()

        await MissionRandomized.__green_blue()
        await MissionRandomized.__blue_green()

        await MissionRandomized.__black_blue()
        await MissionRandomized.__blue_black()

        await MissionRandomized.__blue_red()
        await MissionRandomized.__red_blue()

        await wait(500)

    @staticmethod
    async def __yellow_blue():
        await multitask(HandController.lift_left(15), HandController.lift_right(10))
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_backward(150, with_brake=True)
        await WheelController.move_forward(135, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_forward(160, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=60)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_backward(100)
        await WheelController.left_turn()
        await WheelController.move_forward(770)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)

    @staticmethod
    async def __blue_yellow():
        await multitask(HandController.lift_left(15), HandController.lift_right(10))
        await WheelController.move_backward(30)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_backward(10)
        await HandController.lift_right(-10)
        await WheelController.move_backward(300)
        await WheelController.right_turn()
        await WheelController.move_forward(285)
        await WheelController.left_turn()
        await WheelController.move_forward(335, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(35)
        await HandController.lift_left(-10)
        await WheelController.move_backward(100)
        await WheelController.left_turn()
        await WheelController.move_forward(900)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo, Speed.Slow)

    @staticmethod
    async def __green_red():
        await multitask(HandController.lift_left(15), HandController.lift_right(10))
        await WheelController.move_forward(215)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(100, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(35)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_backward(100)
        await WheelController.left_turn()
        await WheelController.move_forward(500)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo, Speed.Slow)

    @staticmethod
    async def __red_green():
        await multitask(HandController.lift_left(15), HandController.lift_right(10))
        await WheelController.move_forward(350)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(100, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(35)
        await HandController.lift_right(-10)
        await WheelController.move_backward(125)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(285)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_forward(200, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(35)
        await HandController.lift_left(-10)
        await WheelController.move_backward(100)
        await WheelController.left_turn()
        await WheelController.move_forward(600)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo, Speed.Slow)

    @staticmethod
    async def __black_green():
        await multitask(HandController.lift_left(15), HandController.lift_right(10))

        await WheelController.move_forward(90)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(100, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(35)
        await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        await WheelController.move_backward(100)
        await WheelController.left_turn()
        await WheelController.move_forward(500)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo, Speed.Slow)

    @staticmethod
    async def __green_black():
        await multitask(HandController.lift_left(15), HandController.lift_right(10))

        await WheelController.move_forward(215)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(100, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(35)
        await HandController.lift_right(-10)
        await WheelController.move_backward(125)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(275)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_forward(200, speed=Speed.Medium, with_brake=True)
        await WheelController.move_backward(40)
        await HandController.lift_left(-10)
        await WheelController.move_backward(100)
        await WheelController.left_turn()
        await WheelController.move_forward(700)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo, Speed.Slow)

    @staticmethod
    async def __red_yellow():
        await multitask(HandController.lift_left(15), HandController.lift_right(5))
        await WheelController.move_forward(230, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(50, speed=Speed.Medium)
        await WheelController.move_backward(45)
        await HandController.lift_left(-10)
        await WheelController.move_backward(130, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)
        await WheelController.move_forward(220, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_forward(325, speed=Speed.Medium)
        await WheelController.move_backward(40, speed=Speed.Slow)
        await HandController.lift_right(-10)
        await WheelController.move_backward(130, speed=Speed.Medium)
        await WheelController.left_turn()
        await WheelController.move_forward(770)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo, Speed.Slow)
        # await multitask(HandController.lift_left(-10), HandController.lift_right(-10))
        # await WheelController.move_backward(100)
        # await WheelController.left_turn()
        # await WheelController.move_forward(770)
        # await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)

    @staticmethod
    async def __yellow_red():
        await multitask(HandController.lift_left(15), HandController.lift_right(5))
        await WheelController.move_forward(355, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(50, speed=Speed.Medium)
        await HandController.lift_right(0)
        await WheelController.move_backward(45)
        # Placing red relic
        await HandController.lift_right(-10)
        await WheelController.move_backward(130, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(250, speed=Speed.Medium)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)
        await WheelController.move_forward(375, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_forward(185, speed=Speed.Medium)
        await WheelController.move_backward(25)
        await HandController.lift_left(0)
        await WheelController.move_backward(105)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_forward(850)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)

    @staticmethod
    async def __black_yellow():
        await multitask(HandController.lift_left(15), HandController.lift_right(5))
        await WheelController.move_backward(50, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await HandController.lift_left(-10)
        await WheelController.move_backward(100, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_backward(130, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(140, speed=Speed.Medium)
        await WheelController.move_backward(50, speed=Speed.Medium)
        await HandController.lift_right(-10)
        await WheelController.move_backward(130)
        await WheelController.left_turn()
        await WheelController.move_forward(770)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo, Speed.Slow)

    @staticmethod
    async def __yellow_black():
        await multitask(HandController.lift_left(15), HandController.lift_right(5))
        await WheelController.move_forward(75, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_backward(15, speed=Speed.Medium)
        await HandController.lift_right(-10)
        await WheelController.move_backward(100, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_backward(390, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(140, speed=Speed.Medium)
        await WheelController.move_backward(30, speed=Speed.Medium)
        await HandController.lift_left(-10)
        await WheelController.move_backward(130)
        await WheelController.left_turn()
        await WheelController.move_forward(770)
        await WheelController.move_towards_mat_color(MatColor.BlackTwo, Speed.Slow)

    @staticmethod
    async def __red_black():
        await multitask(HandController.lift_left(20), HandController.lift_right(5))
        await WheelController.move_backward(50, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_backward(5, speed=Speed.Medium)
        await HandController.lift_left(-10)
        await WheelController.move_backward(100, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_forward(395, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(150, speed=Speed.Medium)
        await WheelController.move_backward(45, speed=Speed.Medium)
        await HandController.lift_right(-10)
        await WheelController.move_backward(100, speed=Speed.Medium)
        await WheelController.left_turn()
        await WheelController.move_forward(265)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)

    @staticmethod
    async def __black_red():
        await multitask(HandController.lift_left(15), HandController.lift_right(5))
        await WheelController.move_forward(80, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_backward(15, speed=Speed.Medium)
        await HandController.lift_right(-10)
        await WheelController.move_backward(100, speed=Speed.Medium)
        await WheelController.left_turn(turn_speed=60)
        await WheelController.move_forward(115, speed=Speed.Medium)
        await WheelController.right_turn(turn_speed=60)
        await WheelController.move_forward(165, speed=Speed.Medium)
        await WheelController.move_backward(40, speed=Speed.Medium)
        await HandController.lift_left(-10)
        await WheelController.move_backward(120, speed=Speed.Medium)
        await WheelController.left_turn()
        await WheelController.move_forward(440, speed=Speed.Medium)
        await WheelController.move_towards_mat_color(MatColor.Black, Speed.Slow)

    @staticmethod
    async def __yellow_green():
        pass

    @staticmethod
    async def __green_yellow():
        pass

    @staticmethod
    async def __green_blue():
        pass

    @staticmethod
    async def __blue_green():
        pass

    @staticmethod
    async def __black_blue():
        pass

    @staticmethod
    async def __blue_black():
        pass

    @staticmethod
    async def __blue_red():
        pass

    @staticmethod
    async def __red_blue():
        pass

    @staticmethod
    async def __slowly_turning():
        await multitask(HandController.lift_right(10, speed=Speed.Slow),
                        HandController.lift_left(10, speed=Speed.Slow))
        await WheelController.right_turn(5, turn_speed=50)
        await WheelController.move_backward(10)
        await WheelController.right_turn(175, turn_speed=90)
