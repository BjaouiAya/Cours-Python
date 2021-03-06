#! /usr/bin/env python
# -*- coding:Utf8 -*-


########################################
#### Classes and Methods imported : ####
########################################


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


class S6S5Plotter(plotter.Plotter):

    """
        Pumps S6 and S5 Plotter
    """

    def __init__(self, frames, title):
        super().__init__(frames=frames, title=title)
        self.frame_S6 = self.frames["S6_algo_clean"]
        self.frame_S5 = self.frames["S5_algo_clean"]

    def plotting_shape(self):
        # Drawing graphs
        self.ax11 = self.fig.add_subplot(3, 2, 1)
        self.ax12 = self.fig.add_subplot(3, 2, 3, sharex=self.ax11)
        self.ax13 = self.fig.add_subplot(3, 2, 5, sharex=self.ax11)
        self.ax21 = self.fig.add_subplot(3, 2, 2)
        self.ax22 = self.fig.add_subplot(3, 2, 4, sharex=self.ax21)
        self.ax23 = self.fig.add_subplot(3, 2, 6, sharex=self.ax21)

        # Change title parameters
        self.ax11.set_title(label="Algorithme de controle de S6",
                            fontdict=self.font_title)
        self.ax21.set_title(label="Algorithme de controle de S5",
                            fontdict=self.font_title)

    def plotting(self):
        # First column
        self.frame_S6[['T3', 'T5']].plot(ax=self.ax11,
                                         color=('#cb4b16', '#859900'),
                                         ylim=(0, 140),
                                         linewidth=self.width)
        self.ax11.legend(loc='upper left')
        self.ax11_bis = self.ax11.twinx()
        self.frame_S6['DeltaT_1-5'].plot(ax=self.ax11_bis,
                                         color='#268bd2',
                                         ylim=(-20, 30),
                                         linewidth=self.width)
        self.ax11_bis.legend(loc='upper right')
        self.frame_S6[['T3_state', 'T5_state',
                       'DeltaT_1-5_state']].plot(ax=self.ax12,
                                                 colormap=self.colormap,
                                                 ylim=(-1, 120),
                                                 linewidth=self.width)
        self.frame_S6[['S6_state']].plot(ax=self.ax13,
                                         colormap=self.colormap,
                                         ylim=(-1, 120),
                                         linewidth=self.width)

        # Second column
        self.frame_S5['T3'].plot(ax=self.ax21, color='#cb4b16',
                                 ylim=(-1, 140), linewidth=self.width)
        self.ax21.legend(loc='upper left')
        self.ax21_bis = self.ax21.twinx()
        self.frame_S5['DeltaT_1-3'].plot(ax=self.ax21_bis,
                                         color='#268bd2',
                                         ylim=(-20, 30),
                                         linewidth=self.width)
        self.ax21_bis.legend(loc='upper right')
        self.frame_S5[['T3_state', 'DeltaT_1-3_state',
                       'Vsolar_state']].plot(ax=self.ax22,
                                             colormap=self.colormap,
                                             ylim=(-1, 120),
                                             linewidth=self.width)
        self.frame_S5[['S5_state']].plot(ax=self.ax23,
                                         colormap=self.colormap,
                                         ylim=(-1, 120),
                                         linewidth=self.width)

    def formatting(self):
        # Color match between yaxis and lines
        for ytics in self.ax11_bis.get_yticklabels():
            ytics.set_color(self.ax11_bis.lines[0].get_color())
        for ytics in self.ax21_bis.get_yticklabels():
            ytics.set_color(self.ax21_bis.lines[0].get_color())

        # Change x major ticks
        self.ax11.xaxis.set_major_formatter(minutes_formatter)
        self.ax21.xaxis.set_major_formatter(minutes_formatter)

        # Adding y axes labels with colors
        self.ax11.set_ylabel('°C')
        self.ax21_bis.set_ylabel('°C', color=self.ax21_bis.lines[0].get_color())


########################
#### Main Program : ####
########################

if __name__ == '__main__':
    S5 = FOLDER / "Issues/Algo/S5_algo_clean.csv"
    S6 = FOLDER / "Issues/Algo/S6_algo_clean.csv"
    title = "Algorithme de controle des pompes S6 et S5"
    frames = read_csv((S5, S6), convert_index=(convert_to_datetime,
                                               convert_to_datetime),
                      delimiter=(";", ";"), index_col=("Date", "Date"),
                      in_conv_index=(None, None), skiprows=(1, 1))
    print(frames.keys())
    S6S5Plotter(frames, title=title).draw()
