        screen.blit(button0,(50,200))
        screen.blit(button1,(100,200))
        screen.blit(button2,(150,200))
        screen.blit(button3,(200,200))
        screen.blit(button4,(50,250))
        screen.blit(button5,(100,250))
        screen.blit(button6,(150,250))
        screen.blit(button7,(200,250))
        screen.blit(button8,(50,300))
        screen.blit(button9,(100,300))
        screen.blit(buttona,(150,300))
        screen.blit(buttonb,(200,300))
        screen.blit(buttonc,(50,350))
        screen.blit(buttond,(100,350))
        screen.blit(buttone,(150,350))
        screen.blit(buttonf,(200,350))


        button1 = pygame.image.load("button1.jpg")
button1 = pygame.transform.scale(button1,(45,45))
button2 = pygame.image.load("button2.jpg")
button2 = pygame.transform.scale(button2,(45,45))
button3 = pygame.image.load("button3.jpg")
button3 = pygame.transform.scale(button3,(45,45))
button4 = pygame.image.load("button4.jpg")
button4 = pygame.transform.scale(button4,(45,45))
button5 = pygame.image.load("button5.jpg")
button5 = pygame.transform.scale(button5,(45,45))
button6 = pygame.image.load("button6.jpg")
button6 = pygame.transform.scale(button6,(45,45))
button7 = pygame.image.load("button7.jpg")
button7 = pygame.transform.scale(button7,(45,45))
button8 = pygame.image.load("button8.jpg")
button8 = pygame.transform.scale(button8,(45,45))
button9 = pygame.image.load("button9.jpg")
button9 = pygame.transform.scale(button9,(45,45))
button0 = pygame.image.load("button0.jpg")
button0 = pygame.transform.scale(button0,(45,45))
buttona = pygame.image.load("buttona.jpg")
buttona = pygame.transform.scale(buttona,(45,45))
buttonb = pygame.image.load("buttonb.jpg")
buttonb = pygame.transform.scale(buttonb,(45,45))
buttonc = pygame.image.load("buttonc.jpg")
buttonc = pygame.transform.scale(buttonc,(45,45))
buttond = pygame.image.load("buttond.jpg")
buttond = pygame.transform.scale(buttond,(45,45))
buttone = pygame.image.load("buttone.jpg")
buttone = pygame.transform.scale(buttone,(45,45))
buttonf = pygame.image.load("buttonf.jpg")
buttonf = pygame.transform.scale(buttonf,(45,45))


        #pygame.init()
        screen = pygame.display.set_mode(SCREEN_RECT.size)
        pygame.display.set_caption("Short Tale Story")
        player = Player(os.path.join("data", "pipo-charachip021.png"))
        group = pygame.sprite.RenderUpdates()
        group.add(player)
        fieldMap = Map(screen, "field.map", player)
        player.set_map(fieldMap)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            screen.fill((0, 255, 0))
            fieldMap.draw()
            group.update()
            group.draw(screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()