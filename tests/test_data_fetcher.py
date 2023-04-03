from py_solis_s3_logger.data_fetcher import fetch_data
from py_solis_s3_logger.data_classes import InverterData, ResponseState

SOLIS_RESPONSE = "1801020225210738;780035;102;17.7;170;6.600000;d;NO;"


def test_fetch_data(httpx_mock):
    httpx_mock.add_response(url="http://192.168.128.118/inverter.cgi", text=SOLIS_RESPONSE)
    response : InverterData = fetch_data()
    assert response.response_state == ResponseState.SUCCESS
    assert response.current_power == 170
