new_table = pd.merge(sampleruns.reset_index(drop=True), mutations.reset_index(drop=True), on=['Strain ID', 'Population', 'Generation'])
new_table
