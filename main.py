import subprocess
import urllib.request
import tarfile

def main():
    print('Welcome to NPM package analysis')
    
    package = 'nextjs'
    out_filename = f"{package}_out.tgz"

    # Get the URL to download the package
    url = subprocess.check_output(["npm", "view", package, "dist.tarball"], text=True).strip()
    # Download it
    urllib.request.urlretrieve(url, out_filename)

    # Unzip it
    with tarfile.open(out_filename, "r:gz") as tar:
        tar.extractall(path="extracted")

    print('Done...')

if __name__ == "__main__":
    main()