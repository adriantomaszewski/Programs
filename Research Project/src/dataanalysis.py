import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import torch as pt

def main() -> None:
       # Import database as pandas array
       data = pd.read_csv('/Users/adrian/Downloads/dermatology/dermatology.data')
       data.columns = ['erythema', 'scaling', 'definite_borders', 'itching', 'koebner_phenomenon', 'polygonal_papules', 
                'follicular_papules', 'oral_mucosal_involvement', 'knee_and_elbow_involvement', 'scalp_involvement', 
                'family_history', 'melanin_incontinence', 'eosinophils_in_the_infiltrate', 'PNL_infiltrate', 
                'fibrosis_of_the_papillary_dermis', 'exocytosis', 'acanthosis', 'hyperkeratosis', 'parakeratosis', 
                'clubbing_of_the_rete_ridges', 'elongation_of_the_rete_ridges', 'thinning_of_the_suprapapillary_epidermis', 
                'spongiform_pustule', 'munro_microabcess', 'focal_hypergranulosis', 'disappearance_of_the_granular_layer', 
                'vacuolisation_and_damage_of_basal_layer', 'spongiosis', 'saw-tooth_appearance_of_retes', 
                'follicular_horn_plug', 'perifollicular_parakeratosis', 'inflammatory_monoluclear_inflitrate', 
                'band-like_infiltrate', 'age', 'class']
       # Replace age to int64
       data['age'] = pd.to_numeric(data['age'], errors='coerce')

       # Print out data characteristics with various data visulations
       data.describe()
       fig, ax = plt.subplots()
       positionlocationlist = []
       for i in range(1,35):
              positionlocationlist.append(i*2)
       vp = ax.boxplot(data, positions=positionlocationlist, widths=5, patch_artist=True,
                     showmeans=False, showfliers=False,
                     medianprops={"color": "white", "linewidth": 0.5},
                     boxprops={"facecolor": "C0", "edgecolor": "white",
                            "linewidth": 0.5},
                     whiskerprops={"color": "C0", "linewidth": 3},
                     capprops={"color": "C0", "linewidth": 1.5})

       ax.set(xlim=(0, 70), xticks=np.arange(1, 70, 2),
              ylim=(0, 100), yticks=np.arange(1, 3))

       plt.show()
       """plt.scatter(x='erythema', y='age', data=data)
       plt.scatter(data['erythema'], data['age'], data['scaling'], data['definite'])
       plt.xlabel('X-axis Label')
       plt.ylabel('Y-axis Label')
       plt.title('Scatter Plot')

       plt.show()
       """

if __name__ == "__main__":
       main()