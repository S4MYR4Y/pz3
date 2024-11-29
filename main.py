import dns.message
import dns.query
import dns.rdataclass
import dns.rdatatype
from ftplib import FTP
import paramiko


def perform_dns_query():
    queryname = dns.name.from_text("amazon.com")
    q = dns.message.make_query(queryname, dns.rdatatype.NS)
    print("The query is:")
    print(q)
    print(" ")
    r = dns.query.udp(q, "8.8.8.8")
    print("The response is:")
    print(r)

def perform_ftp():
    ftp = FTP('ftp.us.debian.org')  # connect to host, default port
    ftp.login()  # user anonymous, passwd anonymous@
    '230 Login successful.'
    ftp.cwd('debian')  # change into "debian" directory
    '250 Directory successfully changed.'
    ftp.retrlines('LIST')
    with open('README', 'wb') as fp:
        ftp.retrbinary('RETR README', fp.write)
    ftp.quit()

def perform_ssh():
    command = "ip a"

    host = "192.168.56.101"
    username = "kali"
    password = "kali"

    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command(command)
    print(_stdout.read().decode())
    client.close()


if __name__ == "__main__":
    choice = input("Choose a task: 1 - dns, 2 - ftp, ssh - 3: ")
    if choice == "1":
        perform_dns_query()
    elif choice == "2":
        perform_ftp()
    elif choice == "3":
        perform_ssh()
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
