# from pybricks.pupdevices import ColorSensor
# from pybricks.parameters import Port
# from pybricks.tools import wait
#
# from shared import Shared
#
#
# class ColorController:
#     #__front_sensor = ColorSensor(Port.D)
#     __mat_sensor = ColorSensor(Port.C)
#
#     @staticmethod
#     async def get_color(is_white_default: bool = True) -> str:
#         if await ColorController.__detect_green_element():
#             return "Green"
#
#         if await ColorController.__detect_yellow_element():
#             return "Yellow"
#
#         if await ColorController.__detect_red_element():
#             return "Red"
#
#         if await ColorController.__detect_white_or_blue_element():
#             if is_white_default:
#                 return "White"
#             else:
#                 return "Blue"
#
#         color = await ColorController.__front_sensor.hsv()
#         color_int = color.h
#         print("None: ", color_int)
#         return ""
#
#     @staticmethod
#     async def detect_white_floor_color() -> bool:
#         color = await ColorController.__mat_sensor.hsv()
#         color_int = color.h
#         print("Floor detected: ", color_int)
#
#         # 222-225 or 231 or 232?
#         if 231 <= color_int <= 232:
#             return True
#
#         return False
#
#     @staticmethod
#     async def detect_non_white_floor_color() -> bool:
#         color = await ColorController.__mat_sensor.hsv()
#         color_int = color.h
#
#         if color_int < 230:
#             return True
#
#         return False
#
#     @staticmethod
#     async def print_color_int(use_mat: bool = False):
#         count = 1
#
#         while True:
#             if count > 1000:
#                 break
#
#             if use_mat:
#                 color = await ColorController.__mat_sensor.hsv()
#                 color_int = color.h
#                 print("Floor color detected: ", color_int)
#             else:
#                 color = await ColorController.__front_sensor.hsv()
#                 color_int = color.h
#                 print("Color detected: ", color_int)
#
#                 ambient = await ColorController.__front_sensor.ambient()
#                 print("Ambient detected: ", ambient)
#
#             count = count + 1
#             await wait(10)
#
#     @staticmethod
#     async def __detect_yellow_element() -> bool:
#         count = 1
#         is_detected = False
#
#         while True:
#             if count > 3:
#                 is_detected = False
#                 break
#
#             color = await ColorController.__front_sensor.hsv()
#             color_int = color.h
#             print("Color detected: ", color_int)
#
#             if 40 <= color_int <= 65:
#                 Shared.hub().display.char("R")
#                 is_detected = True
#                 break
#
#             count = count + 1
#             await wait(10)
#
#         return is_detected
#
#     @staticmethod
#     async def __detect_red_element() -> bool:
#         count = 1
#         is_detected = False
#
#         while True:
#             if count > 3:
#                 is_detected = False
#                 break
#
#             color = await ColorController.__front_sensor.hsv()
#             color_int = color.h
#             # print("Color detected: ", color_int)
#
#             if 340 <= color_int <= 360:
#                 Shared.hub().display.char("R")
#                 is_detected = True
#                 break
#
#             count = count + 1
#             await wait(10)
#
#         return is_detected
#
#     @staticmethod
#     async def __detect_green_element() -> bool:
#         count = 1
#         is_detected = False
#
#         while True:
#             if count > 3:
#                 is_detected = False
#                 break
#
#             color = await ColorController.__front_sensor.hsv()
#             color_int = color.h
#             # print("Color detected: ", color_int)
#
#             # tested and found out green always at Color(h=156, s=78, v=64), so we be safe at 100 - 165
#             if 110 <= color_int <= 165:
#                 Shared.hub().display.char("G")
#                 is_detected = True
#                 break
#
#             count = count + 1
#             await wait(10)
#
#         return is_detected
#
#     @staticmethod
#     async def __detect_white_or_blue_element() -> bool:
#         count = 1
#         is_detected = False
#
#         while True:
#             if count > 3:
#                 is_detected = False
#                 break
#
#             color = await ColorController.__front_sensor.hsv()
#             color_int = color.h
#             # print("White int: ", color_int)
#
#             if 173 <= color_int <= 241:
#                 Shared.hub().display.char("W")
#                 is_detected = True
#                 print("White int: ", color_int)
#                 break
#
#             count = count + 1
#             await wait(10)
#
#         return is_detected
