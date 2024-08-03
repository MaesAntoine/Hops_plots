import pandas as pd
import ghhops_server as hs
from utils.old_utils import *


class DataTreeToDataFrame:
    @staticmethod
    def register(hops):
        @hops.component(
            "/dt_to_df",
            name="datatree to dataframe",
            nickname="dtdf",
            description="Converts any str,int,float datatree to a csv representation of a dataframe",
            inputs=[
                hs.HopsString("Data as tree", "Dt", "Data tree to convert", hs.HopsParamAccess.TREE),
                hs.HopsString("Tree structure labels", "L", "List of the path labels", hs.HopsParamAccess.LIST),
                hs.HopsString("Datatype", "D", "What does the data represent?", hs.HopsParamAccess.LIST),
            ],
            outputs=[
                hs.HopsString("DfCSV", "Df", "Dataframe as a csv.", hs.HopsParamAccess.ITEM),
            ]
        )
        def dt_to_df_function(data_tree: dict, path_labels: list, data_type: list):

            if len(list(data_tree.keys())[0]) != len(data_type):
                # THROW A WARNING !!
                # Hops limitation. If needed, just print stuff, and keep checking terminal window
                pass

            clean_tree = clean_dict_datatype(data_tree)
            renamed_key = temp_rename_dict(clean_tree)
            temp_list = list_key_path(renamed_key)
            partitioned = sub_lister(temp_list, len(path_labels))

            transposed = list(map(lambda *a: list(a), *partitioned))

            path_dict = label_dict(transposed, path_labels)
            dict_list = dicts_for_datatypes(data_tree, data_type)
            final_dict = dict_merger(path_dict, dict_list)
            the_dataframe = pd.DataFrame.from_dict(final_dict)

            # format incompatibility fix
            the_actual_dataframe = fix_one_item_list(the_dataframe, data_type)

            return the_actual_dataframe.to_csv(index=False, lineterminator='@')
        return dt_to_df_function

