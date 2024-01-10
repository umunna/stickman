import tkinter as tk
import random

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.player = self.create_player()  
        self.coin = self.canvas.create_oval(100, 100, 110, 110, fill='yellow')
        self.enemy = self.create_enemy()
        self.score = 0
         # Enemy speed
        self.speed = 40 
        self.score_text = self.canvas.create_text(20, 20, text=f'Score: {self.score}', anchor='nw', fill="white")
        self.root.bind('<Key>', self.move_player)
        self.move_enemy()

    def create_player(self):
        # Head
        head = self.canvas.create_oval(170, 170, 190, 190, fill='blue')

        # Body
        body = self.canvas.create_line(180, 190, 180, 220, fill="white")

        # Arms
        left_arm = self.canvas.create_line(180, 200, 170, 210, fill="white")
        right_arm = self.canvas.create_line(180, 200, 190, 210, fill="white")

        # Legs
        left_leg = self.canvas.create_line(180, 220, 170, 230, fill="white")
        right_leg = self.canvas.create_line(180, 220, 190, 230, fill="white")

        return [head, body, left_arm, right_arm, left_leg, right_leg]

    def create_enemy(self):
        # Head
        head = self.canvas.create_oval(280, 240, 310, 270, fill='red')

        # Body
        body = self.canvas.create_line(295, 270, 295, 300, fill="white")

        # Arms
        left_arm = self.canvas.create_line(295, 285, 285, 275, fill="white")
        right_arm = self.canvas.create_line(295, 285, 305, 275, fill="white")

        # Legs
        left_leg = self.canvas.create_line(295, 300, 285, 310, fill="white")
        right_leg = self.canvas.create_line(295, 300, 305, 310, fill="white")

        return [head, body, left_arm, right_arm, left_leg, right_leg]

    def move_player(self, event):
        # head's coordinates as the player's coordinates
        x, y, _, _ = self.canvas.coords(self.player[0])  
        if event.char == 'w' and y > 0:
            for part in self.player:
                self.canvas.move(part, 0, -10)
        elif event.char == 's' and y < 390:
            for part in self.player:
                self.canvas.move(part, 0, 10)
        elif event.char == 'a' and x > 0:
            for part in self.player:
                self.canvas.move(part, -10, 0)
        elif event.char == 'd' and x < 390:
            for part in self.player:
                self.canvas.move(part, 10, 0)
        self.check_collision()

    def move_enemy(self):
         # head's coordinates as the enemy's coordinates
        ex, ey, _, _ = self.canvas.coords(self.enemy[0]) 
        # head's coordinates as the player's coordinates
        px, py, _, _ = self.canvas.coords(self.player[0])  
        if ex < px:
            for part in self.enemy:
                self.canvas.move(part, 1, 0)
        elif ex > px:
            for part in self.enemy:
                self.canvas.move(part, -1, 0)
        if ey < py:
            for part in self.enemy:
                self.canvas.move(part, 0, 1)
        elif ey > py:
            for part in self.enemy:
                self.canvas.move(part, 0, -1)
        self.check_collision()
        # speed variable to control the enemy's speed
        self.root.after(self.speed, self.move_enemy)  

    def check_collision(self):
        # Use the head's coordinates as the player's coordinates
        px1, py1, px2, py2 = self.canvas.coords(self.player[0])  
        cx1, cy1, cx2, cy2 = self.canvas.coords(self.coin)
        if px1 < cx2 and px2 > cx1 and py1 < cy2 and py2 > cy1:
            self.score += 1
            # Decrease the delay (increase speed) each time a coin is collected, but don't go below 10
            self.speed = max(10, self.speed - 5)  
            self.canvas.itemconfig(self.score_text, text=f'Score: {self.score}')
            new_x = random.randint(0, 390)
            new_y = random.randint(0, 390)
            # Set new coin's coordinates after taking it.
            self.canvas.coords(self.coin, new_x, new_y, new_x + 10, new_y + 10)  
             # Use the head's coordinates as the enemy's coordinates
        ex1, ey1, ex2, ey2 = self.canvas.coords(self.enemy[0]) 
        if px1 < ex2 and px2 > ex1 and py1 < ey2 and py2 > ey1:
            self.canvas.create_text(200, 200, text='Game Over', font=('Consolas', 30), fill='red')
            # Wait for 2 seconds before closing the window
            self.root.after(2000, self.root.destroy)  

    def run(self):
        self.root.mainloop()

game = Game()
game.run()
