# Copyright 2020 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
#     or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The code on this file was written by Tam Nguyen (@tamsanh) inspired on the work
produced by Lim Hoang (@limdauto), one of Kedro's core developers.

Thank you both for making this tutorial possible :)
"""

import datetime
import logging

from typing import Any, Dict, List

from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog

import great_expectations as ge
from great_expectations.core.batch import Batch
from great_expectations.datasource.types import BatchMarkers
from great_expectations.core.id_dict import BatchKwargs
from great_expectations.validator.validator import Validator


class GreatExpectationsHook:

    def __init__(self, expectations_map: Dict = None, suite_types: List[str] = None):
        if expectations_map is None:
            expectations_map = {}
        if suite_types is None:
            suite_types = ['warning', None]
        self.expectations_map = expectations_map
        self.suite_types = suite_types

        self.expectation_context = ge.data_context.DataContext()
        self.expectation_suite_names = set(self.expectation_context.list_expectation_suite_names())

        self.logger = logging.getLogger('GreatExpectationsHook')

    @hook_impl
    def before_node_run(
            self, catalog: DataCatalog, inputs: Dict[str, Any], run_id: str
    ) -> None:
        """ Validate inputs data to a node based on using great expectation
        if an expectation suite is defined in ``DATASET_EXPECTATION_MAPPING``.
        """
        self._run_validation(catalog, inputs, run_id)

    def _run_validation(self, catalog: DataCatalog, data: Dict[str, Any], run_id: str):
        for dataset_name, dataset_value in data.items():
            for suite_type in self.suite_types:
                if suite_type is None:
                    target_expectation_suite_name = f'{self.expectations_map.get(dataset_name, dataset_name)}'
                else:
                    target_expectation_suite_name = f'{self.expectations_map.get(dataset_name, dataset_name)}.{suite_type}'

                if target_expectation_suite_name not in self.expectation_suite_names:
                    self.logger.warning(f"Missing Expectation Suite: {target_expectation_suite_name}")
                    continue

                dataset = catalog._get_dataset(dataset_name)
                dataset_class = self._get_ge_class_name(dataset)
                if dataset_class is None:
                    self.logger.warning(f"Unsupported DataSet Type: {dataset_name}({type(dataset)})")
                    continue

                self._run_suite(dataset, target_expectation_suite_name, run_id)

    @staticmethod
    def _get_ge_class_name(dataset):
        from kedro.extras.datasets.spark import SparkDataSet
        from kedro.extras.datasets.pandas import CSVDataSet
        if isinstance(dataset, CSVDataSet):
            return 'PandasDataset'
        elif isinstance(dataset, SparkDataSet):
            return 'SparkDFDataset'
        else:
            return None

    def _run_suite(self, dataset, target_expectation_suite_name, run_id):
        class_name = self._get_ge_class_name(dataset)
        target_suite = self.expectation_context.get_expectation_suite(target_expectation_suite_name)
        df = dataset.load()
        batch = Batch(
            'kedro', BatchKwargs({'path': 'kedro', 'datasource': 'kedro'}), df, None,
            BatchMarkers(
                {
                    "ge_load_time": datetime.datetime.now(datetime.timezone.utc).strftime(
                        "%Y%m%dT%H%M%S.%fZ"
                    )
                }

            ), self.expectation_context
        )
        v = Validator(batch, target_suite, {'module_name': 'great_expectations.dataset', 'class_name': class_name})
        vgdf = v.get_dataset()
        self.expectation_context.run_validation_operator('action_list_operator', [vgdf], run_id=run_id)