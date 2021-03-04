from oregonvaxcheck.data.counties import counties_data
from oregonvaxcheck.drivers.sitecheckdriver import SiteCheckDriver


class TestOregonGov:

    def test_county_data(self):
        test_county = counties_data[0]['County']
        # Make sure county data is accurate
        assert test_county == "Marion"
        assert test_county != "Orange"

#    def test_chatbot_county(self):
#        assert
