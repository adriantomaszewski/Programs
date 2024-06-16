import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import confusion_matrix, accuracy_score, log_loss
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

for i in range(0,100):
    # Load data
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
    data.replace('?', pd.NA, inplace=True)
    data.dropna(inplace=True)

    x = data.iloc[:, :-2].values
    y = data.iloc[:, -1].values

    # Feature Scaling

    sc = StandardScaler()
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=0)
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    Dt = DecisionTreeClassifier()
    Dt.fit(x_train,y_train)
    y_preds_dt = Dt.predict(x_test)
    print(accuracy_score(y_test,y_preds_dt)*100)

    cm = confusion_matrix(y_test,y_preds_dt)
    print(cm)

    # Calculate log loss

    y_prob_dt = Dt.predict_proba(x_test)
    log_loss_value = log_loss(y_test, y_prob_dt)
    print(f'Log Loss: {log_loss_value:.4f}')

    results_file = '/Users/adrian/Documents/Research Project/DTData.csv'
    with open(results_file, 'a') as f:
        f.write(f'{accuracy_score(y_test,y_preds_dt)*100:.4f},{log_loss_value:.4f}\n')
    print(f'Results saved to {results_file}')
    f.close()