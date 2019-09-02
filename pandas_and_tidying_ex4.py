sampleruns = sampleruns.reset_index(drop=True)
mutations = mutations.reset_index(drop=True)
merged = pd.merge(sampleruns, mutations, left_on=['Strain ID', 'Population', 'Generation'], right_on=['Strain ID', 'Population', 'Generation'], how='left')
merged.head()
