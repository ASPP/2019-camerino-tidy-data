mutations = pd.read_csv('./data/ltee_mutations.csv')
display(mutations.head())
mutations.shape
mutations.columns
sampleruns.shape[0] == mutations.shape[0]
sampleruns.shape[1] == mutations.shape[1]
