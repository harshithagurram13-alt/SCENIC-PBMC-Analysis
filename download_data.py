
from pathlib import Path
import urllib.request
import tarfile

# Project data directory
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# 10x Genomics PBMC 3k dataset
URL = (
    "https://s3-us-west-2.amazonaws.com/"
    "10x.files/samples/cell/pbmc3k/"
    "pbmc3k_filtered_gene_bc_matrices.tar.gz"
)

ARCHIVE = RAW_DIR / "pbmc3k_filtered_gene_bc_matrices.tar.gz"

# Download dataset
if not ARCHIVE.exists():
    print("Downloading PBMC 3k dataset...")
    request = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(request, timeout=120) as response:
        with open(ARCHIVE, "wb") as output:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                output.write(chunk)

    print("Download completed!")
else:
    print("Dataset archive already exists.")

# Extract dataset
print("Extracting dataset...")

with tarfile.open(ARCHIVE, "r:gz") as tar:
    tar.extractall(path=RAW_DIR, filter="data")

print("Extraction completed!")
print("Dataset location:", RAW_DIR / "filtered_gene_bc_matrices" / "hg19")
