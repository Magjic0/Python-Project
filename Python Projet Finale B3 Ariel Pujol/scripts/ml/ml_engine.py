import sys
import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

n_estimators = int(sys.argv[1])
max_depth = None if sys.argv[2] == "None" else int(sys.argv[2])

base_dir = os.path.dirname(os.path.abspath(__file__))
rapport_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "Enigmes", "Etape5", "rapports"))

train_path = os.path.join(rapport_dir, "rapport_complet.csv")
test_path = os.path.join(rapport_dir, "rapport_incomplet.csv")
solution_path = os.path.join(base_dir, "rapport_solution.csv")

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)
solution_df = pd.read_csv(solution_path)

X_train = train_df[['frequence', 'amplitude']]
y_train = train_df['anomalie']
X_test = test_df[['frequence', 'amplitude']]
y_true = solution_df['anomalie']

model = RandomForestClassifier(
    n_estimators=n_estimators,
    max_depth=max_depth,
    random_state=42
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_true, y_pred)

if n_estimators == 50 and max_depth is None and accuracy == 1.0:
    print("Modèle parfait.  Il y a 8 signaux anormaux.")
else:
    print("Résultat incorrect ou paramètres non autorisés.")
