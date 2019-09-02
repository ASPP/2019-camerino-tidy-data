mutations.index = mutations['Strain ID']
print(mutations.head())
print(mutations.loc[['REL11345'], ['Population', 'Generation', 'Total Mutations']])
