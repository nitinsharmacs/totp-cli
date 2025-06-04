# TOTP CLI

TOTP CLI application to generate time based otp just right into your terminal.

## Installation

1. Clone github repository.
2. Setup your python whether in environment or system globally.
3. Install poetry

```
pip3 install poetry==2.1.3
```
4. Build the application

```
poetry install
poetry build
```
This should create `*.whl` in `dist` directory. 

5. Install this wheel package.

```
## If using python environment
pip3 install <whl-path>

## If using python for system
pip3 install <whl-path> --break-system-packages
```

I would recommend using some python environment.

## Usage

### Adding a MFA to application

```
totp add --name <mfa-name> --secret <mfa-secret>
```

`--name` is name of your choice that you will need to provide while retrieving the otp.

`--secret` is `base32` key that we have alongwith QR code.

For example,

```
totp add --name gitlab:nitin --secret BASE32SECRETLONG
```
### Get OTP

```
totp get <mfa-name>
```

For example,

```
totp get gitlab:nitin
```

It prints the otp and we well copies to your clipboard.

## Shell completions

Source the respective completion file in your shell as provided in `completions` directory.

Source in `~/.zshrc`
```
source totp.zsh
```

For fish, you can add completion file to path `~/.config/fish/completions`

## Notice

I have not implemented anyway to encrypt the secrets so file which stores secrets is easy to access. If you using this, make sure to take care of that file. 

I am planning to add security measures in future versions.