# Kedro Palmer Penguins example

> NOTE: Dear reader, this is a beta repo. I.e., if you think there is anything which could be better explained, please create an issue and let me know.
> I'm always happy to take on suggestions. Same goes if this tutorial helped you in any way. :) 

    
## The Project - Advanced Kedro tutorial

![image of the Penguins](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/lter_penguins.png)

> Artwork: @allison_horst


## Overview
This repo was assembled for those who have have tried the [Spaceflights tutorial](https://kedro.readthedocs.io/en/latest/03_tutorial/01_spaceflights_tutorial.html) 
and want to continue practicing using Kedro.  

If you create an empty project using `kedro new` and follow the text by copying and pasting the example code as described,
it will take you approximately **2 hours** and you will end up with a repository as the one in here.  Alternatively, you can clone this repo using 
```python
git clone https://github.com/laisbsc/kedro_penguins.git
```
and tweak the project as you wish, for exploration/adaptation purposes.
 
By working on this example, you will learn how to use [transformers](https://kedro.readthedocs.io/en/stable/07_extend_kedro/02_transformers.html?highlight=transformers#dataset-transformers), 
and how to expand your project capabilities by using [Hooks](https://kedro.readthedocs.io/en/stable/07_extend_kedro/04_hooks.html?highlight=hooks) with the [Great Expectations](https://greatexpectations.io) Python library for the [Penguins dataset](https://github.com/allisonhorst/palmerpenguins).

### Aim

This repository uses the `size_penguins.csv` dataset, hosted on AWS cloud env and the `iter_penguins.csv`, hosted locally.
The aim of this example is to show users how to:
 - Load 'remote' data, in this case, a `.csv` file hosted in a AWS S3 bucket.
 - Generate a scatter plot with the data in the catalog with `kedro run`.
 - Convert the plot ('scatter_plot.png') in a node using Transcode.
 - Use Kedro Hooks to expand the project with the Great Expectations plugin.  
   > Note: the last part of the project will use PySpark, which is compatible with Python 3.7 and requires Java to be installed.  
                                                                                  >To install Java (in macOS) type `brew cask install java` on your terminal.  
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
    

## Rules and guidelines for best practice

To get the best out of this template:
 * Please don't remove any lines from the `.gitignore` file we provide
 * Make sure your results can be reproduced by following a data engineering convention, e.g. the one we suggest [here](https://kedro.readthedocs.io/en/stable/06_resources/01_faq.html#what-is-data-engineering-convention)
 * Don't commit any credentials or local configuration to your repository
 * Keep all credentials or local configuration in `conf/local/`
