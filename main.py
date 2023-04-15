import batchbangun
import batchkumpul
import jinbangun
import jinkumpul

Exit = False
while not Exit:
    inp = input(">>> ")
    if inp == 'batchbangun':
        batchbangun.run()
    elif inp == 'batchkumpul':
        batchkumpul.run()
    elif inp == 'jinbangun':
        jinbangun.run()
    elif inp == 'jinkumpul':
        jinkumpul.run()
    elif inp == 'exit':
        Exit = True