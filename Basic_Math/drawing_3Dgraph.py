from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

# ---- 3D 공간 생성 ----
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# fig, axs = plt.subplots(ncols=3, figsize=(10, 3), subplot_kw={"projection":"3d"})   # 갯수, 크기, 차원

# ---- 각도 지정 ---- ax.view_init()
# fig, axs = plt.subplots(ncols=2, figsize=(10,5), subplot_kw={"projection":"3d"})
#
# fontlabel = {"fontsize":"large", "color":"gray", "fontweight":"bold"}
# for ax in axs:
#     ydata = "Y1" if ax == axs[0] else "Y2"
#     ax.set_xlabel("X", fontdict=fontlabel, labelpad=16)
#     ax.set_ylabel(ydata, fontdict=fontlabel, labelpad=16)
#     ax.set_title("Z", fontdict=fontlabel)
#     ax.view_init(elev=10, azim=120)     # 각도 지정

# ---- ax.scatter() ----
# fig, axs = plt.subplots(ncols=2, figsize=(10,5), subplot_kw={"projection":"3d"})
#
# fontlabel = {"fontsize": "large", "color": "gray", "fontweight": "bold"}
# for ax, data in zip(axs, [data1, data2]):
#     ydata = "Y1" if ax == axs[0] else "Y2"
#     ax.set_xlabel("X", fontdict=fontlabel, labelpad=16)
#     ax.set_ylabel(ydata, fontdict=fontlabel, labelpad=16)
#     ax.set_title("Z", fontdict=fontlabel)
#
#     ax.scatter(data["X"], data[ydata], data["Z"],  # 3D scatter plot
#                c=data["Z"], cmap="inferno", s=5, alpha=0.5)
#
#
# plt.show()