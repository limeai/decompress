import tarfile
import zipfile
from pathlib import Path

# development of this library was heavily influenced by code in fastai https://github.com/fastai/fastai_dev/blob/master/dev/04_data_external.ipynb

__all__ = ["decompress"]

def decompress(fname=None, dest=None):
    "decompress `fname` to folder `dest`."
    assert(fname), "Please specify a fname to decompress"
    fname = Path(fname)
    dest = fname.parent if dest is None else Path(dest)
    fname_suffix = fname.suffix
    if fname_suffix==".tar":
        tarfile.open(fname, 'r').extractall(dest)
    elif fname_suffix==".tgz" or fname_suffix ==".gz":
        tarfile.open(fname, 'r:gz').extractall(dest)
    elif fname_suffix==".bz2":
        tarfile.open(fname, 'r:bz').extractall(dest)
    elif fname_suffix==".xz":
        tarfile.open(fname, 'r:xz').extractall(dest)
    elif zipfile.is_zipfile(fname):
        zipfile.ZipFile(fname, 'r').extractall(dest)
    else:
        print(f'{fname_suffix} is not yet supported for decompressing')
    return dest