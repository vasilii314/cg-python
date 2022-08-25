import sys

import pygame

from core.input import Input


class Base(object):
    def __init__(self, screen_size=[512, 512]):
        # init all pygame modules
        pygame.init()

        # indicate rendering details
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL

        # initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

        # use core opengl profile for cross-platform compatibility
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE
        )

        # create and display the window
        self.screen = pygame.display.set_mode(screen_size, display_flags)

        # set the text that appears in the title bar of the window
        pygame.display.set_caption('Graphics Window')

        # determine if while loop is active
        self.running = True

        # manage time-related data operations
        self.clock = pygame.time.Clock()

        self.input = Input()

        self.time = 0


    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()

        while self.running:
            self.input.update()
            if self.input.quit:
                self.running = False
            # seconds since iteration of run loop
            self.delta_time = self.clock.get_time() / 1000
            # increment time application has been running
            self.time += self.delta_time
            self.update()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()


