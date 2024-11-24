import pygame
import random
import sys

pygame.init() # important!!!
pygame.display.set_caption('Coffee Shop Detective')
clock = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
    
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

test_surface = pygame.Surface((100,200))

counter = pygame.image.load(f"Images2/Counter.PNG")
cocoa_powder = pygame.image.load(f"Images2/Cocoa_powder.png")
coffee_powder = pygame.image.load(f"Images2/coffee.png")
cream = pygame.image.load(f"Images2/Cream.png")
cup = pygame.image.load(f"Images2/cup.PNG")
customer_1 = pygame.image.load(f"Images2/Customer 1.png")
customer_2 = pygame.image.load(f"Images2/Customer 2.png")
customer_3 = pygame.image.load(f"Images2/Customer 3.png")
customer_4 = pygame.image.load(f"Images2/Customer 1.png")
customer_5 = pygame.image.load(f"Images2/Customer 2.png")
ice_cubes = pygame.image.load(f"Images2/Ice.png")
marshmallows = pygame.image.load(f"Images2/Marshmallows.png")
matcha_powder = pygame.image.load(f"Images2/matcha_powder.png")
oat_milk = pygame.image.load(f"Images2/oat_milk.png")
sales_room_background = pygame.image.load(f"Images2/selling Background.PNG")
startscreen = pygame.image.load(f"Images2/Startscreen.png")
sugar = pygame.image.load(f"Images2/sugar.png")
tapioca = pygame.image.load(f"Images2/Tapioka.png")
tea = pygame.image.load(f"Images2/Tea.png")
text_bubble = pygame.image.load(f"Images/text bubble.png")
regular_milk = pygame.image.load(f"Images2/regular_milk.PNG")
lactose_free = pygame.image.load(f"Images2/lactose_free_milk.PNG")
start_button = pygame.image.load(f"Images2/Startbutton.PNG")

room = "start room"



ingredients = {
    "base": ["white milk", "oat milk"],
    "powder": ["cocoa powder", "coffee powder", "matcha powder", "tea"],
    "topping": ["sugar", "ice cubes", "boba", "marshmallows", "cream"]
}

selected_items = {"regular_milk": False, 
                  "lactose_free": False,
                  "cocoa_powder": False,
                  "oat_milk": False,
                  "coffee_powder": False, 
                  "tea": False,
                  "matcha_powder": False,
                  "marshmallows": False,
                  "ice_cubes": False, 
                  "sugar": False,
                  "tapioca": False,
                  "cream": False }

def draw_sale_room(): 
    global sales_room_background, cup
    sales_room_background_scaled = pygame.transform.scale(sales_room_background, (1000, 1000)) 
    screen.blit(sales_room_background_scaled, (0, 0)) 
    screen.blit(random_customer, (0, 0)) 
    screen.blit(counter, (0, 250)) 
    scaled_cup = pygame.transform.scale(cup, (220, 220)) 
    screen.blit(scaled_cup, (450, 300)) 
    # Zutaten basierend auf dem Status zeichnen 
    if selected_items["regular_milk"]:
        screen.blit(regular_milk, (490, 340)) 
    if selected_items["lactose_free"]: 
        screen.blit(lactose_free, (490, 310)) 
    if selected_items["oat_milk"]: 
        screen.blit(oat_milk, (500, 340)) 
    if selected_items["cocoa_powder"]: 
        screen.blit(cocoa_powder, (470, 335)) 
    if selected_items["coffee_powder"]: 
        screen.blit(coffee_powder, (500, 350)) 
    if selected_items["tea"]: 
        screen.blit(tea, (490, 350)) 
    if selected_items["matcha_powder"]: 
        screen.blit(matcha_powder, (490, 345)) 
    if selected_items["marshmallows"]: 
        screen.blit(marshmallows, (510, 340)) 
    if selected_items["ice_cubes"]: 
        screen.blit(ice_cubes, (480, 340)) 
    if selected_items["sugar"]: 
        screen.blit(sugar, (530, 410)) 
    if selected_items["tapioca"]: 
        screen.blit(tapioca, (510, 400)) 
    if selected_items["cream"]: 
        screen.blit(cream, (450, 300))


