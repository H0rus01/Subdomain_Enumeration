# Subdomain_Enumeration
Subdomain Scanner
Description: This is a simple subdomain scanner tool written in Python. It takes a target domain as an input and checks for the existence of subdomains using a predefined list of subdomains from a file named subdominios.txt.

Usage:

Edit
Copy code
python subdomain_scanner.py -t <target_domain>
Example:

Edit
Copy code
python subdomain_scanner.py -t example.com
Options:

-t or --target: Specify the target domain to scan for subdomains.
Requirements:

Python 3.x
urllib module
os module
argparse module
subdominios.txt file containing a list of subdomains to check (one per line)
How it works:

The script reads the list of subdomains from the subdominios.txt file.
It then iterates through the list and constructs a URL for each subdomain by appending the target domain.
The script uses urllib.request.urlopen to send a request to each URL and checks if the subdomain exists.
If the subdomain exists, it prints a success message indicating the found subdomain.
If the subdomain does not exist, it silently skips to the next one.
Notes:

The script does not perform any DNS lookups or recursive scans. It simply checks if the subdomain responds to an HTTP request.
The script assumes that the subdominios.txt file is in the same directory as the script.
The script does not handle errors or exceptions other than KeyboardInterrupt (Ctrl+C).
License: This script is released under the MIT License. See the LICENSE file for details.
