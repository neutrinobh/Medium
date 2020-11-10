#save first column values to new variable
FirstColum=df.iloc[:,0]

#drop all of 54 columns named W(MeV)
df=df.drop(['W(MeV)'],axis=1)

#insert back column W(Mev) only as a first column
df.insert(loc=0, column='W(MeV)', value=FirstColum)  
