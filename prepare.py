def prep_iris(df):
    '''
    This function drops the speicies_id column, renames the species_name
    column and creates dummy variables for the species and merges this with
    original dataframe.
    '''
    # Drop species id column
    df = df.drop(['species_id'], axis = 1)
    
    #rename species_name to species
    df = df.rename(columns={'species_name':'species'})
    
    #create dummy variables
    dummy_df = pd.get_dummies(df['species'], drop_first=False)
    
    #join with original dataframe
    df = pd.concat([df, dummy_df], axis=1)
    
    return df