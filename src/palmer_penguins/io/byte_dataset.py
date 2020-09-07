from kedro.io.core import AbstractDataSet, DataSetError


class ByteDataSet(AbstractDataSet):
    def __init__(self, filepath):
        self._filepath = filepath

    def _save(self, _):
        raise DataSetError('Read Only DataSet')

    def _load(self):
        # used in the input part of the node
        with open(str(self._filepath), 'rb') as f:
            return f.read()

    def _describe(self):
        return dict(filepath=self._filepath)
