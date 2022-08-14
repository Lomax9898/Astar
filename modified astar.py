import pygame
import math


def line_distance(value, value2):  # Finds the value cost for two points
    d = math.sqrt((value2[0] - value[0]) ** 2 + (value2[1] - value[1]) ** 2)
    return d


def reconstruct_path(came_from, current):  # Path construction
    total_path = []
    while current in came_from:
        total_path.insert(0, current)
        current = came_from[current]
    total_path.insert(0, current)
    return total_path


trunk = {"S_Pos": ["Rec1TL", "Rec1BL", "Rec2L"],  # The possible routes for each point for the first environment
         "Rec1TL": ["Rec1TR", "Rec2L", "Rec2B"],
         "Rec1TR": ["Tri1L", "QuaL", "Tri1R"],
         "Rec1BL": ["Rec1BR"],
         "Rec1BR": ["QuaL", "Rec1TR", "Tri1L", "QuaB", "Tri1R"],
         "Rec2L": ["Rec2T", "Rec2B"],
         "Rec2T": ["Rec2R"],
         "Rec2R": ["Rec1TR", "Tri1L", "Tri1T", "Tri2L", "Tri2T"],
         "Rec2B": ["Rec1TR", "Tri1L", "Tri1T"],
         "Tri1L": ["Tri1T", "Tri1R", "QuaL"],
         "Tri1R": ["G_Pos", "QuaT", "Tri2R", "Tri2L"],
         "Tri1T": ["Tri2L", "Tri2T", "Tri1R"],
         "Tri2L": ["Tri2T", "Tri2R", "G_Pos", "QuaT"],
         "Tri2R": ["G_Pos"],
         "Tri2T": ["G_Pos", "Tri2R"],
         "QuaL": ["QuaT", "QuaB", "Tri1R"],
         "QuaR": ["QuaT", "G_Pos"],
         "QuaT": ["G_Pos"],
         "QuaB": ["QuaR"],
         "G_Pos": []
         }

Points_2 = {  # Where the nodes are on the screen
    "S_Pos": (50, 300),
    "Rec1TL": (74, 254),
    "Rec1BL": (74, 338),
    "Rec1TR": (340, 254),
    "Rec1BR": (340, 338),
    "Rec2L": (78, 154),
    "Rec2T": (136, 14),
    "Rec2R": (316, 89),
    "Rec2B": (258, 230),
    "Tri1L": (352, 208),
    "Tri1T": (384, 142),
    "Tri1R": (489, 232),
    "Tri2L": (446, 150),
    "Tri2T": (505, 60),
    "Tri2R": (562, 110),
    "QuaL": (414, 311),
    "QuaR": (642, 214),
    "QuaT": (596, 184),
    "QuaB": (613, 260),
    "G_Pos": (620, 118),
}

