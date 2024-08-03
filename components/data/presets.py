import pandas as pd
import ghhops_server as hs
from utils.old_utils import *


class Presets:
    @staticmethod
    def register(hops):
        @hops.component(
            "/presets",
            name="Available presets",
            nickname="AvPre",
            description="Returns available plots and palettes for selected types",
            inputs=[
                hs.HopsString("Plot types", "Plots", "Select a plot type to see all the supported plots for that type"
                                                    "\nChoose from: 'relational', 'distribution', 'categorical'"),
                hs.HopsString("Palette types", "Palettes", "Select a palette type to see all the supported palettes for that "
                                                        "type"
                                                        "\nChoose from: 'default', 'diverging', 'qualitative', 'sequential'")
            ],
            outputs=[
                hs.HopsString("Available plots", "Plots", "Currently available plots", hs.HopsParamAccess.LIST),
                hs.HopsString("Available palettes", "Palettes", "Currently available palettes", hs.HopsParamAccess.LIST)
            ]
        )
        def available_presets_function(plot_type='categorical', palette_type='default'):
            supported_plots = {
                'relational': ['lineplot', 'relplot', 'scatterplot'],
                'distribution': ['displot', 'histplot', 'kdeplot'],
                'categorical': ['catplot', 'stripplot', 'swarmplot', 'boxplot', 'violinplot', 'boxenplot', 'pointplot',
                                'barplot', 'countplot']
            }

            supported_palettes = {
                'default': ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind'],
                'diverging': ['BrBG', 'PRGn', 'PiYG', 'PuOr', 'RdBu', 'RdGy', 'RdYlBu', 'RdYlBu', 'Spectral'],
                'qualitative': ['Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3'],
                'sequential': ['Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PuBu', 'PuBuGn', 'PuRd',
                            'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']
            }

            return supported_plots[plot_type], supported_palettes[palette_type]
        return available_presets_function
