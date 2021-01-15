# Mallook

A Python script for generating image representations of portable executables (PEs).

## Description

This script is designed to iterate byte-by-byte through an executable and generate a 3-channel RGB image with square dimensions as output for use in training image recognition models. In particular, the intended datasets are meant to be image representations of malware and benign software.

(The name is a portmanteau of "malware" and "look" inspired by the otherwise unrelated C-language malloc function.)

## Getting Started

### Dependencies

* This project has been tested and used successfully on the Windows 10 OS with the following libraries installed. Other operating systems and libraries may or may not work.
* Python 3.8.3
* matplotlib 3.3.1
* numpy 1.19.1

### Installing

* Fork the project from (https://github.com/fieldsfieldsfields/mallook)
* In a CLI with Python 3.8.3 and pip, navigate to the mallook folder and type
```
pip install -r requirements.txt
```

### Executing program

* Put the files you would like to convert into mallook/data/input. The folders 'benign' and 'malicious' are there by default, but you can set up your own categories.
* In a CLI with Python 3.8.3 aliased as python, navigate to the mallook folder and type
```
python ./mallook.py
```

## Help

Please submit an issue on the project's github (https://github.com/fieldsfieldsfields/mallook/issues) if you run into any problems. This script was initially written for a single purpose and environment, but I am interested in generalizing it to further uses and environments.

## Authors

[Matthew Fields](https://gist.github.com/fieldsfieldsfields)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [Apache License 2.0] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration
* [Deep Learning with PyTorch](https://www.manning.com/books/deep-learning-with-pytorch)
* [fast.ai](https://www.fast.ai/)