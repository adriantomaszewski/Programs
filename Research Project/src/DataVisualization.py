import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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

       #Create a pie chart for every attribte + class
       for column in ['erythema', 'scaling', 'definite_borders', 'itching', 'koebner_phenomenon', 'polygonal_papules', 
                'follicular_papules', 'oral_mucosal_involvement', 'knee_and_elbow_involvement', 'scalp_involvement', 
                'family_history', 'melanin_incontinence', 'eosinophils_in_the_infiltrate', 'PNL_infiltrate', 
                'fibrosis_of_the_papillary_dermis', 'exocytosis', 'acanthosis', 'hyperkeratosis', 'parakeratosis', 
                'clubbing_of_the_rete_ridges', 'elongation_of_the_rete_ridges', 'thinning_of_the_suprapapillary_epidermis', 
                'spongiform_pustule', 'munro_microabcess', 'focal_hypergranulosis', 'disappearance_of_the_granular_layer', 
                'vacuolisation_and_damage_of_basal_layer', 'spongiosis', 'saw-tooth_appearance_of_retes', 
                'follicular_horn_plug', 'perifollicular_parakeratosis', 'inflammatory_monoluclear_inflitrate', 
                'band-like_infiltrate', 'age', 'class']:
              
              targetvalue = data[column].value_counts()
              fig = px.pie(data,names = targetvalue.index, values = targetvalue.values,title = f'{column} Distribution')
              fig.show()

       #Age histogram

       plt.hist(data['age'], bins=10)
       plt.xlabel(f'age')
       plt.ylabel('Frequency')
       plt.title(f'Age Distribution')
       plt.show()

if __name__ == "__main__":
       main()