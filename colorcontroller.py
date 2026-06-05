from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port


class MatColor:
    White = 213
    Green = 114
    Maroon = 349
    Black = 240
    BlackTwo = 220  # 210 #216
    Red = 349
    Others = -1


class MatColorAlt:
    White = 0
    Black = 240


class ElementColor:
    Blue = "Blue"
    Yellow = "Yellow"
    Red = "Red"
    Green = "Green"
    Black = "Black"


class ColorController:
    mat_sensor = ColorSensor(Port.C)
    __side_sensor = ColorSensor(Port.D)

    @staticmethod
    async def get_element_color(is_hsv: bool = True) -> str:
        if is_hsv:
            return await ColorController.__get_element_color_hsv()

        return await ColorController.__get_element_color_non_hsv()

    @staticmethod
    async def print_mat_color():
        color = await ColorController.mat_sensor.hsv()
        color_int = color.h
        print("mat color: ", color_int)

    @staticmethod
    async def __get_element_color_hsv() -> str:
        color = await ColorController.__side_sensor.hsv()
        color_int = color.h
        print("side color hsv: ", color_int)

        # when it detects blue
        if 216 <= color_int <= 220:
            return ElementColor.Blue

        # when it detects yellow
        if 38 <= color_int <= 42:
            return ElementColor.Yellow

        # when detects red
        if 348 <= color_int <= 356:
            return ElementColor.Red

        # when detects green
        if 150 <= color_int <= 157:
            return ElementColor.Green

        # when it detects outside the above or 240, just treat it as Black
        if color_int == 240:
            return ElementColor.Black

        return ElementColor.Black

    @staticmethod
    async def __get_element_color_non_hsv() -> str:
        color = await ColorController.__side_sensor.color()
        color_int = color.h
        print("side color: ", color_int)

        # when it detects blue
        if 216 <= color_int <= 220:
            return ElementColor.Blue

        # when it detects yellow
        if 40 <= color_int <= 42:
            return ElementColor.Yellow

        # when detects red
        if 348 <= color_int <= 356:
            return ElementColor.Red

        # when detects green
        if 150 <= color_int <= 157:
            return ElementColor.Green

        # when it detects outside the above or 240, just treat it as Black
        if color_int == 240:
            return ElementColor.Black

        return ElementColor.Black
