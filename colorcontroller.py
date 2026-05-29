from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port


class MatColor:
    White = 0
    Black = 1
    Others = -1


class ElementColor:
    Blue = 0
    Yellow = 1
    Red = 2
    Green = 3
    Black = 4


class ColorController:
    mat_sensor = ColorSensor(Port.C)
    __side_sensor = ColorSensor(Port.D)

    @staticmethod
    async def get_mat_color() -> int:
        color = await ColorController.mat_sensor.hsv()
        color_int = color.h
        print("mat color: ", color_int)

        # when it detects white then 0, which is center
        if 223 <= color_int <= 224:
            return MatColor.White

        # when it detects black return 1, swerving to the right
        if 209 <= color_int <= 221:
            return MatColor.Black

        # when detects other color return -1, swerving to the left
        if color_int <= 204:
            return MatColor.Others

        # when it detects outside the above, just treat it as White so wheels move straight
        return MatColor.White

    @staticmethod
    async def get_element_color() -> int:
        color = await ColorController.__side_sensor.hsv()
        color_int = color.h
        print("side color: ", color_int)

        # when it detects blue
        if 218 <= color_int <= 220:
            return ElementColor.Blue

        # when it detects yellow
        if 40 <= color_int <= 41:
            return ElementColor.Yellow

        # when detects red
        if 348 <= color_int <= 356:
            return ElementColor.Red

        # when detects green
        if 150 <= color_int <= 157:
            return ElementColor.Green

        # when it detects outside the above or 240, just treat it as Black
        if color_int == 240:
            return MatColor.Black

        return ElementColor.Black
