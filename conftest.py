import subprocess
import warnings
import paramiko
import pytest

host = '192.168.0.100'
username = 'vika'
password = 'None'


@pytest.fixture(scope='function')
def server():
    client.paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username, password)
    _stdin, _stdout, _stderr = client.exec_command("iperf -s -u -t 15")
    print(_stdout.read().decode())
    client.close()
    return _stderr


@pytest.fixture(scope='function')
def client(server):
    stderr = server
    sp = subprocess.Popen('iperf -c {} -u -i 1'.format(host), shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, err = sp.communicate()
    return out, err, stderr


