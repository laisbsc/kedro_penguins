# Kedro Palmer Penguins example

> NOTE: Dear reader, this is a beta repo. I.e., if you think there is anything which could be better explained, please create an issue and let me know.
> I'm always happy to take on suggestions. Same goes if this tutorial helped you in any way. :) 

## Overview
This repo was assembled for those who have have tried the [Spaceflights tutorial](https://kedro.readthedocs.io/en/latest/03_tutorial/01_spaceflights_tutorial.html) 
and want to continue practicing using Kedro.  

If you create an empty project using `kedro new` and follow the text by copying and pasting the example code as described,
it will take you approximately **2 hours** and you will end up with a repository as the one in here.  Alternatively, you can clone this repo using 
```python
git clone https://github.com/laisbsc/kedro_penguins.git
```
and tweak the project as you wish, for exploration/adaptation purposes.
 
By working on this example, you will learn how to set up [transformers](https://kedro.readthedocs.io/en/stable/07_extend_kedro/02_transformers.html?highlight=transformers#dataset-transformers), 
and how to expand your project capabilities by using [Hooks](https://kedro.readthedocs.io/en/stable/07_extend_kedro/04_hooks.html?highlight=hooks) with the [Great Expectations](https://greatexpectations.io) Python library for the [Penguins dataset](https://github.com/allisonhorst/palmerpenguins).


## About the Dataset

The Palmer Archipelago (Antarctica) Penguins dataset was made available by [Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php) and the [Palmer Station Antartica LTER](https://pal.lternet.edu/), a member of the [Long Term Ecological Research Network (LTRN)](https://lternet.edu).

The `palmerpenguins` package contains two pandas datasets, `size_penguins.csv` and `penguins_iter.csv`.
The former is hosted on an AWS Cloud, on a S3 bucket. The latter is locally hosted under `data/01_raw`.

## The datasets
### Variables:
`size_penguins.csv`
- species: penguin species (Chinstrap, Adélie, or Gentoo)
- culmen_length_mm: culmen length (mm)
- culmen_depth_mm: culmen depth (mm)
- flipper_length_mm: flipper length (mm)
- body_mass_g: body mass (g)
- island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago (Antarctica)
- sex: penguin gender  
** `penguins_iter.csv`: Original `size_penguins.csv` combined with data for 3 penguin species.

> Please refer to the official [Github page](https://github.com/allisonhorst/palmerpenguins) for details and license information.

Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

Thank you everyone for gathering this info and for making it widely available. Special thanks to Dr. Gorman, Palmer Station LTER and the LTER Network and to Marty Downs.

#### License & citation
Data are available by CC-0 license in accordance with the Palmer Station LTER Data Policy and the LTER Data Access Policy for Type I data.
Please cite this data using: Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3): e90081. doi:10.1371/journal.pone.0090081

### Meet the penguins:
![image of the Penguins](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/lter_penguins.png)

> Artwork: @allison_horst

*What are culmen length & depth?*
The culmen is "the upper ridge of a bird's beak" (definition from Oxford Languages).

For this penguin data, the `culmen length` and `culmen depth` are measured as shown below (thanks Kristen Gorman for clarifying!):
![Penguin parts](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/culmen_depth.png)  

## The Project - Intermediate Kedro tutorial

### Aim

This repository uses the `size_penguins.csv` dataset, hosted on AWS cloud env and the `iter_penguins.csv`, hosted locally.
The aim of this example is to show users how to:
 - Load 'remote' data, in this case, a `.csv` file hosted in a AWS S3 bucket.
 - Generate a scatter plot with the data in the catalog with `kedro run`.
 - Convert the plot ('scatter_plot.png') in a node using Transcode.
 - Use Kedro Hooks to expand the project with the Great Expectations plugin.  
   > Note: the last part of the project will use PySpark, which requires Java to be installed. To install Java (macOS) type `brew cask install java` on your terminal.  
                                                                                  >[It did not work for me - troubleshoot?]

### Table of contents

> NOTE: edit the links when the docs are structured.

1. [Rules and guidelines for Kedro template](#rules-and-guidelines-for-best-practice)
2. Tutorial
    * [Creating a new project](#Creating-a-new-project)
    * [Installing dependencies](#Installing-dependencies)
    * [Loading data to `catalog.yml` from AWS S3 bucket](#load-data-to-catalogyml-from-aws-s3-bucket-using-credentials-and-load-args)
    * [Generate a scatter plot using a Kedro node](#Generate-a-scatter-plot-graph-using-a-node-function)
    * [Convert plots into binary and on base64  with transcode](#Convert-the-plots-into-binary-and-on-base64-by-using-transcode)
    * [Using Kedro Hooks to integrate Great Expectations plugin](#kedro-hooks---integration-with-great-expectations)
3. [Add-ons](#Add-ons)  
    

## Rules and guidelines for best practices

To get the best out of this template:
 * Please don't remove any lines from the `.gitignore` file we provide
 * Make sure your results can be reproduced by following a data engineering convention, e.g. the one we suggest [here](https://kedro.readthedocs.io/en/stable/06_resources/01_faq.html#what-is-data-engineering-convention)
 * Don't commit any data to your repository
 * Don't commit any credentials or local configuration to your repository
 * Keep all credentials or local configuration in `conf/local/`


## Installing dependencies
Before we start, add the `Great Expectations` library to your project dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.
```
great-expectations==0.12.1
```

To install the dependencies, run:
```
kedro install
```
> NOTE: if you have installed the latest version of Kedro (currently, 0.16.4), running the above command will downgrade your version. If you wish to remove this feature, change the version of Kedro required in `requirements.txt`.  
> Alternatively, you can upgrade Kedro to the latest available version with `pip install kedro -U`.  


## Load data to `catalog.yml` from AWS S3 bucket (using `credentials` and `load args`)
1. If using PyCharm or VSCode, drag the `credentials.yml` file from `./base` and drop it into `./local`. This file will hold the S3 credentials to access your account. DO NOT SHARE YOUR CREDENTIALS.  
All files in the `./local` folder will be ignored by git, which by default will protect your credentials from being public.
Add the credentials following the steps on 'Example 4' on the [this documentation page](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html).  
Add a wrapper `client_kwargs` to the credentials and your code should look something like this:  
```
# S3 bucket credentials for development setup
 dev_s3:
           aws_access_key_id: CDFREWSFDSSSDDDDR456
           aws_secret_access_key: LOREMIPSUMBLABLABLAWEALLLOVEKLEDROVERYMUCH
```
> NOTE: The credentials above are fake.
 


## Creating a new project
This Kedro project was generated using `Kedro 0.16.3` by running:
```
kedro new
```
For more details on how to create your Kedro project, visit [this page](https://kedro.readthedocs.io/en/stable/02_get_started/04_new_project.html).

2.In `./base/catalog.yml` add the catalog entries for your dataset:

Once in the IPython shell, check if the data is loads successfully by running:
```
    context.catalog.load('size_penguins')
```
Once you see the data on the CLI output, all is working well.


## Generate a scatter plot graph using a node function
The `notebooks` folder contains the initial data analysis exploration for the project. It generates a scatter plot relating the penguin's culmens dimensions and their species.
![scatter_plot_img](notebooks/scatter_plot_species.png)  
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
Now, compare the code snippet in the function with the one on the notebook (below). Note the similarity between the code inside the for loop above and the individual functions.
![image](docs/images/notebook_pic.png) 

 
## Convert the plots into binary and on base64 by using transcode
In this section, we will write a custom dataset that will allow read the data from the output `.png` file as a binary string and convert it to a base64. Such encoding is helpful when there is a need to transfer binary data over a media that only supports textual data transfer. It assures data integrity over the transference.  
Transcode allows the user to load and save the same file in multiple ways, via its specified `filepath`, by using different DataSet implementations. For more information, check out the [documentation](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html?highlight=transcode#transcoding-datasets).

On the `conf/base/catalog.yml` file add the `@matplotlib` transcode to the `penguins_scatter_plot`, such as:
```
penguins_scatter_plot@matplotlib:
  type: kedro.extras.datasets.matplotlib.MatplotlibWriter
  filepath: data/scatter_plot.png
```
In the `src/palmer_penguins/pipelines/data_engineering/pipeline.py` also add the `@matplotlib` transcode to the output of `make_scatter_plot` node. Your code should now look like this:  
```
node(
    make_scatter_plot,
    inputs="size_penguins",
    outputs='penguins_scatter_plot@matplotlib',
),
```
Check if all runs as expected by executing `kedro run`.  

### Writing custom dataset for transcode
Create a folder under `src/Palper_penguins/io`. Create a file named `byte_dataset.py`. The class ByteDataSetAdd will be a read-only dataset and return a binary string of the input data.
```
from kedro.io.core import AbstractDataSet, DataSetError


class ByteDataSet(AbstractDataSet):
    def __init__(self, filepath):
        self._filepath = filepath

    def _save(self, _):
        """ Used in the output portion of a node
        """
        raise DataSetError('Read Only DataSet')

    def _load(self):
        """ Used in the input part of the node
        """
        with open(str(self._filepath), 'rb') as f:
            return f.read()

    def _describe(self):
        """Describe what the dataset is
        """
        return dict(filepath=self._filepath)
```
Create another file named `base64_dataset.py`. The class `Base64DataSet` will be a write-only dataset and will return the base64 .txt file.
```
from kedro.io.core import AbstractDataSet, DataSetError

from base64 import b64encode


class Base64DataSet(AbstractDataSet):
    def __init__(self, filepath):
        self._filepath = filepath

    def _save(self, binary_data):
        """Takes the incoming binary data and encodes to base64
        """
        with open(str(self._filepath), 'w') as f:
            f.write(b64encode(binary_data).decode('utf8'))

    def _load(self):
        raise DataSetError('Write Only DataSet')

    def _describe(self):
        return dict(filepath=self._filepath)
```
Next, add the transcoded data catalog to the `catalog.yml` file, such as:
```
penguins_scatter_plot@byteform:     #transcode that reads the .png file as byte string
  type: palmer_penguins.io.byte_dataset.ByteDataSet
  filepath: data/scatter_plot.png

penguins_scatter_plot_base64:
  type: palmer_penguins.io.base64_dataset.Base64DataSet
  filepath: data/scatter_plot_64.txt
```
Now, let's add those datasets into the pipelines. In `src/palmer_penguins/pipelines/data_engineering/pipeline.py` add another pipeline.
```
node(
    lambda x: x,  # identity function since this node just encodes (no function)
    inputs="penguins_scatter_plot@byteform",
    outputs="penguins_scatter_plot_base64",
),
```


## Kedro Hooks integration with Great Expectations
In this example, we will integrate the Great Expectations plugin to Kedro using Hooks.

### Kedro Hooks
Allows the user to 'hook' several functionalities to their Kedro project in an easy and consistent manner.
For more details on Kedro Hooks, check out the [documentation](https://kedro.readthedocs.io/en/stable/07_extend_kedro/04_hooks.html).

### Great Expectations
Provides the ability to automatically profile and validate the data, as well as to generate documentation based on the expectations.
In this tutorial we will generate a JSON file with the expectations.
To learn more about Great Expectations, have a look at the [documentation page](https://docs.greatexpectations.io/en/stable/intro.html).  
 
> [NOTE: Explain why one would use them together]
 
#### Create GE folders template
The following command will generate a new directory. The folder structure will be shown on the CLI upon execution.  
From the `src` folder, run:
```
great_expectations init
```
Type `y` and press enter.

Next step is to configure our data source. Type `y` on the next prompt. And `y` again.

For this project, we will use Pandas. Type `1` on the next prompt and `1` again.  
Enter the path for the folder where your data is stored. In this project, we will be using the `iter_penguins.csv`, hosted locally at `data/01_raw`.  
Following, the prompt will ask for a Datasource short name. Enter your name of choice (I chose `pandas_penguins`) and `y` to confirm.  
Next prompt will ask about profiling, type `y`. Since the csv file is in our Datasource, typing `1` will return the list of files available. Type `1` to choose the file.  
The Expectations suite will create a folder path and save the expectations as a JSON file. The file will describe all the expectations which will be asserted on this dataset.  
> [NOTE: Add .gif with the process]

Typying `y` on the next prompt will open the GE documentation with the data profiling analysis on a browser page.  
The 'Walkthrough' window shown is great to get you more familiar with the suite setup.

### Link Kedro to Great Expectations  
#### Creating a Custom dataset
Under `src/<palmer_penguins>/hooks` create a python file. In this project, the file is named `great_expectations_hooks.py`. 
This file will hold the contents of a custom Dataset that will replicate the way Great Expectations generate the validators and runs the checks on the data types of the dataset. In this case, the check will be performed on both `pandas` and `Spark` datasets.  
The snippet of code below illustrates where the datatypes are described.  
![snippet of code showing where the dataset types are specified](docs/images/hooks_pic.png)  
For more information on how to write your own custom datasets, have a look at the [documentation](https://kedro.readthedocs.io/en/stable/07_extend_kedro/01_custom_datasets.html#).  

#### Add pandas and Spark datasets to `catalog.yml`
Add the `pandas` and `Spark` datasets to the catalog file from `data/01_raw`, as follows:  
```
pandas_penguins_data:
  type: pandas.CSVDataSet
  filepath: data/01_raw/penguins_iter.csv

spark_penguins_data:
  type: spark.SparkDataSet
  filepath: data/01_raw/penguins_iter.csv
  file_format: csv
  load_args:
    header: true 
```

#### Add nodes to `src/palmer_penguins/pipeline.py`  
Now, let's add the nodes to `pipelines.py`. In the return
```
"__ge_pipeline__": Pipeline([
            node(lambda x: x.show(), inputs='spark_penguins_data', outputs=None),
            node(lambda x: x.describe(), inputs='pandas_penguins_data', outputs=None),
        ]),
```
By the end, your `create_pipelines()` function will look like this:
```
def create_pipelines(**kwargs) -> Dict[str, Pipeline]:
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    return {
        "__ge_pipeline__": Pipeline([
            node(lambda x: x.show(), inputs='spark_penguins_data', outputs=None),
            node(lambda x: x.describe(), inputs='pandas_penguins_data', outputs=None),
        ]),
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
        "__default__": data_engineering_pipeline + data_science_pipeline,

    }
```

Now, let's run `great_expectations docs build` to check the output on the data validation.


#### Create Datasource for PySpark dataset
On terminal type:
```bash
great_expectations datasource new
```  
Followed by `1` for file, `2` for PySpark. Specify the path for the datafile, which here will be `data/01_raw`.
And the datasource name `spark_data`. 

#### Create a new suite
On terminal type:
```bash
great_expectations suite new
```
Followed by `2` for Spark data and `1` and select the file on disc, option `1`. Name the new Expectation suite, here `spark_penguins_data`.  
The final `y` will open a notebook with the expectations for the data.  
This will create a new expectation. You can edit that expectation on a Jupyter notebook. Moreover, you can always access that notebook by typing `great_expectations suite edit`







====== stopped the tutorial here due to Java install error ==========
_________ Stopped writing the docs here - still needs some tidying __________


If you are interested on knowing more about the integration between Kedro and Great Expectations, have a look at `kedro-great`,
a [Python plugin](https://pypi.org/project/kedro-great/) desinged by [Tam-Sanh Nguyen](https://pypi.org/user/tamu/) to facilitate the integration between Kedro and GE.

_"Hold yourself accountable to Great Expectations. Never have fear of data silently changing ever again."_


This is the end of the tutorial.

## Add-ons
This section contains the documentation add-ons that one might consider using on a Kedro project.

### Working with Kedro from notebooks

In order to use notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```
> NOTE: only necessary if not using `conda`.

For using Jupyter Lab, you need to install it:

```
pip install jupyterlab
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```  
or simply run your regular `jupyter notebook`.

You can also start Jupyter Lab:

```
kedro jupyter lab
```

And if you want to run an IPython session:

```
kedro ipython
```

Running Jupyter or IPython this way provides the following variables in
scope: `proj_dir`, `proj_name`, `conf`, `io`, `parameters` and `startup_error`.


### Ignoring notebook output cells in `git`

In order to automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be left intact locally.  



