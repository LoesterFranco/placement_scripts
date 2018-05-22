import numpy as np
import json
import argparse
import sys

def parse_args():
    """parse arguments to the script and return them
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('height', type=int, help="height of the board")
    parser.add_argument('width', type=int, help="width of the board")
    parser.add_argument('num_modules', type=int, help="number of modules")
    parser.add_argument('num_components', type=int, help="number of 'strongly' connected components")
    parser.add_argument('component_size_mean', type=float, help="mean size of 'strongly' connected components")
    parser.add_argument('component_size_stddev', type=float, help="standard distribution of size of components")
    parser.add_argument('num_component_nets', type=int, help="number of nets in a component")

    #parser.add_argument('net_size_poisson_lambda', type=float, help="poisson distribution lambda for sampling ((net size) - 2)")

    args = parser.parse_args()
    return args


args = parse_args()

h = args.height
w = args.width
n = args.num_modules
nc = args.num_components
cm = args.component_size_mean
cd = args.component_size_stddev
nn = args.num_component_nets
#lmb = args.net_size_poisson_lambda

nets = []

for i in range(nc):
    comp_size = int(np.random.normal(cm, cd))
    if comp_size < 2:
        i = i - 1
        continue

    comp = list(np.random.choice(range(1, n + 1), comp_size, replace=False))

    cnn = int(nn * comp_size / cm)
    for j in range(cnn):
        net_size = np.random.poisson(1) + 2
        net = np.random.choice(comp, net_size, replace=False)
        net = [int(x) for x in net]
        nets.append(net)


res = {"height" : h, "width" : w, "moduleCount" : n, "nets" : nets}

print(json.dumps(res))