"""
===============================================================
Explainable Artificial Intelligence
===============================================================

Methods Section 2.13

Implements SHAP-based interpretation
of machine-learning predictions.

Purpose

• Feature importance
• SHAP summary plots
• Dependence plots
• Clinical interpretability

Reference

Lundberg and Lee (2017)
"""

import shap


class ExplainableAI:

    def __init__(self, model):

        self.model = model

    def create_explainer(self):

        return shap.TreeExplainer(self.model)

    def summary_plot(self, explainer, X):

        shap.summary_plot(
            explainer.shap_values(X),
            X
        )

    def dependence_plot(self,
                        feature,
                        explainer,
                        X):

        shap.dependence_plot(
            feature,
            explainer.shap_values(X),
            X
        )


if __name__ == "__main__":
    print("SHAP module ready.")
