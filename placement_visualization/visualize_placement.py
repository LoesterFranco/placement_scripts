import matplotlib
import matplotlib.pyplot as plt
import json
import random
import os
import argparse

def parse_args():
    """parse arguments to the script and return them
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('placement_input_file', help="input file of the placement problem instance")
    parser.add_argument('placement_sol_file', help="placement solution file")
    parser.add_argument('percent_nets', type=float, help="what percent of nets to visualize [0;100]")
    parser.add_argument('output_image_file', help="path of output image file")

    args = parser.parse_args()
    return args



def find_optimal_edges(net):
    res = []
    for i in range(len(net) - 1):
        res.append((net[i], net[i + 1]))
        
    return res

def find_optimal_edges(net):
    res = []
    for i in range(len(net) - 1):
        res.append((net[i], net[i + 1]))
        
    return res

def draw(height, width, module_positions, nets, percent_nets, colors):
    
    def cell_center(i, j):
        return (2 * i + 1) / (2 * height), (2 * j + 1) / (2 * width)
    
    fig, axs = plt.subplots(figsize=(width, height))

    axs.axis('off')

    # draw horizontal lines
    for i in range(1, height):
        y_coord = i / height
        plt.plot((0, 1), (y_coord, y_coord), color='black', linewidth=0.5)

    # draw vertical lines
    for i in range(1, width):
        x_coord = i / width
        plt.plot((x_coord, x_coord), (0, 1), color='black', linewidth=0.5)

    # draw borders
    plt.plot([0, 0], [0, 1], color='black')
    plt.plot([0, 1], [0, 0], color='black')
    plt.plot([1, 1], [0, 1], color='black')
    plt.plot([0, 1], [1, 1], color='black')    
    
    circle_ys = []
    circle_xs = []
    
    for module_id in module_positions:
        i = module_positions[module_id]["x"]
        j = module_positions[module_id]["y"]
        cx, cy = cell_center(i, j)
        circle_xs.append(cx)
        circle_ys.append(cy)
    
    plt.scatter(circle_ys, circle_xs, s=15 * (height + width))

    for i, net in enumerate(nets):
        
        if random.random() > percent_nets / 100.0:
            continue
        
        edges = find_optimal_edges(net)

        color_idx = random.randint(0, len(colors) - 1)
        color='xkcd:{}'.format(colors[color_idx])
        
        for edge in edges:
            sx = module_positions[str(edge[0])]["x"]
            sy = module_positions[str(edge[0])]["y"]
            ex = module_positions[str(edge[1])]["x"]
            ey = module_positions[str(edge[1])]["y"]
            
            sx, sy = cell_center(sx, sy)
            ex, ey = cell_center(ex, ey)
                
            
            plt.plot([sy, ey], [sx, ex], color=color)
            
    return plt

def main(input_filepath, sol_filepath, percent_nets, colors, img_path):
    with open(input_filepath) as f:
        input_data = json.load(f)

    height = input_data["height"]
    width = input_data["width"]

    with open(sol_filepath) as f:
        sol_data = json.load(f)

    nets = input_data["nets"]

    plt = draw(height, width, sol_data, nets, percent_nets, colors)

    plt.savefig(img_path, bbox_inches='tight')



if __name__ == "__main__":
    args = parse_args()

    input_filepath = args.placement_input_file
    sol_filepath = args.placement_sol_file
    percent_nets = args.percent_nets
    img_path = args.output_image_file

    if percent_nets < 0 or percent_nets > 100:
        raise IllegalArgumentException("Percent of nets must be in range [0;100]")


    xkcd_colors_path = r'{}'.format(os.path.join(os.path.realpath(os.path.dirname(__file__)), "xkcd_colors.txt"))

    with open(xkcd_colors_path, 'r') as f:
        xkcd_colors = f.readlines()
        xkcd_colors = [c.strip() for c in xkcd_colors]

    main(input_filepath, sol_filepath, percent_nets, xkcd_colors, img_path)

    


