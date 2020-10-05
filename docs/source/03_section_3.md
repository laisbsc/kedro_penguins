## Load data to `catalog.yml` from AWS S3 bucket (using `credentials` and `load args`)

1. If using PyCharm or VSCode, drag the `credentials.yml` file from `./base` and drop it into `./local`. This file will hold the S3 credentials to access your account.  
DO NOT SHARE YOUR CREDENTIALS.    
All files in the `./local` folder will be ignored by git, which by default will protect your credentials from being public.
Add the credentials following the steps on 'Example 4' on the [this documentation page](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html).  
Add a wrapper (in this case, `client_kwargs`) to the credentials and your code should look something like this:  
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

## Generate a scatter plot graph using a node function
The `notebooks` folder contains the initial data analysis exploration for the project. It generates a scatter plot relating the penguin's culmens dimensions and their species.
![scatter_plot_img](./notebooks/scatter_plot_species.png)  
To open a notebook from the command line using Kedro datasets type `kedro jupyter notebook`. In case you would like to use a regular jupyter notebook with the data in your `catalog.yml` file, add the code snippet to your notebook:  

```
from kedro.context import load_context

context = load_context('../')   #loads the context and catalog from the kedro project
catalog = context.catalog
```  

The following steps will take the dataset, filter it according to the species column and create a scatter plot. The image will be saved in the project folder.  
In the `src/data_engineering/nodes.py` create a new node called `make_scatter_plot`. This node which takes in a pandas dataframe and output a figure:
```
def make_scatter_plot(df: pd.DataFrame):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    for i, species in enumerate(list(df.species.unique())):
        df[df['species'] == species].plot.scatter\
            (x="culmen_length_mm", y="culmen_depth_mm", label=species, color=f"C{i}", ax=ax)
        fig.set_size_inches(12, 12)
        return fig
```  

Now, compare the code snippet in the funtion with the one on the notebook (below). Note the similarity between the code inside the for loop above and the individual functions.
![image](./docs/images/notebook_pic.png)

Kedro nodes are meant to be pure Python functions. Hence, the `savefig()` cell not being necessary. Instead, we will create a dataset to save the plots. To do so,
inside `base/catalog.yml` create a new dataset:
```
penguins_scatter_plot:
  type: kedro.extras.datasets.matplotlib.MatplotlibWriter
  filepath: data/scatter_plot.png
```
Now, let's combine everything into a data pipeline.  

In the `src/palmer_penguins/pipelines/data_engineering/pipeline.py` file add a node to the pipeline. Start by importing `make_scatter_plot` from `.nodes`.  

Next, add the node:
```
node(
    make_scatter_plot,
    inputs="size_penguins",
    outputs='penguins_scatter_plot',
),
```
When `kedro run` is executed, the project will run the `make_scatter_plot` function with the `size_penguins` dataset as
 input and output the `penguins_scatter_plot` as a `.png` file at the place indicated on the `catalog.yml`. In this case,
  `  filepath: data/scatter_plot.png`.