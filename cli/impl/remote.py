import paramiko
import os

class Remote:

    def __init__(self, server, user, password=None, key_file=None):
        self.server = os.environ.get("REMOTE_SERVER", server)
        self.user = os.environ.get("REMOTE_USER", user)
        self.password = os.environ.get("REMOTE_PASSWORD", password)
        self.key_file = os.environ.get("REMOTE_KEY_FILE", key_file)

    def execute(self, command, file):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            if self.key_file:
                key = paramiko.RSAKey.from_private_key_file(self.key_file)
                client.connect(hostname=self.server, username=self.user, pkey=key)
            else:
                client.connect(hostname=self.server, username=self.user, password=self.password)
        except Exception as e:
            print(f"[!] Cannot connect to the SSH Server: {e}")
            exit()

        execute_me = ""
        if file:
            with open(file, 'r') as f:
                execute_me = f.read()
        elif command:
            execute_me = command
        else:
            print("No file or command provided")
            exit()

        stdin, stdout, stderr = client.exec_command(execute_me)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(f"Error: {err}")

        client.close()
        print("=" * 10 + " done " + "=" * 10)