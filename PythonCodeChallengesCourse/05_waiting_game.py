import time
import random

def waiting_game():
    val = ""

    while val != "q":
        print("Press Q then <enter> to quit...")
        
        #generate random number between 2 and 4 inclusively
        wait_time = random.randint(2,4)

        print("Your target time is {} seconds".format(wait_time))
        val = input(" ---Press Enter to Begin--- ")
        
        if val == "q": return

        start = time.perf_counter()

        val = input("\n...Press Enter again after {} seconds...".format(wait_time))
        elapsed = time.perf_counter() - start

        print("\nElapsed time: {0:.3f} seconds".format(elapsed))

        if elapsed == wait_time:
            print("Unbelievable! Perfect timing!")
        elif elapsed < wait_time:
            print("{0:.3f} seconds too fast".format(wait_time-elapsed))
        else:
            print("{0:.3f} seconds too slow".format(wait_time-elapsed))

if __name__ == "__main__":
    waiting_game()