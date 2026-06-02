import socket
import os

def is_valid_ip(word):
	parts = word.split(".")
	if len(parts) == 4:
		for part in parts:
			if not part.isdigit():
				return False
			if not (0 <= int(part) <= 255):
				return False
		return True
	return False

def get_ips(text,):
	ip_listed = []
	ip_list = text.split()
	for word in ip_list:
		if is_valid_ip(word):
			ip_listed.append(word)
	return ip_listed

def check_ports(ip):
	open_ports = []
	for port in range(20, 101):
		sock = socket.socket()
		sock.settimeout(0.5)
		result = sock.connect_ex((ip, port))
		sock.close()
		if result == 0:
			open_ports.append(port)
	return open_ports

def menu():
	print("==== Port Scanner ====")
	print("1. Загрузить файл")
	print("2. Выход")
	choice = input("Выбор: ")
	return choice

def load_file(path):
	with open(path, "r") as file:
		text = file.read()
	return text

while True:
	choice = menu()
	if choice == "1":
		path = input("Путь к файлу: ")
		text = load_file(path)
		ips = get_ips(text)
		for ip in ips:
			open_ports = check_ports(ip)
			print(f"\nIP: {ip}")
			print(f"Open ports: {open_ports}")
	elif choice == "2":
		break
