from abc import ABC
from typing import Dict, Any
from uuid import uuid4
import sys
from typing import List
from typing import Union
from metamenth.measure_instruments.sensor_data import SensorData
from metamenth.measure_instruments.trigger_history import TriggerHistory
from metamenth.datatypes.interfaces.abstract_measure import AbstractMeasure


class AbstractTransducer(ABC):
    def __init__(self,
                 name: str,
                 registry_id: str = None):
        """
        Describes a transducers (in a building)
        :param name: the unique name of the transducers
        :param registry_id: the registry id of the transducers
        """
        self._UID = str(uuid4())
        self._name = None
        self._registry_id = registry_id
        self._set_point = None
        self._meta_data: Dict[str, Any] = {}
        self._data = []

        self.setName(name)

    def getUID(self) -> str:
        return self._UID

    def getName(self) -> str:
        return self._name

    def setName(self, value: str):
        if value is None:
            raise ValueError('name is required')
        self._name = value

    def getRegistryId(self) -> str:
        return self._registry_id

    def setRegistryId(self, value: str):
        self._registry_id = value

    def getSetPoint(self):
        return self._set_point

    def setTransducerSetPoint(self, value: AbstractMeasure, measure: str):
        if value is not None and measure is not None:
            if value.measurement_unit.value != measure:
                raise ValueError('(Input) sensor measure: {} not matching set point measure: {}'
                                 .format(value.measurement_unit.value, measure))
        self._set_point = value

    def getMetaData(self):
        return self._meta_data

    def addData(self, data: Union[List[TriggerHistory], List[SensorData]]):
        if data is None:
            raise ValueError('data should be a list of SensorData or TriggerHistory')
        self._data.extend(data)

    def removeData(self, data: Union[TriggerHistory, SensorData]):
        self._data.remove(data)

    def addMetaData(self, key, value):
        """
        Adds meta data to transducers
        :param key: the key part of the metadata
        :param value: the value part of the metadata
        :return:
        """
        self._meta_data[key] = value

    def removeMetaData(self, key):
        """
        removes meta data to transducers
        :param key: the key part of the metadata
        :return:
        """
        try:
            del self._meta_data[key]
        except KeyError as err:
            print(err, file=sys.stderr)

    def getData(self):
        """
        Search data by attributes values
        :param search_terms: a dictionary of attributes and their values
        :return [SensorData|TriggerHistory]:
        """
        return self._data

    def __eq__(self, other):
        if isinstance(other, AbstractTransducer):
            # Check for equality based on the 'name' attribute
            return self.getName() == other.getName()
        return False

    def __str__(self):
        return (f"Unit: {self.getUID()}, Name: {self.getName()}, Registry ID: {self.getRegistryId()}, "
                f"Set Point: {self.getSetPoint()}, "
                f"Metadata: {self.getMetaData()})")
