from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class ResponseState(Enum):
    SUCCESS = 0
    TIMEOUT = 1

@dataclass
class InverterData:
    serial_number: str | None
    model: str | None
    firmware: str | None
    current_power: int | None
    energy_today: float | None
    energy_total: float | None
    response_state: ResponseState = ResponseState.SUCCESS

    @staticmethod
    def from_response(data: str) -> InverterData:
        """Return Inverter object from the Solis Inverter response.
        Args:
            data: The data from the Solis Inverter CGI.
        Returns:
            An Inverter object.
            :rtype: object
        """

        split_data = data.split(";")
        if len(split_data) < 7:
            raise Exception("Wrong data from inverter.")

        def try_parse_float(item):
            try:
                return float(item)
            except:
                return None

        return InverterData(
            serial_number=split_data[0],
            model=split_data[2],
            firmware=split_data[1],
            current_power=try_parse_float(split_data[4]),
            energy_today=try_parse_float(split_data[5]),
            energy_total=try_parse_float(split_data[6]),
            response_state=ResponseState.SUCCESS
        )

    @staticmethod
    def timeout_value() -> InverterData:
        return InverterData(
            serial_number="",
            model="",
            firmware="",
            current_power=0,
            energy_today=0,
            energy_total=0,
            response_state=ResponseState.TIMEOUT
        )