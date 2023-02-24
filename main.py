import argparse
import requests


def download_file(url, local_filename):
    if local_filename == None:
        local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response    uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()

parser.add_argument('URL', help='Url To Download File')
# parser.add_argument('Output', help='By Which Name You Want To Save File')
parser.add_argument("-o", '--output',
                    help='By Which Name You Want To Save File', default=None)

args = parser.parse_args()

print(args.URL)
print(args.output)
print(type(args.output))
download_file(args.URL, args.output)
