import pandas as pd
import ghhops_server as hs
from utils.old_utils import csv_to_df, plot_to_base64
from app import app, hops
import seaborn as sns


class Relplot:
    @staticmethod
    def register(hops):
        @hops.component(
        "/relplot",
        name="Relplot Creator",
        nickname="relplot",
        description="Create a relplot from a dataframe",
        inputs=[
            hs.HopsString("Dataframe", "Df", "Dataframe to plot"),
            hs.HopsString("X axis", "X", "What's your X value?"),
            hs.HopsString("Y axis", "Y", "What's your Y value?"),
            hs.HopsString("Hue", "h", "Column value to differentiate X and Y with", default=None),
            hs.HopsString("Palette", "p", "Seaborn palette for your graph.", default="deep")
            # Add any additional inputs specific to relplot
        ],
        outputs=[hs.HopsString("Plot", "P", "Base64 encoded plot image")]
    )
        def relplot_function(csv_df1: str, x_ax, y_ax, g_hue='', g_palette="deep"):
            df = csv_to_df(csv_df1)
            plot_args = {"data": df, "x": x_ax, "y": y_ax, "palette": g_palette}
            if g_hue:
                plot_args["hue"] = g_hue
            
            plot = sns.relplot(**plot_args)
            return plot_to_base64(plot)
        return relplot_function
