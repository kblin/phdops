Title: Installing a valid SSL certificate on HP ILO3
Date: 2014-11-04 15:42
Modified: 2014-11-06 08:32
Category: Ops
Tags: Firefox, HP, ILO, SSL
Slug: hp-ilo-ssl-cert
Author: Kai Blin
Summary: Notes on how to get a valid SSL cert on an HP ILO3.

*UPDATE 2014-11-06*: Can't use an IP address for the CN, fixed the text accordingly

After not having to manage my ILO3based HP servers for a while, today I did feel
the need for remote console access. Unfortunately, Firefox 33 decided that the
SSL certificate shipped out of the box is invalid. So, for my future reference
and for everybody running into a similar issue, here's how to fix access by
creating a certificate sign request (CSR) on the ILO, creating an SSL
certification authority (CA) on your work machine and using the CA to sign the
CSR. The bonus of doing this is that you don't have to bother with browser
warnings about the SSL cert anymore.

Start by logging into the ILO with a less picky browser (Chromium worked for me)
and under Administration > Security > SSL Certificate, fill out the required
information. I initially tried using the IP address to avoid the "certificate
name/host mismatch" warning, but it turns out that while ILO3 claims to load a
certificate when the CN is an IP, it just falls back to the old invalid
certificate instead. So use the ILO's host name and then set up that host name
to access the ILO (DNS or `/etc/hosts`). Click the "Generate CSR" button. This
will take a while to generate the CSR, so in the meantime, get the CA started on
your work machine.


```
# generate the CA key, using a 4096 bit RSA key with an AES256 passphrase
openssl genrsa -aes256 -out rootCA.key 4096
...enter password twice when prompted, don't forget this password...

# Create and self-sign the root CA certificate
openssl req -x509 -new -nodes -key rootCA.key -days 1024 -out rootCA.pem

# copy the rootCA certificate to the distro's CA certificate store
cp rootCA.pem /etc/ssl/certs/   # might be different for your distro
```

In the meantime, hopefully the generation of the CSR in the ILO has finished
(make sure to wait 10 minutes), so click the "Generate CSR" button again to get
a pop-up with the base64-encoded CSR. Copy&paste that into a file on your work
machine, I'll assume ilo.csr.

```
# optional: Check if the CSR looks sane
openssl req -text -noout -verify -in ilo.csr

# sign the ILO CSR using the rootCA key
openssl x509 -req -in ilo.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out ilo.crt -days 500
...enter password when prompted...
```

Now click the "Import certificate" button in the ILO and copy&paste the ilo.crt
file contents into the text box. Click import and wait for an ILO restart.
While the ILO is restarting, open your browser settings and import your
`/etc/ssl/certs/rootCA.pem` file as trusted CA.
