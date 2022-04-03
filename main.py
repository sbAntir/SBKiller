import toKill

sb = input("Enter a name who you want to kill: ")
status = bool(input("Are you sure that you want to kill? Enter anything for true or do not enter anything for false: "))
if sb:
    if status == True:
        print(toKill.killSb(sb, True))
