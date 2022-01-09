# FormSG Python SDK v2

This library was created during my stint at MOH where I had to automate the processing of FormSG forms after they were filled up. The official FormSG SDK is only written in JavaScript and Node.JS.

## Table of Contents

- [FormSG Python SDK v2](#formsg-python-sdk-v2)
  - [Table of Contents](#table-of-contents)
  - [Roadmap](#roadmap)
  - [Usage](#usage)
  - [Support](#support)
  - [Contributing](#contributing)
  - [Acknowledgement](#acknowledgement)

## Roadmap

These are my plans to improve this repository
- Add comments and logging for easier readability and troubleshooting 
- Verifying FormSG Header Signatures
- Create Medium article to explain the codes in detail
- Improve README.md

## Usage

Clone the repository

```sh
git clone https://github.com/miltonsim/formsg-python-sdk-v2
```

Set your FormSG secret in the environment 

## Support

Please open an issue for support.

## Contributing

Make a PR if you are interested to contribute.

## Acknowledgement
After I developed this SDK, I chanced upon a [repository](https://github.com/fivehealth/formsg-python-sdk) written by skylander86 to solve the exact same problem in Oct 2021. However, it did not support attachment decryption then which mine did. I eventually open-sourced mine in Jan 2022 when I had time.

I did learn from the way he structured his codes as it is my first time open-sourcing a project. Evidently, the logic is completely different.