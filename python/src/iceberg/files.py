# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from abc import abstractmethod
from enum import Enum, auto
from typing import Any

try:
    from typing import Protocol, runtime_checkable
except ImportError:  # pragma: no cover
    from typing_extensions import Protocol  # type: ignore
    from typing_extensions import runtime_checkable


class FileContentType(Enum):
    """An enum that includes all possible content types for an Iceberg data file"""

    DATA = auto()
    POSITION_DELETES = auto()
    EQUALITY_DELETES = auto()


class FileFormat(Enum):
    """An enum that includes all possible formats for an Iceberg data file"""

    ORC = auto()
    PARQUET = auto()
    AVRO = auto()
    METADATA = auto()


@runtime_checkable
class StructProtocol(Protocol):  # pragma: no cover
    """A generic protocol used by accessors to get and set at positions of an object"""

    @abstractmethod
    def get(self, pos: int) -> Any:
        ...

    @abstractmethod
    def set(self, pos: int, value) -> None:
        ...
