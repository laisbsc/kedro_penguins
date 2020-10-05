## Creating a new project

This Kedro project was generated using `Kedro 0.16.3` by running:
```
kedro new
```
For more details on how to create your Kedro project, visit [this page](https://kedro.readthedocs.io/en/stable/02_get_started/04_new_project.html).


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