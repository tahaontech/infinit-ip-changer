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
git clone https://github.com/your-username/infinit-ip-changer.git
```

2. Install the dependencies:

```bash
cd infinit-ip-changer
```

## Usage

### Proxy

To use the proxy, start the server:

```bash
# run command
```

By default, the server will listen on port 8000. You can change this by setting the `PORT` environment variable.

To use the proxy, set your browser or application to use the following URL:

```
http://localhost:3000
```

The server will randomly select a proxy IP address from a list of available IP addresses every time you make a request.

### API

To use the API, start the server:

```bash
npm run api
```

By default, the server will listen on port 3001. You can change this by setting the `PORT` environment variable.

The API provides a single endpoint:

```
GET /changeip
```

This endpoint returns a random proxy IP address from a list of available IP addresses.

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
