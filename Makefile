start:
	mitmweb  --set http2=false -s ./ws.py


start-cli:
	mitmproxy  --set http2=false -s ./ws.py


start-socks5:
	mitmproxy  --set http2=false --mode socks5 -s ./ws.py

