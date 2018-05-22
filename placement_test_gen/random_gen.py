import numpy as np
import json
import argparse

def parse_args():
    """parse arguments to the script and return them
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('height', type=int, help="height of the board")
    parser.add_argument('width', type=int, help="width of the board")
    parser.add_argument('num_modules', type=int, help="number of modules")
    parser.add_argument('num_nets', type=int, help="number of nets")
    parser.add_argument('net_size_poisson_lambda', type=float, help="poisson distribution lambda for sampling ((net size) - 2)")

    args = parser.parse_args()
    return args


args = parse_args()

h = args.height
w = args.width
n = args.num_modules
m = args.num_nets
lmb = args.net_size_poisson_lambda


nets = []

for _ in range(m):
    net_size = min(np.random.poisson(lmb) + 2, n)
    net = list(np.random.choice(n, net_size, replace=False))
    net = [x + 1 for x in net]
    nets.append(net)

res = {"height" : h, "width" : w, "moduleCount" : n, "nets" : nets}

print(json.dumps(res))