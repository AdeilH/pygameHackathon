# Example file showing a circle moving on screen
import pygame
import button
import random
import data_structures
# pygame setup


pygame.init()

screen = pygame.display.set_mode((600, 600))

list_of_four = ['2','4','6','8']
computer_turn = data_structures.queue()
difficulty = 1
clock = pygame.time.Clock()
user_turn = False
running = True
dt = 0
text_surface_object = pygame.font.SysFont("Arial", 12).render("0", True, "red")
generated = 0
pygame.event.set_blocked(pygame.MOUSEMOTION)
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
pygame.event.set_blocked(pygame.KEYUP)
pygame.event.set_blocked(pygame.TEXTINPUT)
pygame.event.set_blocked(pygame.WINDOWFOCUSLOST)
pygame.event.set_blocked(pygame.WINDOWFOCUSGAINED)
pygame.event.set_blocked(pygame.WINDOWLEAVE)
pygame.event.set_blocked(pygame.WINDOWENTER)
pygame.event.set_blocked(pygame.ACTIVEEVENT)
pygame.mouse.set_visible(False)

font = pygame.font.Font('freesansbold.ttf', 32)


scoretext = font.render('Score is ', True, "white")
scoretextRect = scoretext.get_rect()
scoretextRect.center = (screen.get_rect().centerx // 2, screen.get_rect().centery + 250)

userturntext = font.render('User turn', True, "white")
userturntextRect = userturntext.get_rect()
userturntextRect.center = (screen.get_rect().centerx // 2, screen.get_rect().centery + 200)

pygame.display.set_caption('Simon')

pygame.mixer.init()
center = screen.get_rect()
center.center
score = 0
while running:
    # poll for events
    
    # pygame.QUIT event means the user clicked X to close your window
        # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    score_text = 'Score is ' + str(score)
    scoretext = font.render(score_text, True, "white")
    screen.blit(scoretext, scoretextRect)
    bt1 = button.button("2", screen, center.centerx - 50, center.centery + 25)
    bt2 = button.button("4", screen, center.centerx - 200, center.centery - 100)
    bt3 = button.button("6", screen, center.centerx + 100, center.centery - 100)
    bt4 = button.button("8", screen, center.centerx - 50, center.centery - 225)
    pygame.display.flip()
    pygame.time.wait(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    random_number  = random.choice(list_of_four)

    if random_number == '2':
        bt1.lightup("green", "Piano.pp.C1.wav")
        computer_turn.push_back('2')
    if random_number == '4':
        bt2.lightup("green", "Piano.pp.F1.wav")
        computer_turn.push_back('4')
    if random_number == '6':
        bt3.lightup("green", "Piano.pp.G1.wav")
        computer_turn.push_back('6')
    if random_number == '8':
        bt4.lightup("green", "Piano.pp.A1.wav")
        computer_turn.push_back('8')

    generated = generated + 1
    if generated == difficulty:
        pygame.event.clear()
        userturntextRect.center = (screen.get_rect().centerx // 2, screen.get_rect().centery + 200)
        userturntext = font.render('User turn', True, "white")
        screen.blit(userturntext, userturntextRect)
        pygame.display.flip()
        user_turn = True
        print(generated)
    if user_turn:
        print(user_turn)
        print(computer_turn.internal_list)
        correct = True
        while user_turn:
            if computer_turn.isempty():
                user_turn = False
                if correct:
                    userturntext = font.render('Correct', True, "green")
                    userturntextRect.center = (screen.get_rect().centerx + 50, screen.get_rect().centery + 200)
                    screen.blit(userturntext, userturntextRect)
                    pygame.display.flip()
                    pygame.time.wait(1500)
                    difficulty = difficulty + 1
                    score = score + 1
                else:
                    userturntext = font.render('Wrong Move', True, "red")
                    userturntextRect.center = (screen.get_rect().centerx + 50, screen.get_rect().centery + 200)
                    screen.blit(userturntext, userturntextRect)
                    pygame.display.flip()
                    pygame.time.wait(1500)
                    screen.blit(userturntext, userturntextRect)
                generated = 0
                pygame.display.flip()
                break
            user_event = pygame.event.wait()
            print(user_event)
            
            if user_event.type == pygame.QUIT:
                running = False
                user_turn = False
            if user_event.type == pygame.KEYDOWN:
                if user_event.key == pygame.K_KP2 or user_event.key == pygame.K_2:
                    print("2")
                    if computer_turn.pop() == "2":
                        bt1.lightup("green", "Piano.pp.C1.wav")
                        print("Right Move")
                        continue
                    else:
                        correct = False
                        computer_turn.emptyqueue()
                        print("Wrong Move")
                if user_event.key == pygame.K_KP4 or user_event.key == pygame.K_4:
                    print("4")
                    if computer_turn.pop() == "4":
                        bt2.lightup("green", "Piano.pp.F1.wav")
                        print("Right Move")
                        continue
                    else:
                        correct = False
                        computer_turn.emptyqueue()
                        print("Wrong Move")
                if user_event.key == pygame.K_KP6 or user_event.key == pygame.K_6:
                    print("6")
                    if computer_turn.pop() == "6":
                        bt3.lightup("green", "Piano.pp.G1.wav")
                        print("Right Move")
                        continue
                    else:
                        correct = False
                        computer_turn.emptyqueue()
                        print("Wrong Move")
                if user_event.key == pygame.K_KP8 or user_event.key == pygame.K_8:
                    print("8")
                    if computer_turn.pop() == "8":
                        bt4.lightup("green", "Piano.pp.A1.wav")
                        print("Right Move")
                        continue
                    else:
                        correct = False
                        computer_turn.emptyqueue()
                        print("Wrong Move")
                print(True)
            
            else:
                print(False)
    # flip() the display to put your work on screen
    

    


    # pygame.time.wait(100)
    # limits wFPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()