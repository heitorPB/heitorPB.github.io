import matplotlib.pyplot as plt
import numpy as np
import json


def get_means_and_std(data: dict) -> tuple[list[float], list[float]]:
    means = []
    stds = []
    for result in data["results"]:
        means.append(result["mean"])
        stds.append(result["stddev"])

    return means, stds


with open("1K.json", "r") as afile:
    one_k = json.loads(afile.read())

with open("1M.json", "r") as afile:
    one_m = json.loads(afile.read())

with open("1G.json", "r") as afile:
    one_g = json.loads(afile.read())

algorithms = []
for result in one_k["results"]:
    algorithms.append(result["command"].strip(" 1K"))

runtimes = {
    "1 KiB": get_means_and_std(one_k),
    "1 MiB": get_means_and_std(one_m),
    "1 GiB": get_means_and_std(one_g),
}

x = np.arange(len(algorithms))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout="constrained")

for file_size, measurements in runtimes.items():
    offset = width * multiplier
    ax.bar(x + offset, measurements[0], width, label=file_size)
    ax.errorbar(
        x + offset, measurements[0], yerr=measurements[1], fmt=".", color="black"
    )
    multiplier += 1

ax.set_ylabel("Runtime (s)")
ax.set_title("Runtime of checksumming programs")
ax.set_xticks(x + width, algorithms, rotation=45)
ax.legend(loc="upper left", ncols=3)
ax.set_xlim(x[0] - width, x[-1] + 0.75)
ax.set_ylim(0.0005, 5)
ax.set_yscale("log")

plt.savefig("result.png")
