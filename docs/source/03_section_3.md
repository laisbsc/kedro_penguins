# Kedro Palmer Penguins example

## Load data to `catalog.yml` from AWS S3 bucket (using `credentials` and `load args`)
1. If using PyCharm or VSCode, drag the `credentials.yml` file from `./base` and drop it into `./local`. This file will hold the S3 credentials to access your account. DO NOT SHARE YOUR CREDENTIALS.  
All files in the `./local` folder will be ignored by git, which by default will protect your credentials from being public.
Add the credentials following the steps on 'Example 4' on the [this documentation page](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html).  
Add a wrapper `client_kwargs` to the credentials and your code should look something like this:  
```
# S3 bucket credentials for development setup
 dev_s3:
      client_kwargs:
           aws_access_key_id: CDFREWSFDSSSDDDDR456
           aws_secret_access_key: LOREMIPSUMBLABLABLAWEALLLOVEKLEDROVERYMUCH
```
> NOTE: The credentials above are fake.
 
2.In `./base/catalog.yml` add the catalog entries for your dataset:
```
size_penguins:
  type: pandas.CSVDataSet
  filepath: s3://penguins-dataset-iter/penguins_size.csv
  credentials: dev_s3
  load_args:
    sep: ','
    na_values: ['#NA', NA]
```
 
3. Test your data using IPython. On terminal type:
``` commandline
    kedro ipython
```
Once in the IPython shell, check if the data is loads successfully by running:
```
    context.catalog.load('size_penguins')
```
Once you see the data on the CLI output, all is working well.