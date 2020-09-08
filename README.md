# Kedro Palmer Penguins example

The Palmer Archipelago (Antarctica) Penguins dataset was made available by [Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php) and the [Palmer Station Antartica LTER](https://pal.lternet.edu/), a member of the [Long Term Ecological Research Network (LTRN)](https://lternet.edu).

The palmerpenguins package contains two pandas datasets, `size_penguins.csv` and `penguins_iter.csv`.
The first is locally hosted under `data/01_raw` and the later on the AWS Cloud, on a S3 bucket.

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
** `penguins_iter.csv`: Original combined data for 3 penguin species.

> Please refer to the official [Github page](https://github.com/allisonhorst/palmerpenguins) for details and license information.

Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

Thank you everyone for gathering this info and for making it widely available. Special thanks to Dr. Gorman, Palmer Station LTER and the LTER Network! Special thanks to Marty Downs.

#### License & citation
Data are available by CC-0 license in accordance with the Palmer Station LTER Data Policy and the LTER Data Access Policy for Type I data.
Please cite this data using: Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3): e90081. doi:10.1371/journal.pone.0090081

### Meet the penguins:
![image of the Penguins](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/lter_penguins.png)

> Artwork: @allison_horst

What are culmen length & depth?
The culmen is "the upper ridge of a bird's beak" (definition from Oxford Languages).

For this penguin data, the culmen length and culmen depth are measured as shown below (thanks Kristen Gorman for clarifying!):
![Penguin parts](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/culmen_depth.png)  


## The Project

### Aim
This repository uses the `size_penguins.csv` dataset, hosted on AWS cloud env and the `iter_penguins.csv`, hosted locally.
The aim of this example is to show users how to:
 - Load 'remote' data, in this case, a `.csv` file hosted in a AWS S3 bucket.
 - Plot a scatter graph with the data using `kedro run`. [write the docs]
 - Convert the generated image ('scatter_plot.png') in a node using Transcode [write the docs]
 - Use Kedro Hooks to expand the project with the Great Expectations plugin. [code and docs]

### Table of contents
1. [Rules and guidelines for Kedro template](#rules-and-guidelines-for-best-practice)
2. Tutorial
    * [Creating a new project](#Creating-a-new-project)
    * [Installing dependencies](#Installing-dependencies)
    * [Loading data to `catalog.yml` from AWS S3 bucket](#load-data-to-catalogyml-from-aws-s3-bucket-using-credentials-and-load-args)
    * [Generate a scatter plot using a Kedro node](#Generate-a-scatter-plot-graph-using-a-node-function)
    * [Convert plots into binary and on base64  with transcode](#Convert-the-plots-into-binary-and-on-base64-by-using-transcode)
    * [Using Kedro Hooks to integrate Great Expectations plugin](#kedro-hooks---integration-with-great-expectations)
3. [Add-ons](#Add-ons)
    
    


## Rules and guidelines for best practice
To get the best out of this template:
 * Please don't remove any lines from the `.gitignore` file we provide
 * Make sure your results can be reproduced by following a data engineering convention, e.g. the one we suggest [here](https://kedro.readthedocs.io/en/stable/06_resources/01_faq.html#what-is-data-engineering-convention)
 * Don't commit any data to your repository
 * Don't commit any credentials or local configuration to your repository
 * Keep all credentials or local configuration in `conf/local/`


## Creating a new project

This Kedro project was generated using `Kedro 0.16.3` by running:
```
kedro new
```

## Installing dependencies
Before we start, add the `Great Expectations` plugin to your project dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.
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
1. If using PyCharm or VSCode, drag the `credentials.yml` file from `./base` and drop it into `./local`. This file will hold the S3 credentials to access your account. DO NOT SHARE THESE CREDENTIALS.  
All files in the `./local` folder will be ignored by git, which by default will protect your credentials from being public.
Add the credentials following the steps on 'Example 4' on the [this documentation page](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html).  
Add a wrapper `client_kwargs` to the credentials and your code should look something like this:
![picture](./docs/images/Screenshot%202020-09-08%20at%2000.15.30.png)
 
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
 [write the docs]
 
 ## Convert the plots into binary and on base64 by using transcode
 Explain the reason why you would like to do this.
 [write the docs]


## Kedro Hooks integration with Great Expectations
In this example, we will integrate the Great Expectations plugin to Kedro using Hooks.

### Kedro Hooks
Allows the user to 'hook' several functionalities to their Kedro project in an easy and consistent manner.
For more details on Kedro Hooks, check out the [documentation](https://kedro.readthedocs.io/en/stable/07_extend_kedro/04_hooks.html).

### Great Expectations
Provides the ability to automatically profile and validate the data, as well as to generate documentation based on the expectations.
In this tutorial we will generate a JSON file with the expectations.
To learn more about Great Expectations, have a look at the [documentation page](https://docs.greatexpectations.io/en/latest/intro.html).  
 
> [Why use them together?]
 
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


Typying `y` on the next prompt will open the GE documentation with the data profiling analysis on a browser page.  
The 'Walkthrough' window shown is great to get you more familiar with the suite setup.

#### Creating a Custom dataset
Under `src/<palmer_penguins>/hooks` create a python file. In this project, the file is named `great_expectations_hooks.py`. This file will hold the contents of a custom Dataset that will validate your data inputs and generate the Great Expectations validation.














### Running Kedro

You can run your Kedro project with:

```
kedro run
```
If you are interested on knowing more about the integration between Kedro and Great Expectations, have a look at `kedro-great`,
a [Python plugin](https://pypi.org/project/kedro-great/) desinged by [Tam-Sanh Nguyen](https://pypi.org/user/tamu/) to facilitate the integration between Kedro and GE.

"Hold yourself accountable to Great Expectations.
Never have fear of data silently changing ever again."


This is the end of the tutorial.

## Add-ons
This section contains the documentation add-ons that one might consider using. 

### Working with Kedro from notebooks

In order to use notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```
> NOTE: only needed if not using `conda`.

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



### Testing your project
Kedro supports tests with... by default.
For instructions on how to write your tests, have a look at the file `src/tests/test_run.py` . You can run your tests with the following command:

```
kedro test
```

To configure the coverage threshold, please have a look at the file `.coveragerc`.

### Package the project

In order to package the project's Python code in `.egg` and / or a `.wheel` file, you can run:

```
kedro package
```

After running that, you can find the two packages in `src/dist/`.

### Building API documentation

To build API docs for your code using Sphinx, run:

```
kedro build-docs
```

See your documentation by opening `docs/build/html/index.html`.

### Building the project requirements

To generate or update the dependency requirements for your project, run:

```
kedro build-reqs
```

This will copy the contents of `src/requirements.txt` into a new file `src/requirements.in` which will be used as the source for `pip-compile`. You can see the output of the resolution by opening `src/requirements.txt`.

After this, if you'd like to update your project requirements, please update `src/requirements.in` and re-run `kedro build-reqs`.
