import click
from impl import remote as rmt


@click.group()
def cli():
    pass


@click.command(name="remote", help="Execute command on remote server")
@click.option("--host", help="Remote Hostname")
@click.option("--pwd", help="Remote password")
@click.option("--usr", help="Remote username")
@click.option("--command", help="Command to be executed")
@click.option("--file", help="script file")
@click.option("--key-file", help="Path to the private key file for key-based authentication")
def remote_cmd(host, pwd, usr, command, file, key_file):
    rm = rmt.Remote(server=host, user=usr, password=pwd, key_file=key_file)
    rm.execute(command=command, file=file)


cli.add_command(remote_cmd)

if __name__ == '__main__':
    cli()
