from PIL import Image as image, ImageFont as font, ImageDraw as drawer

banner = """

 ██████╗███████╗██████╗ ████████╗     ██████╗ ███████╗███╗   ██╗ version: 1.0
██╔════╝██╔════╝██╔══██╗╚══██╔══╝    ██╔════╝ ██╔════╝████╗  ██║
██║     █████╗  ██████╔╝   ██║       ██║  ███╗█████╗  ██╔██╗ ██║
██║     ██╔══╝  ██╔══██╗   ██║       ██║   ██║██╔══╝  ██║╚██╗██║
╚██████╗███████╗██║  ██║   ██║       ╚██████╔╝███████╗██║ ╚████║
 ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝ by: ivanrbnc
                                                                
"""

success_banner = """                                        
                                                              
  █████  █████ ████  ██████   ██████   ██████   █████   █████ 
 ███░░  ░░███ ░███  ███░░███ ███░░███ ███░░███ ███░░   ███░░  
░░█████  ░███ ░███ ░███ ░░░ ░███ ░░░ ░███████ ░░█████ ░░█████ 
 ░░░░███ ░███ ░███ ░███  ███░███  ███░███░░░   ░░░░███ ░░░░███
 ██████  ░░████████░░██████ ░░██████ ░░██████  ██████  ██████ 
░░░░░░    ░░░░░░░░  ░░░░░░   ░░░░░░   ░░░░░░  ░░░░░░  ░░░░░░  
                                                                                                                                                                 
"""

def generator():
    #TODO: Customize your names source
    text_file = open(r'resources/names.txt')
    names = text_file.read().split('\n')

    #TODO: Customize your font source, size, and color
    font_used = font.truetype(r'resources/ArianaVioleta-dz2K.ttf', 180)
    font_color_used = "#000000"

    for name in names:
        #TODO: Customize your template source
        template = image.open(r'resources/template.png')
        draw = drawer.Draw(template)

        coordinates = draw.textbbox((0,0), name, font=font_used)

        #TODO: Customize your text placement
        draw.text(((template.size[0] - coordinates[2]) / 2 - 0, (template.size[1] - coordinates[3]) / 2 - 65), name, fill=font_color_used, font=font_used)

        template.save("./results/" + name +".png")    
    
if __name__ == "__main__":
    print(banner)
    print('Now loading..')
    generator()
    print(success_banner)
    input('Press enter to continue..')

