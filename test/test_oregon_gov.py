from oregonvaxcheck.counties import counties_data


class TestOregonGov:
    def test_county_data(self):
        test_county = counties_data[0]['County']
        # Make sure county data is accurate
        assert test_county == "Marion"
        assert test_county != "Orange"

#    def test_chatbot_county(self):
#        assert