from settings import *
from particle import Particle
from node import Node


screen = pygame.display.set_mode(resolution)


def draw(particle: Particle):
    pygame.draw.circle(screen, particle.color, particle.position, particle.radius)


def generate_nodes():
    pygame.init()
    clock = pygame.time.Clock()

    release = True
    particles = []
    for k in range(default_number_of_planets):
        particles.append(Particle())
    while True:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #  Generate new particle with each mouse click
        click = pygame.mouse.get_pressed()
        if click[0] == 1 and release is True:
            mouse = pygame.mouse.get_pos()
            particles.append(Particle(position=mouse))
            release = False
        if click[0] == 0:
            release = True

        nodes = Node(particles, [0, resolution[0]], [0, resolution[1]], screen, 0)
        for j in range(len(particles)):
            draw(particles[j])
        clock.tick(frame_rate)
        
        for particle in particles:
            particle.position += particle.velocity
            particle.position[0] %= resolution[0]
            particle.position[1] %= resolution[1]
        
        
        pygame.display.update()


if __name__ == "__main__":
    generate_nodes()
