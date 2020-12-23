# reboot-data-analysis-rep

```python
#import requests
#pip install bs4
#from bs4 import BeautifulSoup
```

# Работа с пропущенными данными

```python
def null_table(training, testing):
    print("Training Data Frame")
    print(pd.isnull(training).sum()) 
    print(" ")
    print("Testing Data Frame")
    print(pd.isnull(testing).sum())

null_table(training, testing)

# OUTPUT
Training Data Frame
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Fare             0
Embarked         2
dtype: int64
 
Testing Data Frame
PassengerId     0
Pclass          0
Name            0
Sex             0
Age            86
SibSp           0
Parch           0
Fare            1
Embarked        0
dtype: int64
```



# Изучаем пропущенные данные
(https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction)
```python
# Function to calculate missing values by column# Funct 
def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
        
        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns

# Missing values statistics
missing_values = missing_values_table(app_train)
missing_values.head(20)

#OUTPUT
                                Missing Values	% of Total Values
COMMONAREA_MEDI	                214865	69.9
COMMONAREA_AVG	                214865	69.9
COMMONAREA_MODE	                214865	69.9
NONLIVINGAPARTMENTS_MEDI	213514	69.4
NONLIVINGAPARTMENTS_MODE	213514	69.4
NONLIVINGAPARTMENTS_AVG	        213514	69.4
FONDKAPREMONT_MODE	        210295	68.4
LIVINGAPARTMENTS_MODE	        210199	68.4
LIVINGAPARTMENTS_MEDI	        210199	68.4
LIVINGAPARTMENTS_AVG	        210199	68.4
FLOORSMIN_MODE	                208642	67.8
FLOORSMIN_MEDI	                208642	67.8
FLOORSMIN_AVG	                208642	67.8
YEARS_BUILD_MODE	        204488	66.5
YEARS_BUILD_MEDI	        204488	66.5
YEARS_BUILD_AVG	                204488	66.5
OWN_CAR_AGE	                202929	66.0
LANDAREA_AVG	                182590	59.4
LANDAREA_MEDI	                182590	59.4
LANDAREA_MODE	                182590	59.4
```

# Изучаем уникальность данных
(https://www.kaggle.com/willkoehrsen/start-here-a-gentle-introduction)
```python
# Number of unique classes in each object column
app_train.select_dtypes('object').apply(pd.Series.nunique, axis = 0)

Out[10]:
NAME_CONTRACT_TYPE             2
CODE_GENDER                    3
FLAG_OWN_CAR                   2
FLAG_OWN_REALTY                2
NAME_TYPE_SUITE                7
NAME_INCOME_TYPE               8
NAME_EDUCATION_TYPE            5
NAME_FAMILY_STATUS             6
NAME_HOUSING_TYPE              6
OCCUPATION_TYPE               18
WEEKDAY_APPR_PROCESS_START     7
ORGANIZATION_TYPE             58
FONDKAPREMONT_MODE             4
HOUSETYPE_MODE                 3
WALLSMATERIAL_MODE             7
EMERGENCYSTATE_MODE            2
dtype: int64
```
