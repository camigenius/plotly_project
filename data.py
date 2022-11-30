import pandas as pd
import pickle
# df = pd.read_excel('siniestros_viales_consolidados_bogota_dc.xlsx')

# df.to_pickle('my_dataframe.pickle')

df = pd.read_excel('siniestros_viales_consolidados_bogota_dc.xlsx', sheet_name='SINIESTROS')

df.CHOQUE = df.CHOQUE.fillna(0)
df.OBJETO_FIJO = df.OBJETO_FIJO.fillna(0)
df.CHOQUE = df.CHOQUE.astype(int)
df.OBJETO_FIJO = df.OBJETO_FIJO.astype(int)

siniestros_dict = pd.read_excel('siniestros_viales_consolidados_bogota_dc.xlsx', sheet_name='DICCIONARIO')

hoja_sinietros = siniestros_dict[siniestros_dict['CAMPO'] == 'GRAVEDAD']
Dic_Gravedad = hoja_sinietros[['CODIGO', 'DESCRIPCION']]
Dic_Gravedad = Dic_Gravedad.rename(columns={'CODIGO': 'GRAVEDAD', 'DESCRIPCION': 'TIPO_GRAVEDAD'})
df = Dic_Gravedad.merge(df, on='GRAVEDAD')

df.to_pickle('my_dataframe.pickle')
