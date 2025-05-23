def loop():
    while True:
        try:
            while True:
                input(">>> ")
        except KeyboardInterrupt:
            print("Caught KeyboardInterrupt")
            # optionally: break to quit instead of restarting
loop()