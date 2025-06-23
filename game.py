name = input('Hi, what is your name: ')
print(f'Hello {name}, welcome to my game! ')
print('You wake up in a quiet forest clearing. You hear the sound of water in the distance and see two paths ahead of you.')
print('Do you want to play a game? (yes/no)')
play = input('> ').lower()

if play == 'yes':
    print('game on! 😊')
    print('You can go left toward the sound of water, or right into the dark woods. Where do you go? (left/right) 🤔' )
    choice = input('> ').lower()
    if choice == 'left':
        print('You find a shaky rope bridge over a river.')
        print('Do you want to cross it or turn back? (cross/ turn back) 🤔')
        choice = input('> ').lower()
        if choice == 'cross':
            print('The bridge creaks, but you make it across. You find a chest buried under a tree.')
            print('Open the chest? (yes/no) 🤔')
            choice = input('> ').lower()
            if choice == 'yes':
                print('🎉 You find a magical map that leads you out safely.')
            else:
                print(' A wild boar charges you for lingering. Game over. 😒')
        elif choice == 'turn back':
            print('A wild boar charges you for lingering. Game over. 😒')
    if choice == 'right':
        print('The woods get darker, and you stumble upon a sleeping bear. 😨')
        print('Do you wanna sneak past it or run? (sneak / run) 🤔')
        choice = input('> ').lower()
        if choice == 'sneak':
            print('You tiptoe around... success! You find a cave. 😁')
            print('Enter cave? (yes/no) 🤔')
            choice = input('> ').lower()
            if choice == 'yes':
                print('Inside is an old traveler who gives you safe passage. You survive. 🎉')
            elif choice == 'no':
                print('You get lost trying to backtrack. Bear attacks you. Game over. 😒')
        elif choice == 'run':
            print('You wake the bear. You already know how that ends. Game over! 🐻')
            
else:
    print('We are NOT playing...😔')