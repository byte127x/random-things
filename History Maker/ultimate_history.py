import random as rm

print("Welcome To The Domination Controller\nThis program makes radical algorithms to decide which country should fade from existence!\n")
countries = ['Austria', "Belgium", 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'The Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Andorra', 'Armenia', 'Belarus', 'Bosnia and Herzegovina', 'Faroe Isands', 'Georgia', 'Gibraltar', 'Iceland', 'Isle of Man', 'Liechtenstein', 'Macedonia', 'Moldova', 'Monaco', 'Montenegro', 'Norway', 'Russia', 'San Marino', 'Serbia', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom']

input('Press Enter to Start!')
fIO = open('Data.txt', 'a')

while True:
    revolt_time = (rm.randint(0, 8) == 6)
    victim_state = rm.randint(0, len(countries)-1)
    swallow_by_neighbor_time = (rm.randint(0, 10) == 9)
    print('')

    if len(countries) == 1:
        print(f'{countries[0]} Won The Supreme Battle!')
        fIO.write(f'{countries[0]} Won The Supreme Battle!')
        break
    elif revolt_time:
        fIO.write("REVOLUTION TIME FOR ...")
        print("REVOLUTION TIME FOR ...")
        fIO.write(countries[victim_state] + '\n')
        print(countries[victim_state] + '\n')
    elif swallow_by_neighbor_time:
        print(f"{countries[victim_state]} Turns its neighbors into puppets!\nThey still exist but are dominated by their puppetmaster\n")
        fIO.write(f"{countries[victim_state]} Turns its neighbors into puppets!\nThey still exist but are dominated by their puppetmaster\n")
    else:
        fIO.write('Battle Time - Who Will Win???')
        print('Battle Time - Who Will Win???')
        countrybattle = rm.randint(0, len(countries)-1)
        if countrybattle == victim_state:
            fIO.write(f'It\'s The Same Country! ({countries[victim_state]}) Nothing Happens\n')
            print(f'It\'s The Same Country! ({countries[victim_state]}) Nothing Happens\n')
        else:
            battlers = []
            battlers.append(countries[victim_state])
            battlers.append(countries[countrybattle])

            print(f'It\'s {battlers[1]} vs. {battlers[0]} ')
            fIO.write(f'It\'s {battlers[1]} vs. {battlers[0]} ')
            if bool(rm.getrandbits(1)):
                print(f'{battlers[0]} Wins and incorporates {battlers[1]}\n')
                fIO.write(f'{battlers[0]} Wins and incorporates {battlers[1]}\n')
                countries.remove(countries[countrybattle])
            else:
                print(f'{battlers[1]} Wins and incorporates {battlers[0]}\n')
                fIO.write(f'{battlers[1]} Wins and incorporates {battlers[0]}\n')
                countries.remove(countries[victim_state])
fIO.close()
input('>')    
