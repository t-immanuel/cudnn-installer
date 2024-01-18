import hashlib
import json
import os.path


def main():
    split_file( 'C:\\Users\\ACER\\Downloads\\cudnn-local-repo-ubuntu2004-8.9.7.29_1.0-1_arm64.deb', "cudnn-local-repo-ubuntu2004-8.9.7.29_1.0-1_arm64")


def split_file(filename, target_folder, split_byte_size=20*1024*1024):
    file_size = os.path.getsize(filename)
    number_of_splits = ceildiv(file_size, split_byte_size)
    os.makedirs(os.path.basename(target_folder), exist_ok=True)

    hashes = []

    with open(filename, "rb") as f:
        for i in range(number_of_splits):
            content = f.read(split_byte_size)
            hashes.append(hashlib.md5(content).hexdigest())

            with open(os.path.join(target_folder, f"{i}"), "wb") as target:
                target.write(content)
    with open(os.path.join(target_folder, f"hash"), "w") as hashfile:
        json.dump(hashes, hashfile, indent=2)



def ceildiv(a, b):
    return -((-a) // b)


if __name__ == "__main__":
    main()

