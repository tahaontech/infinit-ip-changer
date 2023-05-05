# Infinit IP Changer

Infinit IP Changer is an open source project that provides a proxy and an API to change your proxy IP every time you want. It is designed to help you protect your privacy and increase your online security by allowing you to access the web with different IP addresses.
This application is an excellent choice for circumventing rate and IP limits.

## Features

- Change your proxy IP every time you want
- Access the web with different IP addresses
- Protect your privacy and increase your online security
- Open source

## Requirements

- Docker

## Installation

1. Clone the repository:

```bash
git clone https://github.com/tahaontech/infinit-ip-changer.git
```

2. build the image:

```bash
cd infinit-ip-changer
docker build . -t ip-changer
```

## Usage

To use the proxy and api, start the server:

```bash
docker run -p 8118:8118 -p 5000:5000 ip-changer
```

### Proxy

To use the proxy, set your browser or application to use the following URL:

```
http://localhost:8118
```

The server will randomly select an IP address from tor network available IP addresses.

### API

By default, the server will listen on port 5000.

The API provides a single endpoint:

```
GET /changeip
```

This endpoint renew your tor connection and return you the new IP address.

## Contributing

We welcome contributions to Infinit IP Changer. To contribute, please:

1. Fork the repository
2. Create a feature branch (`git checkout -b my-new-feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create a new Pull Request

## License

Infinit IP Changer is released under the MIT License. See `LICENSE` for details.
