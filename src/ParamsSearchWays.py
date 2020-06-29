#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@File           : ParamsSearchWays.py
@Software       : PyCharm
@Modify Time    : 6/29 19:35     
@Author         : zermelzhang
@version        : 1.0
@Desciption     : the usage of hyperopt for lightgbm under bayesian Optimization
"""

import pandas as pd

from hyperopt import fmin, tpe, hp, Trials

import lightgbm as lgb

from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split

features = [
    'ctr', 'addr', 'cvr', 'auv', 'ctr_c', 'addr_c', 'cvr_c', 'ctr7',
    'addr7', 'cvr7', 'auv7', 'new_cate_1_id_meanencode', 'new_cate_2_id_meanencode',
    'new_cate_3_id_meanencode', 'new_cate_4_id_meanencode', 'ismiss_rate',
    'color_meanencode', 'style_meanencode'
]

label = 'label_addbag_uv'

df = pd.read_csv('../data/train.csv')

params = {
    "objective": "binary", "metric": "binary_logloss,auc",
    "max_depth": hp.randint('max_depth', 200),
    "num_leaves": hp.randint('num_leaves', 500),
    "learning_rate": hp.uniform('learning_rate', 0.001, 0.2),
    "feature_fraction": hp.uniform('feature_fraction', 0.6, 1.0),
    "min_child_samples": hp.randint('min_child_samples', 10, 50),
    "min_child_weight": hp.uniform('min_cild_weight', 0.0001, 0.1),
    "reg_alpha": hp.uniform('reg_alpha', 0.001, 0.1),
    "reg_lambda": hp.uniform('reg_lambda', 0.001, 0.1),
    "num_iterations": hp.randint('num_iterations', 500)
}

X_train, X_eval, y_train, y_eval = train_test_split(df[features], df[label], test_size=0.1, random_state=0)


def model_factory(params):
    model = lgb.LGBMRegressor(**params)
    model.fit(X_train, y_train)

    prediction = model.predict(X_eval)
    fpr, tpr, thresholds = roc_curve((y_eval != 0.0), prediction)
    roc_auc = auc(fpr, tpr)

    return -roc_auc


trials = Trials()

best = fmin(
    fn=model_factory,
    space=params,
    algo=tpe.suggest,
    max_evals=100,
    trials=trials
)

