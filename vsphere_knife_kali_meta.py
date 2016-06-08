import subprocess
from random import choice
from string import ascii_uppercase


def main():
   for _ in range(instances()):
        vmnames = generate_vm_name()
        for name in vmnames:
            deploy_kali(name)
            deploy_meta(name)

   #print(generate_vm_name())
    #print(instances())


def instances():
    number_of_instances = input('Enter how many instances you would like to initiate: ')
    return number_of_instances

def power_on():
    pass


def reset_ip():
    pass


def generate_vm_name():
    return ''.join(choice(ascii_uppercase) for i in range(12))


def deploy_kali(self):
    try:
        subprocess.check_call('knife vsphere vm clone Kali-{} --template "SP_Kali"'.format(self), shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))


def deploy_meta(self):
    try:
        subprocess.check_call('knife vsphere vm clone Meta-{} --template "SP_Meta"'.format(self), shell=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

if __name__ == "__main__": main()
