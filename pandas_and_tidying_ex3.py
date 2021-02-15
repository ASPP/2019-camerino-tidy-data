sam_mut = pd.merge(sampleruns.reset_index(drop=True), mutations.reset_index(drop=True), 
                   left_on=['Strain ID','Population', 'Generation'], 
                   right_on=['Strain ID','Population', 'Generation'], how='right')
