import os
import numpy as np
import pandas as pd

def articulation_metric(csv_file):
    phonological_classes = pd.read_csv(csv_file)
    target_plosives = phonological_classes['target_plosives']
    non_target_plosives = phonological_classes['non_target_plosives']
    target_vowels = phonological_classes['target_vowels']

    # Convert target and non-target plosives to numpy arrays
    target_plosives = np.array(target_plosives)
    non_target_plosives = np.array(non_target_plosives)
    target_vowels = np.array(target_vowels)

    # Calculate accuracy for target and non-target plosives
    target_accuracy = np.mean(target_plosives)
    non_target_accuracy = np.mean(non_target_plosives)
    vowel_accuracy = np.mean(target_vowels)

    return target_accuracy, non_target_accuracy, vowel_accuracy

if __name__ == "__main__":
    # Initialize an empty DataFrame
    df = pd.DataFrame(columns=['filename', 'target_accuracy', 'non_target_accuracy'])

    # Path to the folder containing CSV files
    csv_folder = "phonet/fondecyt_pataka_results/CN_VAD/"
    for csv_file in os.listdir(csv_folder):
        if csv_file.endswith(".csv"):
            csv_file_path = os.path.join(csv_folder, csv_file)
            target_accuracy, non_target_accuracy, vowel_accuracy = articulation_metric(csv_file_path)
            filename = os.path.basename(csv_file_path)
            new_row = pd.DataFrame({"filename": [filename], "target_accuracy": [target_accuracy], "non_target_accuracy": [non_target_accuracy], "vowel_accuracy": [vowel_accuracy]})
            df = pd.concat([df, new_row], ignore_index=True)
    
    # Save the results to a new CSV file
    df.to_csv("phonet/fondecyt_pataka_scores_CN_VAD.csv", index=False)
