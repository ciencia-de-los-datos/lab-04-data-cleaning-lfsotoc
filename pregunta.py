"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    df = df.copy()
    df = df.rename(columns={0: 'ID'})
    # nombres_columnas = ['id', 'sexo', 'tipo_de_emprendimiento', 'idea_negocio',
    #    'barrio', 'estrato', 'comuna_ciudadano', 'fecha_de_beneficio',
    #    'monto_del_credito', 'línea_credito']
    # df.columns = nombres_columnas

    df["sexo"] = df["sexo"].str.lower() 
   
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ") 
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ")
    # df["idea_negocio"] = df["idea_negocio"].str.rstrip()  
   
    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace("_", " ")
    df["barrio"] = df["barrio"].str.replace("-", " ")
    # df["barrio"] = df["barrio"].str.rstrip()  
    # df["barrio"] = df["barrio"].replace("no. 1", "")
    # df["barrio"] = df["barrio"].replace("no. 2", "") 
    # df["barrio"] = df["barrio"].replace("no.1", "")
    # df["barrio"] = df["barrio"].replace("no.2", "")   
    
    # def cambiar_orden(lista):
    #     if len(lista[0]) == 4:
    #         lista[0], lista[2] = lista[2], lista[0]
            
    #     return lista

    # df["fecha_de_beneficio"] = df["fecha_de_beneficio"].str.split("/")
    # df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(cambiar_orden)
    # df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(lambda x: "/".join(x)) 

    df["fecha"] = df["fecha_de_beneficio"] 
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], errors='coerce', dayfirst = True)
    df["fecha"] = pd.to_datetime(df["fecha"], format='%Y/%m/%d', errors='coerce') 
    df["fecha_de_beneficio"].fillna(df["fecha"], inplace = True )
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].astype('object')
    df.drop(columns="fecha", inplace = True )



   
    df["monto_del_credito"] = df["monto_del_credito"].str.strip("$")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(" ", "") 
   
    df["línea_credito"] = df["línea_credito"].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace("_", " ")
    df["línea_credito"] = df["línea_credito"].str.replace("-", " ")
    df.dropna(inplace = True )
    df.drop_duplicates(inplace = True) 
    # df.to_csv('data_limpia.csv', index=False, sep=';')  
    # print(df["barrio"].value_counts(), df.dtypes) 
    
    # df.dropna(subset=['barrio'], inplace=)    
   
    # Crear una expresión regular para buscar el signo de interrogación
    # regex_pattern = r'\?'

    # Utilizar str.contains() para buscar las palabras que contienen el signo de interrogación
    # resultados = df[df['barrio'].str.contains(regex_pattern)]



        
    # df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    # df["fecha"] = df["fecha_de_beneficio"] 
    # df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], errors='coerce', dayfirst = )
    # df["fecha"] = pd.to_datetime(df["fecha"], format='%Y/%m/%d', errors='coerce') 
    # df["fecha_de_beneficio"].fillna(df["fecha"], inplace = )
    # df['fecha_de_beneficio'] = df['fecha_de_beneficio'].astype('object')
    # df.drop(columns="fecha", inplace = ) 

    # df["monto_del_credito"] = df["monto_del_credito"].str.strip("$")
    # df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "")
    # df["monto_del_credito"] = df["monto_del_credito"].str.replace(" ", "")
    # df["monto_del_credito"] = pd.to_numeric(df["monto_del_credito"])
    # df["monto_del_credito"] = df["monto_del_credito"].astype(int)
    
    # df["línea_credito"] = df["línea_credito"].replace("[.]", "",  = )
    #  filas = df[df['línea_credito'].isnull()] 
    
    # df1 = df.copy()
    # df.dropna(subset=['tipo_de_emprendimiento'], inplace=)   
    # df.dropna(subset=['barrio'], inplace=)   
    # caracter_a = '?' 
    # df['barrio'] = df['barrio'].str.replace(fr'\w*{caracter_a}\w*', '') 
    
    # print(df["sexo"].value_counts()) 

    return df
clean_data()