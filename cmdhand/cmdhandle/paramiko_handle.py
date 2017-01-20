# coding=utf-8

import paramiko


class ParamikoHandle(object):
    def __init__(self):
        pass

    def command_run(self, user, ip, port, command, password=None):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port, user)
        stdin, stdout, stderr = ssh.exec_command(command)

        res_stdout = stdout.read()
        res_stderr = stderr.read()
        return res_stdout, res_stderr


if __name__ == '__main__':
    conn = ParamikoHandle()
    result = conn.command_run('sate', '120.27.161.212', 22, 'cat a')
    print result