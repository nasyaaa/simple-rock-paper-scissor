print "Welcome to play Rock , Paper , Scissors game . Enter -1 to end."	
print "You can only type 'rock' , 'paper' and 'scissor' "						
							
rounds = 0							
scorep1 = 0							
scorep2 = 0

p1 = raw_input (" >> Player 1 ? ") .lower()        
p2 = raw_input (" >> Player 2 ? ") .lower()
		
while (p1 != '-1' and p2 != '-1'):
        
		if (p1 == 'rock'  and p2=='rock') or (p1=='paper' and p2 == 'paper') or (p1=='scissor' and p2 == 'scissor') :
			scorep1 += 0					
			scorep2 += 0					
			print ("\nIt's a tie")
		elif(p1 == 'rock' and p2 == 'scissor') or ( p1 == 'paper' and p2 == 'rock') or (p1 == 'scissor' and p2 == 'paper'):
			scorep1 += 1					
			scorep2 += 0					
			print ("\nPlayer 1 win")		
		elif(p1 == 'rock' and p2 == 'paper') or (p1 == 'paper' and p2 == 'scissor') or (p1 == 'scissor' and p2 == 'rock'): 
			scorep1 += 0					
			scorep2 += 1					
			print ("\nPlayer 2 win")
		else:
			print "One of your choice is invalid.Try again" 
		
                
		rounds += 1
		print "============================\n Score :"	
		print "Player 1 :" , scorep1							
		print "Player 2 :" , scorep2
		print "Total game played : " , rounds 

		p1 = raw_input (" >> Player 1 ? ") .lower()

		if p1 == '-1':
				break
		
		p2 = raw_input (" >> Player 2 ? ") .lower()

		if p2 == '-1':
				break

print '\nEnd of game !'
print "Total game played : " ,rounds		
print "============================\nScore :"
print "Player 1 :" , scorep1 
print "Player 2 :" , scorep2
							
print "\n***********************************"
if (scorep1 > scorep2):
	print ("Winner : Player 1")
		
if (scorep2 > scorep1):
	print ("Winner : Player 2")
	
if (scorep1 == scorep2):
	print ("Both player have same mark.It's tie!")
print "***********************************"	
 
 
