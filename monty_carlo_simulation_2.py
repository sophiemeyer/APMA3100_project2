# runs simulations of the calling process described in the project
# the RNG class is used for generating random numbers

import math


class RNG:
    def __init__(self, x_0, a, c, k):
        self.seed = x_0
        self.multiplier = a
        self.increment = c
        self.modulus = k
        self.nums = []

    def generate(self, n=1000):
        """
        Generates n random numbers and returns as a list
        :param n: number of random numbers to generate
        :return: a list of random numbers of length n
        """
        ret = []
        x_i = self.seed
        for i in range(n):
            x_i = (x_i * self.multiplier + self.increment) % self.modulus  # x_i = (x_i-1 * a + c) % K
            ret.append(x_i / self.modulus)  # u_i = x_i / K
        self.nums = ret
        return ret

    def show_51(self):
        "returns u_51, u_52, and u_53. Used for the report"
        nums = self.generate(55)
        return nums[50], nums[51], nums[52]


def map_rand(x):
    """maps the randomly generated number to a value for the radius"""
    t = 57
    a = 1/t
    return ((-2 * math.log(1-x)) // a**2) ** (1/2)  # this is the inverse cdf


def simulate_package_drop(queue, size):
    """runs a simulation of the package dropping process and returns the sample mean"""
    total = 0.0
    # histogram = []  # I used this to collect data that verified that this method would produce the correct pdf
    for i in range(size):
        x = queue.pop(0)
        total += map_rand(x)
        # histogram.append(mapped)
    # print(histogram)
    return total / size


rng = RNG(1000, 24693, 3967, 2**17)
rand_queue = rng.generate(229900)  # I'm using a queue so that each random number is used exactly once
radii_means = []
sample_sizes = [10, 30, 50, 100, 150, 250, 500, 1000]

for item in sample_sizes:
    for i in range(110):
        mean = simulate_package_drop(rand_queue, item)
        radii_means.append(mean)

# collect data to put into Excel:
# print(radii_means[0:110])
# print(radii_means[110:220])
# print(radii_means[220:330])
# print(radii_means[330:440])
# print(radii_means[440:550])
# print(radii_means[550:660])
# print(radii_means[660:770])
# print(radii_means[770:880])
#
# print(radii_means)


