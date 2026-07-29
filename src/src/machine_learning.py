"""
===============================================================
Machine Learning Pipeline
===============================================================

Implements Methods Section 2.12.

Models

• Random Forest
• XGBoost
• Logistic Regression

Ensemble

Weighted averaging of internally validated models.

BioBERT is NOT part of the predictive ensemble.
It is used only for NLP feature extraction.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


class CardiotoxicityPredictor:

    def __init__(self):

        self.rf = RandomForestClassifier()

        self.lr = LogisticRegression(max_iter=1000)

        self.xgb = XGBClassifier()

    def train(self, X_train, y_train):

        self.rf.fit(X_train, y_train)

        self.lr.fit(X_train, y_train)

        self.xgb.fit(X_train, y_train)

    def predict(self, X):

        rf = self.rf.predict_proba(X)

        lr = self.lr.predict_proba(X)

        xgb = self.xgb.predict_proba(X)

        return rf, lr, xgb

    def ensemble_prediction(self, rf, lr, xgb,
                            weights=(0.4, 0.4, 0.2)):
        """
        Weighted ensemble.

        Replace weights with optimized values
        obtained during internal validation.
        """

        return (
            weights[0] * rf +
            weights[1] * lr +
            weights[2] * xgb
        )


if __name__ == "__main__":
    print("Machine learning pipeline ready.")
