import time
run = raw_input("Start? > ")
limit = 20
secs = 0
# Only run if the user types in "start"
if run == "y":
    # Loop until we reach 20 minutes running
    while limit:
        print ">>>>>>>>>>>>>>>>>>>>>", limit
        # Sleep for a minute
        time.sleep(1)
        # Increment the minute total
        limit -= 1
    # Bring up the dialog box here
