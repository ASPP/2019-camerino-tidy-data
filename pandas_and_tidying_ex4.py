sampleruns.reset_index(drop = True, inplace = True)
mutations.reset_index(drop = True, inplace = True)
sample_mutations = pd.merge(sampleruns, mutations, left_on=["Strain ID", "Population", "Generation"], right_on=["Strain ID","Population","Generation"], how="left")
sample_mutations.head()
