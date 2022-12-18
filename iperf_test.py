import parser
import

class TestSuite():
    def test_iperf3(self, client):
        stdout, error, err_serv = client
        print('Received from fixture client is: {}'.format(stdout))
        assert error != 0, "Error connect"
        assert err_serv != 0, "Error start server"
        dict = parser.parser(stdout)
        for i in range(len(dict)):
            assert float(dict[i][1]) > 100 and float(dict[i][2]) > 1

        return
