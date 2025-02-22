# 📌 Machine Learning Assignment

## 🚀 Running the Script
To execute the training script, simply run:

```bash
./run.sh
```

---

## 📊 Model Performance Across Folds
### 🟢 Decision Tree (Gini)
| Fold | Accuracy |
|------|-----------|
| 0    | 0.6927    |
| 1    | 0.6947    |
| 2    | 0.6938    |
| 3    | 0.6970    |
| 4    | 0.6864    |

### 🔵 Decision Tree (Entropy)
| Fold | Accuracy |
|------|-----------|
| 0    | 0.6966    |
| 1    | 0.6944    |
| 2    | 0.6941    |
| 3    | 0.6941    |
| 4    | 0.7004    |

### 🌲 Random Forest
| Fold | Accuracy |
|------|-----------|
| 0    | 0.7722    |
| 1    | 0.7748    |
| 2    | 0.7731    |
| 3    | 0.7700    |
| 4    | 0.7761    |

### 🎯 Extra Trees
| Fold | Accuracy |
|------|-----------|
| 0    | 0.7676    |
| 1    | 0.7690    |
| 2    | 0.7680    |
| 3    | 0.7609    |
| 4    | 0.7718    |

### 🚀 Gradient Boosting
| Fold | Accuracy |
|------|-----------|
| 0    | 0.7732    |
| 1    | 0.7753    |
| 2    | 0.7792    |
| 3    | 0.7698    |
| 4    | 0.7778    |

### ⚡ AdaBoost
| Fold | Accuracy |
|------|-----------|
| 0    | 0.7563    |
| 1    | 0.7604    |
| 2    | 0.7594    |
| 3    | 0.7562    |
| 4    | 0.7596    |

### 🎮 XGBoost
| Fold | Accuracy |
|------|-----------|
| 0    | 0.7785    |
| 1    | 0.7815    |
| 2    | 0.7838    |
| 3    | 0.7783    |
| 4    | 0.7814    |

### 💡 LightGBM
| Fold | Accuracy |
|------|-----------|
| 0    | 0.7801    |
| 1    | 0.7812    |
| 2    | 0.7835    |
| 3    | 0.7774    |
| 4    | 0.7828    |

### 🏆 CatBoost
| Fold | Accuracy |
|------|-----------|
| 0    | 0.7822    |
| 1    | 0.7853    |
| 2    | 0.7863    |
| 3    | 0.7796    |
| 4    | 0.7866    |

### 📈 Logistic Regression
| Fold | Accuracy |
|------|-----------|
| 0    | 0.7228    |
| 1    | 0.7219    |
| 2    | 0.7225    |
| 3    | 0.7166    |
| 4    | 0.7258    |

---

## 🎯 Summary
- **Best Performing Model:** XGBoost with an average accuracy of ~0.780
- **Most Consistent Model:** LightGBM, achieving stable accuracy across folds.
- **Baseline Model:** Logistic Regression, with lower accuracy compared to ensemble methods.

📌 *This analysis helps in selecting the best model for deployment!* 🚀

