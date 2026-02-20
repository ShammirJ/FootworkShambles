import random
import time

class TimerHit:
    """
    Docstring for TimerHit
    """
    # Attributes
    corners = [1, 2, 3 , 4, 5, 6]
    

    def __init__(self, duration=120, delayRange=(3.0, 3.0)):
        self.duration = duration
        self.delayRange = delayRange
        self.running = False

    def run(self):
        self.running = True
        startTime = time.time()

        while self.running and (time.time() - startTime < self.duration):

            # Random Delay
            delay = random.uniform(*self.delayRange)
            time.sleep(delay)

            if not self.running:
                break

            corner = random.choice(self.corners)
            print(f"Hit: {corner}")

    def stop(self):
        self.running = False