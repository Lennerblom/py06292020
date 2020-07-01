#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
#import worktodo.txt
#worktodo = open("worktodo.txt", "r")
import yaml
# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('\nHandshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

# function that prints the IPs
def devicereboot(ipList):
    for ip in ipList:
        print("Connecting to.." + ip)
        print("REBOOTING NOW!")

# start our main script
def main():
    with open("worktodo.yml", "r") as df:
        work2do = yaml.load(df,Loader=yaml.FullLoader)
   # work2do = worktodo
   # work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1": 
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices
    devicereboot(work2do.keys())
# call our main function
main()

