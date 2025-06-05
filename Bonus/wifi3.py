import subprocess

def get_wifi_password(ssid_name):
    try:
        result = subprocess.check_output(
            f'netsh wlan show profile name="{ssid_name}" key=clear',
            shell=True
        ).decode('utf-8', errors='ignore')

        # Find the line with "Key Content"
        for line in result.split('\n'):
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                return password

        return "Password not found or not stored."
    except subprocess.CalledProcessError:
        return "Network profile not found."

# Example usage:
ssid = input("Enter the Wi-Fi network name (SSID): ")
password = get_wifi_password(ssid)
print(f"Password for '{ssid}': {password}")
