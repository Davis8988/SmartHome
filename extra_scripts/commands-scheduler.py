
from datetime import  datetime
import time, threading

scheduled_id = 0
scheduled_commands = []


class ScheduledCommand:
    def __init__(self, device_name, command_name, when):
        global scheduled_id
        self.device_name = device_name
        self.command_name = command_name
        self.when = datetime.strptime(when, '%d-%m-%Y %H:%M:%S')
        self.id = scheduled_id
        scheduled_id += 1







class CommandsScheduler:
    def __init__(self):
        self.scheduled_commands = {}

    def add_scheduled_command(self, scheduled_command):
        self.scheduled_commands[scheduled_command.id] = scheduled_command
        wait_seconds = (scheduled_command.when - datetime.now()).total_seconds()
        threading.Timer(wait_seconds, self.scheduled_time_excution, [scheduled_command.id]).start()


    def scheduled_time_excution(self,schduled_id):
        try:
            sch_command = self.scheduled_commands[schduled_id]
            print("Excuting {}:{}".format(sch_command.device_name, sch_command.command_name))
            self.scheduled_commands.pop(schduled_id)
            print("Total scheduled commands after: {}".format(len(self.scheduled_commands)))
        except:
            pass


    def cancell_scheduled_command(self,scheduled_id):
        self.scheduled_commands.pop(scheduled_id)



# Main

scheduler = CommandsScheduler()
sch1 = ScheduledCommand("kitchenLight", "off", "11-10-2019 19:13:40")
sch2 = ScheduledCommand("saloonLight", "off", "11-10-2019 19:13:50")
scheduler.add_scheduled_command(sch1)
scheduler.add_scheduled_command(sch2)

scheduler.cancell_scheduled_command(0)


while True:
    time.sleep(1)
