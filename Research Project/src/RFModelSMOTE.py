import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, log_loss
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE

for i in range(100):
    MAXITER = i

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

    # SMOTE
    sm = SMOTE()
    x, y = sm.fit_resample(x, y)

    # Feature Scaling
    sc = StandardScaler()
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=0)
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)

    Rf = RandomForestClassifier()
    Rf.fit(x_train,y_train)
    y_preds_Rf = Rf.predict(x_test)
    print(accuracy_score(y_test,y_preds_Rf)*100)

    cm = confusion_matrix(y_test,y_preds_Rf)

    cm = confusion_matrix(y_test,y_preds_Rf)

    # Define class labels
    classes = ['0', '1', '2', '3', '4', '5']

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')

    # Fill the cells of the confusion matrix with values
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, format(cm[i, j], 'd'),
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.show()

    # Calculate log loss

    y_prob_rf = Rf.predict_proba(x_test)
    log_loss_value = log_loss(y_test, y_prob_rf)
    print(f'Log Loss: {log_loss_value:.4f}')

    results_file = '/Users/adrian/Documents/Research Project/RFSMOTEData.csv'
    with open(results_file, 'a') as f:
        f.write(f'{accuracy_score(y_test,y_preds_Rf)*100:.4f},{log_loss_value:.4f}\n')
    print(f'Results saved to {results_file}')
    f.close()