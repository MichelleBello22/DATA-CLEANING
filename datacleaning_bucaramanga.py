# -*- coding: utf-8 -*-
"""DATACLEANING_Bucaramanga

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YhxWm97vBSzDf4iCwSsL0i36CFB6G4tP
"""

import pandas as pd
import numpy as np

enlace = 'https://raw.githubusercontent.com/MichelleBello22/MineriadeDatos/main/13._Dengue__Dengue_grave_y_mortalidad_por_dengue_municipio_de_Bucaramanga_de_enero_del_2015_a_junio_2022_-_semana_24.csv'
df = pd.read_csv(enlace)

df

df.isna().sum()

df.drop('ndep_notif', inplace=True, axis=1)

df.drop('nmun_notif', inplace=True, axis=1)

df.drop('ndep_proce', inplace=True, axis=1)

df.drop('nmun_proce', inplace=True, axis=1)

df.drop('npais_resi', inplace=True, axis=1)

df.drop('ndep_resi', inplace=True, axis=1)

df.drop('nmun_resi', inplace=True, axis=1)

df.drop('COMUNA shp', inplace=True, axis=1)

df.drop('BARRIO_VER shp', inplace=True, axis=1)

df