values_2 = {  # Where the Nodes are if the y value is not flipped like in pygame
    "S_Pos": (50, 51),
    "Rec1TL": (74, 97),
    "Rec1BL": (74, 13),
    "Rec1TR": (340, 254),
    "Rec1BR": (340, 13),
    "Rec2L": (78, 197),
    "Rec2T": (136, 337),
    "Rec2R": (316, 262),
    "Rec2B": (258, 121),
    "Tri1L": (352, 143),
    "Tri1T": (384, 209),
    "Tri1R": (489, 119),
    "Tri2L": (446, 201),
    "Tri2T": (505, 291),
    "Tri2R": (562, 110),
    "QuaL": (414, 40),
    "QuaR": (642, 137),
    "QuaT": (596, 167),
    "QuaB": (613, 91),
    "G_Pos": (620, 233),
}
tree = {"S_Pos": ["Rec1TL", "Rec1BL", "PenBL", "PenL"],  # The possible routes for each point for the first environment
        "Rec1TL": ["Rec1TR", "Tri1L", "PenBR", "PenBL", "Tri1R"],
        "Rec1BL": ["Rec1BR"],
        "Rec1TR": ["Tri2T", "Tri2L"],
        "Rec1BR": ["Tri2T", "Tri2L", "Tri2R", "HexB"],
        "PenBL": ["PenL"],
        "PenBR": ["PenR", "Tri1T", "Tri1L"],
        "PenL": ["PenT"],
        "PenT": ["Qua1L", "Tri1T", "PenR"],
        "PenR": ["Tri1T", "Qua1L", "Tri1L"],
        "Tri1L": ["Tri1T", "Tri1R", "Rec1TR"],
        "Tri1T": ["Tri1R", "Qua1L", "Qua1B"],
        "Tri1R": ["Rec1TR", "Tri2T", "Qua1B", "Qua1R"],
        "Qua1L": ["Qua1T", "Qua1B"],
        "Qua1T": ["Qua1R", "Rec2TL", "Rec2TR"],
        "Qua1R": ["Rec2TL", "Rec2BL"],
        "Qua1B": ["Tri2T", "Rec2BL", "Qua1R"],
        "Tri2T": ["Tri2L", "Tri2R", "Rec2BL"],
        "Tri2L": ["Tri2R", "HexTL", "HexBL"],
        "Tri2R": ["Rec2BR", "HexTL"],
        "Rec2TL": ["Rec2TR", "Qua2T"],
        "Rec2TR": ["Qua2T", "Qua2L"],
        "Rec2BL": ["Rec2BR", "HexT", "Qua2B"],
        "Rec2BR": ["Qua2L", "HexT", "Qua2B"],
        "HexTL": ["HexT", "Rec2BR"],
        "HexT": ["Qua2L", "HexTR", "Qua2B"],
        "HexTR": ["Qua2B"],
        "HexBL": ["HexB", "HexTL"],
        "HexB": ["HexBR"],
        "HexBR": ["HexTR", "Qua2B"],
        "Qua2T": ["Qua2R", "G_Pos"],
        "Qua2L": ["Qua2T"],
        "Qua2R": ["G_Pos"],
        "Qua2B": ["Qua2R", "G_Pos"],
        "G_Pos": []
        }

Points = {  # Where the nodes are on the screen for the first environment
    "S_Pos": (60, 300),
    "Rec1TL": (83, 253),
    "Rec1BL": (83, 340),
    "Rec1TR": (330, 253),
    "Rec1BR": (330, 340),
    "PenBL": (71, 190),
    "PenL": (56, 100),
    "PenT": (145, 12),
    "PenR": (203, 98),
    "PenBR": (156, 210),
    "Tri1L": (206, 217),
    "Tri1R": (274, 217),
    "Tri1T": (238, 82),
    "Qua1B": (280, 127),
    "Qua1L": (280, 20),
    "Qua1T": (340, 10),
    "Qua1R": (383, 62),
    "Tri2T": (340, 173),
    "Tri2L": (366, 296),
    "Tri2R": (417, 243),
    "Rec2TL": (397, 22),
    "Rec2TR": (500, 22),
    "Rec2BL": (397, 199),
    "Rec2BR": (500, 199),
    "Qua2L": (514, 44),
    "Qua2T": (551, 18),
    "Qua2R": (580, 52),
    "Qua2B": (566, 218),
    "HexT": (512, 207),
    "HexTL": (456, 249),
    "HexTR": (556, 249),
    "HexBL": (456, 312),
    "HexBR": (556, 316),
    "HexB": (504, 344),
    "G_Pos": (594, 24),
}

values = {  # Where the nodes are on the screen for the first environment
    "S_Pos": (60, 51),
    "Rec1TL": (83, 98),
    "Rec1BL": (83, 11),
    "Rec1TR": (330, 98),
    "Rec1BR": (330, 11),
    "PenBL": (71, 161),
    "PenL": (56, 251),
    "PenT": (145, 339),
    "PenR": (203, 253),
    "PenBR": (156, 141),
    "Tri1L": (206, 134),
    "Tri1R": (274, 134),
    "Tri1T": (238, 270),
    "Qua1B": (280, 224),
    "Qua1L": (280, 331),
    "Qua1T": (340, 341),
    "Qua1R": (383, 289),
    "Tri2T": (340, 178),
    "Tri2L": (366, 55),
    "Tri2R": (417, 108),
    "Rec2TL": (397, 329),
    "Rec2TR": (500, 329),
    "Rec2BL": (397, 152),
    "Rec2BR": (500, 152),
    "Qua2L": (514, 307),
    "Qua2T": (551, 333),
    "Qua2R": (580, 299),
    "Qua2B": (566, 218),
    "HexT": (512, 54),
    "HexTL": (456, 102),
    "HexTR": (556, 102),
    "HexBL": (456, 39),
    "HexBR": (556, 35),
    "HexB": (504, 7),
    "G_Pos": (594, 327),
}


