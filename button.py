import pygame as pg

class button:
    screen: pg.Surface
    rect : pg.Rect
    on: bool
    x: int
    y: int
    text_color: str
    number: str
    box_color: str
    text_surface_object : pg.Surface
    def __init__(self, number,  screen, x =0, y = 0) -> None:
        self.on = False
        self.x = x
        self.y = y
        self.screen = screen
        self.number = number
        self.text_color = "black"
        self.box_color = "red"
        self.rect =  pg.draw.rect(self.screen, self.box_color, (self.x, self.y, 100, 100))  
        self.text_surface_object = pg.font.SysFont("Arial", 40).render(self.number, True, self.text_color)
        self.text_rect = self.text_surface_object.get_rect(center=self.rect.center)
        self.screen.blit(self.text_surface_object, self.text_rect)

    def lightup(self, color:str, soundfile: str):
        self.box_color = color
        self.rect =  pg.draw.rect(self.screen, self.box_color, (self.x, self.y, 100, 100))  
        self.text_surface_object = pg.font.SysFont("Arial", 40).render(self.number, True, self.text_color)
        self.text_rect = self.text_surface_object.get_rect(center=self.rect.center)
        self.screen.blit(self.text_surface_object, self.text_rect)
        self.on = False
        pg.display.flip()
        pg.mixer.music.load(soundfile)
        pg.mixer.music.set_volume(2.7)
        pg.mixer.music.play()
        pg.mixer.music.fadeout(800)
        pg.time.wait(500)
        self.box_color = "red"
        self.rect =  pg.draw.rect(self.screen, self.box_color, (self.x, self.y, 100, 100))  
        self.text_surface_object = pg.font.SysFont("Arial", 40).render(self.number, True, self.text_color)
        self.text_rect = self.text_surface_object.get_rect(center=self.rect.center)
        self.screen.blit(self.text_surface_object, self.text_rect)
        pg.display.flip()
        pg.time.wait(500)
        return



