/**
EkoDataPull_master.py
*/


#this file centralizes the current version of the ekotrope pull script that we want to run on our remote computer (our virual machine) on a set schedule
#this makes it so we don't have to edit the reference directory on the virtual machine, we can just update this file to do what we want!

import logging
import EkoDataPull_2_9 as eko


#loop through data range to get most recent tropes

i = -1 #date you want to start at, 0 would mean start with today/now!
interval = 2 #size of loop, 5 would mean loop in 5 day increments
while i < 10: #how far back you want to look in ekotrope, 15 would mean look back 15 days and then stop
    try:   
        eko.main(i, interval)
        with open("eko_log.csv", "a") as log:
            log.write("success" +','+ str(i) +'\n')
    except Exception as e: 
        with open("eko_log.csv", "a") as log:
                log.write(str(e) +','+ str(i) +'\n')
                log.write(logging.Formatter('[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(funcName)s %(levelname)s - %(message)s','%m-%d %H:%M:%S')+'\n')
                print('Error: ' + str(e))
                
    i += interval