class Program:
    def __init__(self):
        pygame.init()  # Initializing  variables
        self.screen = pygame.display.set_mode((686, 430))
        self.screen.fill(pygame.Color('white'))
        self.font_size = 30
        self.path_font_size = 20
        pygame.draw.rect(self.screen, pygame.Color('black'), (0, 0, 686, 351), 4)
        self.font = pygame.font.SysFont('Arial', self.font_size, bold=True)
        self.path_font = pygame.font.SysFont('Arial', self.path_font_size, bold=True)
        self.path = ""
        self.text_env = self.font.render("Press q or w to swap environments", True, (0, 0, 0))
        self.screen.blit(self.text_env, (10, 360))
        self.text_cost = self.font.render("Enter Cost:", True, (0, 0, 0))
        self.screen.blit(self.text_cost, (480, 360))
        self.input = pygame.Rect(615, 360, 60, 35)
        self.path_found = pygame.Rect(10, 400, 60, 35)
        pygame.draw.rect(self.screen, (pygame.Color('Grey')), self.input)
        self.active = False
        self.env = 0
        self.user_input = ""

    def find(self, graph, nodes, pygame_nodes):  # Modified A* Algorithm
        openset = {}
        closedset = set()
        came_from = {}

        openset['S_Pos'] = (math.inf, 0)
        try:
            while openset != 0:
                current = min(openset, key=lambda t: openset[t][0])
                (uscore, gscore) = openset[current]

                if current == 'G_Pos':
                    closedset.add('G_Pos')
                    total_path = reconstruct_path(came_from, current)
                    self.path = total_path
                    if len(total_path) > 9:  # A big path shrinks the font so that it can fit on screen
                        self.path_font_size = 15
                        self.path_font = pygame.font.SysFont('Arial', self.path_font_size, bold=True)
                    else:
                        self.path_font_size = 20
                        self.path_font = pygame.font.SysFont('Arial', self.path_font_size, bold=True)
                    text = self.path_font.render(("Path is: " + ' '.join(self.path)), True, (pygame.Color("black")))
                    self.screen.blit(text, self.path_found)
                    pygame.display.flip()
                    print("The path is: ")
                    for item in total_path:
                        print(item + " ", end='')

                    for item in range(len(total_path) - 1):
                        pygame.draw.line(self.screen, (pygame.Color('red')), pygame_nodes[total_path[item]],
                                         pygame_nodes[total_path[item + 1]], 3)
                    break
                del openset[current]
                closedset.add(current)
                neighbors = graph[current]
                for neighbor in neighbors:
                    tentative_gscore = gscore + line_distance(nodes[current], nodes[neighbor])
                    constraint = tentative_gscore + line_distance(nodes[current], nodes[neighbor])
                    if neighbor in openset:
                        pass
                    elif constraint >= int(self.user_input):
                        pass
                    else:
                        openset[neighbor] = (math.inf, math.inf)
                    try:
                        if tentative_gscore < openset[neighbor][1]:
                            came_from[neighbor] = current
                            uscore = (int(self.user_input) - tentative_gscore) / line_distance(nodes[current],
                                                                                               nodes["G_Pos"])
                            openset[neighbor] = (uscore, tentative_gscore)
                    except KeyError:
                        break
        except ValueError:
            print("Due to the C value, there is no such path to Goal")
            text = self.path_font.render("Due to the C value, there is no such path to the Goal", True,
                                         (pygame.Color("black")))
            self.screen.blit(text, self.path_found)
            pygame.display.flip()

    def blit_text(self):  # Prints the text to the screen 
        self.screen.blit(self.text_env, (10, 360))
        self.screen.blit(self.text_cost, (480, 360))

    def blit_input(self):  # Controls the cost input Box 
        color = (pygame.Color('grey'))
        color_active = pygame.Color('darkgrey')
        if self.active:
            color = color_active
        pygame.draw.rect(self.screen, color, self.input)
        text = self.font.render(self.user_input, True, (pygame.Color("black")))
        self.screen.blit(text, self.input)
        pygame.display.flip()

    def environment_1(self):  # Refreshes the screen with the environment
        self.screen.fill((pygame.Color('white')))
        self.blit_text()
        self.blit_input()
        pygame.draw.rect(self.screen, pygame.Color('black'), (0, 0, 686, 351), 4)
        pygame.draw.circle(self.screen, pygame.Color('black'), (60, 300), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (83, 253), (330, 253), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (83, 253), (83, 340), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (330, 253), (330, 340), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (83, 340), (330, 340), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (71, 190), (156, 210), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (71, 190), (56, 100), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (56, 100), (145, 12), 6)
        pygame.draw.line(self.screen, pygame.Color('black'), (145, 12), (203, 98), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (203, 98), (156, 210), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (206, 217), (274, 217), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (238, 82), (274, 217), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (206, 217), (238, 82), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (280, 127), (280, 20), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (280, 20), (340, 10), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (340, 10), (383, 62), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (383, 62), (280, 127), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (340, 173), (366, 296), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (340, 173), (417, 243), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (417, 243), (366, 296), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (397, 22), (397, 199), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (397, 22), (500, 22), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (500, 22), (500, 199), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (397, 199), (500, 199), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (512, 207), (456, 249), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (512, 207), (556, 249), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (456, 249), (456, 312), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (556, 249), (556, 316), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (556, 316), (504, 344), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (456, 312), (504, 344), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (514, 44), (551, 18), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (551, 18), (580, 52), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (580, 52), (566, 218), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (514, 44), (566, 218), 5)

        pygame.draw.circle(self.screen, pygame.Color('black'), (594, 24), 5)

    def environment_2(self):
        self.screen.fill((pygame.Color('white')))
        self.blit_text()
        self.blit_input()
        pygame.draw.circle(self.screen, pygame.Color('black'), (50, 300), 5)
        pygame.draw.rect(self.screen, pygame.Color('black'), (0, 0, 686, 351), 4)

        pygame.draw.line(self.screen, pygame.Color('black'), (74, 254), (340, 254), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (74, 338), (340, 338), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (74, 254), (74, 338), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (340, 254), (340, 338), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (78, 154), (136, 14), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (136, 14), (316, 89), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (78, 154), (258, 230), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (258, 230), (316, 89), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (352, 208), (384, 142), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (384, 142), (489, 232), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (352, 208), (489, 232), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (446, 150), (505, 60), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (505, 60), (562, 110), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (446, 150), (562, 110), 5)

        pygame.draw.line(self.screen, pygame.Color('black'), (414, 311), (596, 184), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (414, 311), (613, 260), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (613, 260), (642, 214), 5)
        pygame.draw.line(self.screen, pygame.Color('black'), (596, 184), (642, 214), 5)

        pygame.draw.circle(self.screen, pygame.Color('black'), (620, 118), 5)

    def run(self):  # Handles pygame events
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  # Confirms button has been pressed
                    if self.input.collidepoint(event.pos):
                        self.active = True
                    else:
                        self.active = False
                    self.blit_input()

                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_input = self.user_input[:-1]
                            self.blit_input()
                        else:  # Only takes four number inputs
                            if len(self.user_input) < 4 and (event.key == pygame.K_0 or event.key == pygame.K_1 or
                                                             event.key == pygame.K_2 or event.key == pygame.K_3 or
                                                             event.key == pygame.K_4 or event.key == pygame.K_5 or
                                                             event.key == pygame.K_6 or event.key == pygame.K_7 or
                                                             event.key == pygame.K_8 or event.key == pygame.K_9 or
                                                             event.key == pygame.K_0):
                                self.user_input += event.unicode
                                self.blit_input()
                        if event.key == pygame.K_RETURN:  # The enter key starts up A* 
                            if self.env == 1:
                                self.environment_1()
                                self.find(tree, values, Points)
                            elif self.env == 2:
                                self.environment_2()
                                self.find(trunk, values_2, Points_2)

                if event.type == pygame.KEYDOWN:  # Pressing the q or w keys changes the environment 
                    if event.key == pygame.K_q:
                        self.environment_1()
                        self.env = 1

                    elif event.key == pygame.K_w:
                        self.environment_2()
                        self.env = 2

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()


if __name__ == '__main__':
    prog = Program()
    prog.run()
