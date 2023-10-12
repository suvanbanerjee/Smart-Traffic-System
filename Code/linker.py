import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
it = pyfirmata.util.Iterator(board)
it.start()
signal_1_red = board.get_pin('d:2:o')
signal_1_yellow = board.get_pin('d:3:o')
signal_1_green = board.get_pin('d:4:o')
signal_2_red = board.get_pin('d:5:o')
signal_2_yellow = board.get_pin('d:6:o')
signal_2_green = board.get_pin('d:7:o')
signal_3_red = board.get_pin('d:8:o')
signal_3_yellow = board.get_pin('d:9:o')
signal_3_green = board.get_pin('d:10:o')
signal_4_red = board.get_pin('d:11:o')
signal_4_yellow = board.get_pin('d:12:o')
signal_4_green = board.get_pin('d:13:o')
def Signal_1_red_on():
    signal_1_red.write(1)
def Signal_1_red_off():
    signal_1_red.write(0)
def Signal_1_yellow_on():
    signal_1_yellow.write(1)
def Signal_1_yellow_off():
    signal_1_yellow.write(0)
def Signal_1_green_on():
    signal_1_green.write(1)
def Signal_1_green_off():
    signal_1_green.write(0)
def Signal_2_red_on():
    signal_2_red.write(1)
def Signal_2_red_off():
    signal_2_red.write(0)
def Signal_2_yellow_on():
    signal_2_yellow.write(1)
def Signal_2_yellow_off():
    signal_2_yellow.write(0)
def Signal_2_green_on():
    signal_2_green.write(1)
def Signal_2_green_off():
    signal_2_green.write(0)
def Signal_3_red_on():
    signal_3_red.write(1)
def Signal_3_red_off():
    signal_3_red.write(0)
def Signal_3_yellow_on():
    signal_3_yellow.write(1)
def Signal_3_yellow_off():
    signal_3_yellow.write(0)
def Signal_3_green_on():
    signal_3_green.write(1)
def Signal_3_green_off():
    signal_3_green.write(0)
def Signal_4_red_on():
    signal_4_red.write(1)
def Signal_4_red_off():
    signal_4_red.write(0)
def Signal_4_yellow_on():
    signal_4_yellow.write(1)
def Signal_4_yellow_off():
    signal_4_yellow.write(0)
def Signal_4_green_on():
    signal_4_green.write(1)
def Signal_4_green_off():
    signal_4_green.write(0)

def All_off():
    Signal_1_red_off()
    Signal_1_yellow_off()
    Signal_1_green_off()
    Signal_2_red_off()
    Signal_2_yellow_off()
    Signal_2_green_off()
    Signal_3_red_off()
    Signal_3_yellow_off()
    Signal_3_green_off()
    Signal_4_red_off()
    Signal_4_yellow_off()
    Signal_4_green_off()