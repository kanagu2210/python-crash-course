def print_guests():
    for guest in guest_list:
        print(f'Bless me, {guest}!')
    print('\n')


guest_list = ['J Krishnamurthi', 'Ramana Maharishi', 'Sadhguru']
print_guests()

cant_come_guest = guest_list[2]
print(f'{cant_come_guest} cant come!')

guest_list[2] = 'Anni Besant'
print_guests()

guest_list.insert(0, 'Annamalai swamy')
middle_of_list = int(len(guest_list) / 2)
guest_list.insert(middle_of_list, 'Osho')
guest_list.append('Papaji')
print_guests()

