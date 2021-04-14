command = ""
started = False
while True :
         command = input(">").lower()
         if command == 'start':
             if started:
                 print ("Car is already started")
             else:
                 started = True
             print ("Car is started")
         elif command == 'stop':
          print ("car is stopped")
         elif command == 'help':
             print(""" 
start - start the car
stop - stop the car 
quit - to quit
             """)
         elif command == 'quit':
             break


         else:
             print ("Sorry i dont understand")


