from timerHit import TimerHit

def main():
    timer = TimerHit(duration=30, delayRange = (1.0, 2.0))
    
    timer.run()

if __name__=="__main__":
    main()
