

## About the Dataset

The Palmer Archipelago (Antarctica) Penguins dataset was made available by [Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php) and the [Palmer Station Antartica LTER](https://pal.lternet.edu/), a member of the [Long Term Ecological Research Network (LTRN)](https://lternet.edu).

The `palmerpenguins` package contains two pandas datasets, `size_penguins.csv` and `penguins_iter.csv`.
The former is hosted on an AWS Cloud, on a S3 bucket. The latter is locally hosted under `data/01_raw`.

### Meet the penguins
![image of the Penguins](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/lter_penguins.png)

> Artwork: @allison_horst

*What are culmen length & depth?*
The culmen is "the upper ridge of a bird's beak" (definition from Oxford Languages).

For this penguin data, the `culmen length` and `culmen depth` are measured as shown below (thanks Kristen Gorman for clarifying!):
![Penguin parts](https://github.com/allisonhorst/palmerpenguins/blob/master/man/figures/culmen_depth.png)  

### Datasets description
- species: penguin species (Chinstrap, Adélie, or Gentoo)
- culmen_length_mm: culmen length (mm)
- culmen_depth_mm: culmen depth (mm)
- flipper_length_mm: flipper length (mm)
- body_mass_g: body mass (g)
- island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago (Antarctica)
- sex: penguin gender  
- **`penguins_iter.csv`: Original combined data for 3 penguin's species.

> Please refer to the official [Github page](https://github.com/allisonhorst/palmerpenguins) for details and license information.

Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

Thank you everyone for gathering this info and for making it widely available. Special thanks to Dr. Gorman, Palmer Station LTER and the LTER Network and to Marty Downs.

#### License & citation
Data are available by CC-0 license in accordance with the Palmer Station LTER Data Policy and the LTER Data Access Policy for Type I data.
Please cite this data using: Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3): e90081. doi:10.1371/journal.pone.0090081



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
> NOTE: if you have installed the latest version of Kedro, running the above command will downgrade your version. If you wish to remove this feature, change the version of Kedro required in `requirements.txt`.  
>  Alternatively, you can upgrade Kedro to the latest available version with `pip install kedro -U`.  