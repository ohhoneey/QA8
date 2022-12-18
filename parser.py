import subprocess

def parser(arg):
    arg = str(arg)
    text = arg.split('[ 1]')
    mass = []

    for i in range(2,12):
        temp = text[i].split()
        mass.append([temp[0], temp[2], temp[4]])

    for j in range(len(mass)):
        if float(mass[j][1]) > 350 and float(mass[j][2] )> 3:
            print('Interval: ', mass[j][0], 'Transfer: ', mass[j][1], 'Brandwidth: ', mass[j][2])

    return mass
