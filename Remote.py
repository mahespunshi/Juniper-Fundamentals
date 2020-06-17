import paramiko
import getpass
class Remote():
    def __init__(self, hostfile, username, commands):
        self.hostfile = hostfile
        self.username = username
        self.commands = commands
    def execute(self):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        ##########################################################
        # just in case it does not recognize the known_host keys
        # in the known_hosts file
        ##########################################################
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.password = getpass.getpass("Password: ")
        for i in self.hostfile.readlines():
            print("Connecting to..." + i)
            client.connect(i.strip(), 22, self.username, self.password)
            stdin, stdout, stderr = client.exec_command(self.commands)
            for t in stdout.readlines():
                print(t.strip())
            for t in stderr.readlines():
                print(t.strip())
