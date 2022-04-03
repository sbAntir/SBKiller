def killSb(sb, status = True):
    if sb:
        if status == True:
            toPrint = "Killed " + sb
            while status:
                return toPrint
                status = False
    else:
        toPrint = "Name is invalid"
        return toPrint
