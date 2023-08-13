import sys
import pygame
import keyboard

pygame.mixer.init()

print('w = snare\na = clap\ns = tom\nd = hat\nq = bass 1\ne = bass 2\nr = crash\nf = snare roll\ny = badumtsss\np = stop\n0 = pause\n9 = unpause')

while True:

        if keyboard.is_pressed('w'):
        #snare
            snare = pygame.mixer.Sound('snare.wav')
            snare.set_volume(0.4)
            pygame.mixer.Channel(1).play(snare)

        if keyboard.is_pressed('a'):
        #clap
            clap = pygame.mixer.Sound('clap.wav')
            clap.set_volume(0.4)
            pygame.mixer.Channel(7).play(clap)

        if keyboard.is_pressed('s'):
        #tom
            tom = pygame.mixer.Sound('tom.wav')
            tom.set_volume(0.4)
            pygame.mixer.Channel(2).play(tom)

        if keyboard.is_pressed('s'):
        #hat
            hat = pygame.mixer.Sound('hat.wav')
            tom.set_volume(0.4)
            pygame.mixer.Channel(4).play(hat)

        if keyboard.is_pressed('q'):
        #basedrum1
            basedrum = pygame.mixer.Sound('basedrum.wav')
            basedrum.set_volume(0.4)
            pygame.mixer.Channel(5).play(basedrum)

        if keyboard.is_pressed('e'):
        #basedrum2
            basedrum2 = pygame.mixer.Sound('basedrum2.wav')
            basedrum2.set_volume(0.4)
            pygame.mixer.Channel(6).play(basedrum2)

        if keyboard.is_pressed('r'):
        #crash
            crash = pygame.mixer.Sound('crash.wav')
            crash.set_volume(0.4)
            pygame.mixer.Channel(3).play(crash)

        if keyboard.is_pressed('f'):
        #snare roll
            snareroll = pygame.mixer.Sound('snareroll.wav')
            snareroll.set_volume(0.4)
            pygame.mixer.Channel(4).play(snareroll)

        #Play special effects:
        if keyboard.is_pressed('y'):
        #badum tss
            badum = pygame.mixer.Sound('badumtss.wav')
            badum.set_volume(0.5)
            pygame.mixer.Channel(1).play(badum)

        #Stop all sounds:
        if keyboard.is_pressed('p'):
            pygame.mixer.stop()
        if keyboard.is_pressed('0'):
            pygame.mixer.pause()
        if keyboard.is_pressed('9'):
            pygame.mixer.unpause()