def create_random_order():
    return {
        "base": random.choice(ingredients["base"]),
        "powder": random.choice(ingredients["powder"]),
        "toppings": random.sample(ingredients["topping"], 2)
    }
def reset_game():
    """Reset for a new customer."""
    global current_order, customer_image, selected_items
    current_order = create_random_order()
    customer_image = random.choice([customer_1, customer_2, customer_3, customer_4, customer_5])
    selected_items = {"base": None, "powder": None, "toppings": []}

def evaluate_order():
    """Compare selected items with the current order."""
    if selected_items["base"] == current_order["base"] and \
       selected_items["powder"] == current_order["powder"] and \
       sorted(selected_items["toppings"]) == sorted(current_order["toppings"]):
        return True
    return False

def draw_order_text():
    """Display the customer's order on the screen."""
    font = pygame.font.Font(None, 36)
    base_text = font.render(f"Base: {current_order['base']}", True, (0, 0, 0))
    powder_text = font.render(f"Powder: {current_order['powder']}", True, (0, 0, 0))
    toppings_text = font.render(f"Toppings: {', '.join(current_order['toppings'])}", True, (0, 0, 0))
    screen.blit(base_text, (20, 20))
    screen.blit(powder_text, (20, 60))
    screen.blit(toppings_text, (20, 100))



random_customer = random.randint(1,6)
if random_customer == 1:
    random_customer = customer_1
elif random_customer == 2:
    random_customer = customer_2
elif random_customer == 3:
    random_customer = customer_3
elif random_customer == 4:
    random_customer = customer_4
elif random_customer == 5:
    random_customer = customer_5
    

running = True
while running: 
    for event in pygame.event.get():        
        if event.type == pygame.QUIT: 
            running = False
            sys.exit()

        clock.tick(60)

        if room == "start room": 


            startscreen = pygame.transform.scale(startscreen, (1000, 1000))
            screen.blit(startscreen, (0,0))
            start_button = pygame.transform.scale(start_button, (250, 250))
            screen.blit(start_button, (400, 500))
        elif room == "sale room":
            draw_sale_room()
        
            if event.type == pygame.MOUSEBUTTONDOWN and room  == "sale room":
               
                x, y = pygame.mouse.get_pos()
                print(x,y)
                # find out where to click
                if 200 > x > 140 and 590 < y < 660:
                    selected_items["regular_milk"] = True
                elif 100 > x > 30 and 560 < y < 630:
                    selected_items["lactose_free"] = True
                elif 120 > x > 60 and 670 < y < 740:
                    selected_items["oat_milk"] = True

                if 460 > x > 380 and 670 < y < 740:
                    selected_items["cocoa_powder"] = True
                elif 360 > x > 300 and 570 < y < 650:
                    selected_items["coffee_powder"] = True
                elif 370 > x > 300 and 670 < y < 740:
                    selected_items["tea"] = True
                elif 450 > x > 380 and 570 < y < 650:
                    selected_items["matcha_powder"] = True
                
                if 960 > x > 890 and 560 < y < 650:
                    selected_items["marshmallows"] = True

                if 710 > x > 630 and 570 < y < 740:
                    selected_items["ice_cubes"] = True
                
                if 610 > x > 530 and 570 < y < 740:
                    selected_items["sugar"] = True


                if 870 > x > 790 and 560 < y < 750:
                    selected_items["tapioca"] = True

                if 960 > x > 890 and 670 < y < 750:
                    selected_items["cream"] = True



                
            
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN and room  == "start room":
            x, y = pygame.mouse.get_pos()
            if 650 > x > 400 and 500 < y < 750:
                room = "sale room"
        pygame.display.update()



        
                

                

        

        




