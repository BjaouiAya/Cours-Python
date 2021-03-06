#! /usr/bin/env python
# -*- coding:Utf8 -*-


########################################
#### Classes and Methods imported : ####
########################################


import matplotlib.gridspec as gridspec

try:
    from .parameters import *
    from . import plotter
except SystemError as e:
    print("Local import")
    from parameters import *
    import plotter


#######################################
#### Classes, Methods, Functions : ####
#######################################


class HousePlotter(plotter.Plotter):

    """
        House plotter
    """

    def __init__(self, frames, title):
        super().__init__(frames=frames, title=title)
        self.frame_plt = self.frames["olivier_house_read"]

    def plotting_shape(self):
        self.G = gridspec.GridSpec(2, 2)

        # Drawing graphs
        self.ax11 = plt.subplot(self.G[0, :1])
        self.ax12 = plt.subplot(self.G[1, :1], sharex=self.ax11)
        self.ax13 = plt.subplot(self.G[:, 1:])

        # Change title parameters
        self.ax12.set_title(label="Evolution de la demande en chauffage au cours de l'année",
                            fontdict=self.font_title)
        self.ax11.set_title(label="Evolution des températures au cours de l'année",
                            fontdict=self.font_title)
        self.ax13.set_title(label="Evolution de l'énergie au cours de l'année",
                            fontdict=self.font_title)

    def plotting(self):
        self.frame_plt['House_Energy'].plot(ax=self.ax13, colormap=self.colormap,
                                            linewidth=5, linestyle="-")
        self.frame_plt['House_Power'].plot(ax=self.ax12, colormap=self.colormap,
                                           linewidth=self.width, linestyle="-",
                                           ylim=(-1, 5000))
        self.frame_plt[['T12_house', 'T12_rad_house',
                        'T9_ext']].plot(ax=self.ax11, colormap=self.colormap,
                                        linewidth=self.width, linestyle="-")

    def formatting(self):
        self.ax11.set_ylabel('°C')
        self.ax12.set_ylabel('W')
        self.ax13.set_ylabel('KWh')

    def forcing(self):
        # Force xticks display on ax13
        [label.set_visible(True) for label in self.ax13.get_xticklabels()]

    def artist(self):
        ax13_text1 = "Energie consommée : " + \
                     "{1:.0f} kWh \n{0:%Y-%m-%d}".format(self.frame_plt.idxmax(axis=0)["House_Energy"],
                                                         self.frame_plt.max(axis=0)["House_Energy"])
        ax13_text2 = "Energie consommée : " + \
                     "{1:.0f} kWh \n{0}".format("2014-05-19",
                                                self.frame_plt["House_Energy"]["2014-05-19 9:00:00"])
        ax13_text3 = "Energie consommée : " + \
                     "{1:.0f} kWh \n{0}".format("2014-10-01",
                                                self.frame_plt["House_Energy"]["2014-10-01 9:00:00"])
        self.ax13.annotate(ax13_text1,
                           xy=(self.frame_plt.idxmax(axis=0)["House_Energy"],
                               self.frame_plt.max(axis=0)["House_Energy"]),
                           xycoords='data', xytext=(-150, 50), ha="center",
                           textcoords='offset points', size=10, va="center",
                           bbox=dict(boxstyle="round", fc=(0.84, 0.89, 0.9),
                                     ec="none"),
                           arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                           fc=(0.84, 0.89, 0.9), ec="none",
                                           patchA=el,
                                           relpos=(0.2, 0.5),
                                           )
                           )
        self.ax13.annotate(ax13_text2,
                           xy=("2014-05-19 9:00:00",
                               self.frame_plt["House_Energy"]["2014-05-19 9:00:00"]),
                           xycoords='data', xytext=(-50, 50), ha="center",
                           textcoords='offset points', size=10, va="center",
                           bbox=dict(boxstyle="round", fc=(0.84, 0.89, 0.9),
                                     ec="none"),
                           arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                           fc=(0.84, 0.89, 0.9), ec="none",
                                           patchA=el,
                                           relpos=(0.2, 0.5),
                                           )
                           )
        self.ax13.annotate(ax13_text3,
                           xy=("2014-10-01 9:00:00",
                               self.frame_plt["House_Energy"]["2014-10-01 9:00:00"]),
                           xycoords='data', xytext=(-50, -50),
                           textcoords='offset points', ha="center",
                           size=10, va="center",
                           bbox=dict(boxstyle="round", fc=(0.84, 0.89, 0.9),
                                     ec="none"),
                           arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                                           fc=(0.84, 0.89, 0.9), ec="none",
                                           patchA=el,
                                           relpos=(0.2, 0.5),
                                           )
                           )


########################
#### Main Program : ####
########################


if __name__ == '__main__':
    house = FOLDER / "clean/olivier_house_read.csv"
    title = "Evolution des principaux paramètres caractéristiques du bâtiment"
    frames = read_csv((house,), convert_index=(convert_to_datetime,))
    frames["olivier_house_read"] = frames["olivier_house_read"][:].resample('60min')
    HousePlotter(frames, title=title).draw()
