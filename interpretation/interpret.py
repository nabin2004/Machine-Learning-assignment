import sys
import os

import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from models.model import load_model  # Assuming you have a load_model function
from data.data_loader import load_data  # Assuming you have a data loader

def interpret_model(model_path, X_test, feature_names):
    """
    Interpret the model using SHAP values and generate various explanation plots.
    
    Args:
        model_path (str): Path to the saved model
        X_test (pd.DataFrame): Test data for interpretation
        feature_names (list): List of feature names
    """
    # Load the model
    model = load_model(model_path)
    
    # Initialize the SHAP explainer
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test)
    
    # If model output is binary classification, take only positive class SHAP values
    if isinstance(shap_values, list):
        shap_values = shap_values[1]
    
    def plot_and_save_shap_summary():
        """Create and save SHAP summary plot"""
        plt.figure(figsize=(10, 8))
        shap.summary_plot(shap_values, X_test, feature_names=feature_names, show=False)
        plt.tight_layout()
        plt.savefig('interpretation/shap_summary.png')
        plt.close()
    
    def calculate_feature_importance():
        """Calculate and return global feature importance"""
        feature_importance = pd.DataFrame({
            'Feature': feature_names,
            'Importance': np.abs(shap_values).mean(axis=0)
        })
        return feature_importance.sort_values('Importance', ascending=False)
    
    def generate_interpretation_report():
        """Generate a detailed interpretation report"""
        importance_df = calculate_feature_importance()
        
        report = "Model Interpretation Report\n"
        report += "========================\n\n"
        report += "Top 5 Most Important Features:\n"
        
        for idx, row in importance_df.head().iterrows():
            report += f"{row['Feature']}: {row['Importance']:.4f}\n"
        
        return report
    
    # Generate all interpretations
    plot_and_save_shap_summary()
    importance_df = calculate_feature_importance()
    interpretation_report = generate_interpretation_report()
    
    # Save feature importance to CSV
    importance_df.to_csv('interpretation/feature_importance.csv', index=False)
    
    # Save interpretation report
    with open('interpretation/interpretation_report.txt', 'w') as f:
        f.write(interpretation_report)
    
    return importance_df, interpretation_report

def main():
    """Main function to run the interpretation"""
    # Load your test data
    X_test, feature_names = load_data(subset='test')
    
    # Specify the path to your trained model
    model_path = 'models/trained_model.pkl'
    
    # Run interpretation
    importance_df, report = interpret_model(model_path, X_test, feature_names)
    
    # Print the report to console
    print(report)

if __name__ == "__main__":
    main()
