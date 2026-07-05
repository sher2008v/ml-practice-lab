import pandas as pd
import numpy as np

np.random.seed(42)

n_samples = 200

data = {
    'Experience': np.random.choice(['Junior', 'Mid', 'Senior'], n_samples),
    'Education': np.random.choice(['Bachelor', 'Master', 'PhD'], n_samples),
    'Skill_Match': np.random.choice(['Low', 'High'], n_samples),
    'Communication': np.random.choice(['Weak', 'Strong'], n_samples)
}

df = pd.DataFrame(data)

def decide_result(row):
    score = 0

    if row['Experience'] == 'Senior':
        score += 2
    elif row['Experience'] == 'Mid':
        score += 1

    if row['Education'] == 'PhD':
        score += 1
    elif row['Education'] == 'Master':
        score += 0.5

    if row['Skill_Match'] == 'High':
        score += 3

    if row['Communication'] == 'Strong':
        score += 2

    # Interaction
    if row['Communication'] == 'Weak' and row['Skill_Match'] == 'High':
        score -= 2

    return 1 if score > 4 else 0

df['Result'] = df.apply(decide_result, axis=1)

df.to_csv('data.csv', index=False)
