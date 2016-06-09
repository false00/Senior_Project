import subprocess
from random import choice
from string import ascii_uppercase
from subprocess import Popen, DEVNULL


def main():
   for _ in range(instances()):
        vmnames = [generate_vm_name()]
        for name in vmnames:
            print('Preparing to deploy {}-Kali'.format(name))
            deploy_kali(name)
            print('{}-Kali deployed successfully'.format(name))
            power_on('{}-Kali'.format(name))
            print('Preparing to deploy {}-Metasploitable'.format(name))
            deploy_meta(name)
            print('{}-Metasploitable deployed successfully'.format(name))
            power_on('{}-Metasploitable'.format(name))

print('Operation completed successfully.')


def instances():
    number_of_instances = input('Enter how many instances you would like to initiate: ')
    number_of_instances = int(number_of_instances)
    return number_of_instances


def power_on(self):
    try:
        subprocess.call('knife vsphere vm state {} --state on'.format(self), shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))


def reset_ip():
    pass


def generate_vm_name():
    return ''.join(choice(ascii_uppercase) for i in range(12))


def deploy_kali(self):
    try:
        subprocess.call('knife vsphere vm clone "{}-Kali" --template SP-Kali'.format(self), shell=True, stdout=DEVNULL, stderr=DEVNULL)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))


def deploy_meta(self):
    try:
        subprocess.call('knife vsphere vm clone "{}-Metasploitable" --template GM-Metasploitable'.format(self), shell=True, stdout=DEVNULL, stderr=DEVNULL )
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

if __name__ == "__main__": main()
