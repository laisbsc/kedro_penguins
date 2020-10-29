## Use transcode to convert the plots into binary and base64
In this section, we will write a custom dataset that will allow read the data from the output `.png` file as a binary string and convert it to a base64. Such encoding is helpful when there is a need to transfer binary data over a media that only supports textual data transfer. It assures data integrity over the transference.  
Transcode allows the user to load and save the same file in multiple ways, via its specified `filepath`, by using different DataSet implementations. For more information, check out the [documentation](https://kedro.readthedocs.io/en/stable/05_data/01_data_catalog.html?highlight=transcode#transcoding-datasets).

On the `conf/base/catalog.yml` file add the `@matplotlib` transcode to the `penguins_scatter_plot`, such as:
```
penguins_scatter_plot@matplotlib:
  type: kedro.extras.datasets.matplotlib.MatplotlibWriter
  filepath: data/scatter_plot.png
```
In the `src/kedro_penguins/pipelines/data_engineering/pipeline.py` also add the `@matplotlib` transcode to the output of `make_scatter_plot` node.  
Your code should now look like this:  

```
node(
    make_scatter_plot,
    inputs="size_penguins",
    outputs='penguins_scatter_plot@matplotlib',
),
```
Check if all runs as expected by executing `kedro run`.  

### Writing the custom dataset for transcode
Create a folder under `src/Palper_penguins/io`. Next, create a file named `byte_dataset.py`. The class ByteDataSetAdd will be a read-only dataset and return a binary string of the input data.
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
Create another file named `base64_dataset.py`. The class `Base64DataSet` will be a write-only dataset and will return the base64 `scatter_plot_64.txt` file.
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
  type: kedro_penguins.io.byte_dataset.ByteDataSet
  filepath: data/scatter_plot.png

penguins_scatter_plot_base64:
  type: kedro_penguins.io.base64_dataset.Base64DataSet
  filepath: data/scatter_plot_64.txt
```
Now, let's add those datasets into the pipelines. In `src/kedro_penguins/pipelines/data_engineering/pipeline.py` add another pipeline.
```
node(
    lambda x: x,  # identity function since this node just encodes (no function)
    inputs="penguins_scatter_plot@byteform",
    outputs="penguins_scatter_plot_base64",
),
```