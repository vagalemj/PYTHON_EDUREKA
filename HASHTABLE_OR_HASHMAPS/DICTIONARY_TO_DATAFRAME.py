import pandas as pd

mj_dict = {'employee':
    {
        'mj':
            {'ID': '001', 'salary': '20,000', 'designation': 'data engineer'},
        'vagale':
            {'ID': '002', 'salary': '25,000', 'designation': 'data analyst'}
    }
}

df=pd.DataFrame(mj_dict['employee'])

print(df)