import linker
import time



def logic(signal_1_density, signal_2_density, signal_3_density, signal_4_density):
    signal_1_density=int(signal_1_density)
    signal_2_density=int(signal_2_density)
    signal_3_density=int(signal_3_density)
    signal_4_density=int(signal_4_density)

    if ((signal_1_density or signal_3_density) > 20) and ((signal_2_density or signal_4_density) == 0 ):
        linker.All_off()
        linker.Signal_1_yellow_on()
        linker.Signal_2_yellow_on()
        linker.Signal_3_yellow_on()
        linker.Signal_4_yellow_on()
        time.sleep(3)
        linker.Signal_1_yellow_off()
        linker.Signal_2_yellow_off()
        linker.Signal_3_yellow_off()
        linker.Signal_4_yellow_off()

        linker.Signal_1_green_on()
        linker.Signal_2_red_on()
        linker.Signal_3_green_on()
        linker.Signal_4_red_on()

    elif ((signal_2_density or signal_4_density) > 20) and ((signal_1_density or signal_3_density) == 0 ):
        
        linker.All_off()
        linker.Signal_1_yellow_on()
        linker.Signal_2_yellow_on()
        linker.Signal_3_yellow_on()
        linker.Signal_4_yellow_on()
        time.sleep(3)
        linker.Signal_1_yellow_off()
        linker.Signal_2_yellow_off()
        linker.Signal_3_yellow_off()
        linker.Signal_4_yellow_off()

        linker.Signal_1_red_on()
        linker.Signal_2_green_on()
        linker.Signal_3_red_on()
        linker.Signal_4_green_on()


    elif ((signal_2_density or signal_4_density) < 2) and ((signal_1_density or signal_3_density) < 2 ):
        
        if (signal_2_density or signal_4_density) > (signal_1_density or signal_3_density):
            
            linker.All_off()

            linker.Signal_1_yellow_on()
            linker.Signal_2_yellow_on()
            linker.Signal_3_yellow_on()
            linker.Signal_4_yellow_on()
            time.sleep(3)
            linker.Signal_1_yellow_off()
            linker.Signal_2_yellow_off()
            linker.Signal_3_yellow_off()
            linker.Signal_4_yellow_off()

            linker.Signal_2_green_on()
            linker.Signal_4_green_on()
            linker.Signal_1_red_on()
            linker.Signal_3_red_on()

        else:
            
            linker.All_off()
            linker.Signal_1_yellow_on()
            linker.Signal_2_yellow_on()
            linker.Signal_3_yellow_on()
            linker.Signal_4_yellow_on()
            time.sleep(3)
            linker.Signal_1_yellow_off()
            linker.Signal_2_yellow_off()
            linker.Signal_3_yellow_off()
            linker.Signal_4_yellow_off()

            linker.Signal_1_green_on()
            linker.Signal_3_green_on()
            linker.Signal_2_red_on()
            linker.Signal_4_red_on()

    else:
        signal_duration = 10
        linker.All_off()

        linker.Signal_1_yellow_on()
        linker.Signal_2_yellow_on()
        linker.Signal_3_yellow_on()
        linker.Signal_4_yellow_on()
        time.sleep(3)
        linker.Signal_1_yellow_off()
        linker.Signal_2_yellow_off()
        linker.Signal_3_yellow_off()
        linker.Signal_4_yellow_off()


        linker.Signal_1_green_on()
        linker.Signal_2_red_on()
        linker.Signal_3_red_on()
        linker.Signal_4_red_on()
        time.sleep(signal_duration)

        linker.All_off()
        linker.Signal_1_yellow_on()
        linker.Signal_2_yellow_on()
        linker.Signal_3_yellow_on()
        linker.Signal_4_yellow_on()
        time.sleep(3)
        linker.Signal_1_yellow_off()
        linker.Signal_2_yellow_off()
        linker.Signal_3_yellow_off()
        linker.Signal_4_yellow_off()

        linker.Signal_2_green_on()
        linker.Signal_1_red_on()
        linker.Signal_3_red_on()
        linker.Signal_4_red_on()
        time.sleep(signal_duration)

        linker.All_off()
        linker.Signal_1_yellow_on()
        linker.Signal_2_yellow_on()
        linker.Signal_3_yellow_on()
        linker.Signal_4_yellow_on()
        time.sleep(3)
        linker.Signal_1_yellow_off()
        linker.Signal_2_yellow_off()
        linker.Signal_3_yellow_off()
        linker.Signal_4_yellow_off()

        linker.Signal_3_green_on()
        linker.Signal_1_red_on()
        linker.Signal_2_red_on()
        linker.Signal_4_red_on()
        time.sleep(signal_duration)

        linker.All_off()
        linker.Signal_1_yellow_on()
        linker.Signal_2_yellow_on()
        linker.Signal_3_yellow_on()
        linker.Signal_4_yellow_on()
        time.sleep(3)
        linker.Signal_1_yellow_off()
        linker.Signal_2_yellow_off()
        linker.Signal_3_yellow_off()
        linker.Signal_4_yellow_off()

        linker.Signal_4_green_on()
        linker.Signal_1_red_on()
        linker.Signal_2_red_on()
        linker.Signal_3_red_on()
        time.sleep(signal_duration)