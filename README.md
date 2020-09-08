# palmer_penguins

The Palmer Archipelago (Antarctica) Penguins dataset was made available by [Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php) and the [Palmer Station Antartica LTER](https://pal.lternet.edu/), a member of the [Long Term Ecological Research Network (LTRN)](https://lternet.edu).

The palmerpenguins package contains two datasets.
In this Kedro-example we will use only the `penguins_size.csv` file.

#### Variables:
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

## Overview

This Kedro project was generated using `Kedro 0.16.3` by running:

```
kedro new
```

This repository uses the `size_penguins.csv` dataset, hosted remotely.  The aim of this repo is to show the user how to:
 - Load 'remote' data, in this case, a `.csv` file hosted in a AWS S3 bucket. [check!]
 - Plot a scatter graph with the data with `kedro run`. [write the docs]
 - Encode and decode the generated image ('scatter_plot.png') in a node using Transcode [write the docs]
 - Use Kedro Hooks to expand the project with plugins, in this case the Great Expectations plugin. [code and docs]

## Rules and guidelines for best practice

To get the best out of this template:
 * Please don't remove any lines from the `.gitignore` file we provide
 * Make sure your results can be reproduced by following a data engineering convention, e.g. the one we suggest [here](https://kedro.readthedocs.io/en/stable/06_resources/01_faq.html#what-is-data-engineering-convention)
 * Don't commit any data to your repository
 * Don't commit any credentials or local configuration to your repository
 * Keep all credentials or local configuration in `conf/local/`

## Installing dependencies
Before we start, add the `Great Expectations` plugin to your project dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

```
great-expectations==0.12.1
```

To install all dependencies, run:

```
kedro install
```
> NOTE: if you have installed the latest version of Kedro (at the moment, 0.16.4), running the above command will downgrade your version. If you wish to remove this feature, change the version of Kedro required in `requirements.txt`.
> Alternatively, you can upgrade Kedro to the latest available version with `pip install kedro -U`  

## Load data to `catalog.yml` from AWS S3 bucket (using credentials and load args)
1. If using PyCharm or VSCode, drag the `credentials.yml` file from `./base` and drop it into `./local`. This file will hold the S3 credentials to access your account. DO NOT SHARE THOSE CREDENTIALS.  
All files in the `./local` folder will be ignored by git, which by default will protect your credentials from being shown in public.
Add the credentials following the steps on Example 4 on the [this page of the docs](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html). Add a wrapper to the credentials and your file should look something like this:
[add screenshot code > credentials S3]
 
2.In `./base/catalog.yml` add the catalog entries for your dataset:
```buildoutcfg
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
Once in the Ipython shell, check if the data is loads successfully by running:
```commandline
    context.catalog.load('size_penguins')
```
Once you see the table on the output, be sure all is working well.



## Running Kedro

You can run your Kedro project with:

```
kedro run
```




## Working with Kedro from notebooks

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
>
>## Testing Kedro

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests with the following command:

```
kedro test
```

To configure the coverage threshold, please have a look at the file `.coveragerc`.

## Kedro Hooks - integration with Great Expectations
In this example, we will integrate the Great Expectations plugin to Kedro using Kedro Hooks.

### Kedro Hooks
Allows the user to 'hook' several functionalities to their Kedro project in an easy and consistent manner.
For more details on Kedro Hooks, check out the [documentation](https://kedro.readthedocs.io/en/stable/07_extend_kedro/04_hooks.html).

### Great Expectations
Has the ability to automatically profile and validate the data, as well as to generate documentation based on the expectations.
To learn more about Great Expectations, have a look at the [documentation page](https://docs.greatexpectations.io/en/latest/intro.html).  
 


```buildoutcfg
pip install great_expectation
```

## Package the project

In order to package the project's Python code in `.egg` and / or a `.wheel` file, you can run:

```
kedro package
```

After running that, you can find the two packages in `src/dist/`.

## Building API documentation

To build API docs for your code using Sphinx, run:

```
kedro build-docs
```

See your documentation by opening `docs/build/html/index.html`.

## Building the project requirements

To generate or update the dependency requirements for your project, run:

```
kedro build-reqs
```

This will copy the contents of `src/requirements.txt` into a new file `src/requirements.in` which will be used as the source for `pip-compile`. You can see the output of the resolution by opening `src/requirements.txt`.

After this, if you'd like to update your project requirements, please update `src/requirements.in` and re-run `kedro build-reqs`.
