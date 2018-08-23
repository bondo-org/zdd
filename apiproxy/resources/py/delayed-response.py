from time import sleep

delay = flow.getVariable("request.queryparam.delay")

delay = 2 if not delay else float(delay)

sleep(delay)