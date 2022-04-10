import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nzbget_service(host):
    s = host.service('transmission-daemon')

    assert s.is_enabled
    assert s.is_running
    assert s.systemd_properties['User'] != 'root'


def test_nzbget_http(host):
    # ZNBGet has user nzbget with password tegbzn6789 set by default
    html = host.run('curl http://transmission:transmission@localhost/transmission').stdout

    assert 'Transmission' in html


def test_firewall(host):
    i = host.iptables

    assert (
        '-A INPUT -p tcp -m tcp --dport 80 '
        '-m conntrack --ctstate NEW,ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'INPUT')
    assert (
        '-A OUTPUT -p tcp -m tcp --sport 80 '
        '-m conntrack --ctstate ESTABLISHED '
        '-m comment --comment "Allow HTTP traffic" -j ACCEPT'
    ) in i.rules('filter', 'OUTPUT')
