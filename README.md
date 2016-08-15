#NetApp SANtricity Client Library - Python SDK


##Requirements

The SANtricity Python SDK client library requires Python 2.7 or later.

##Installation

###setuptools Installation

Installation of the Python bindings can be performed through [setuptools](http://pypi.python.org/pypi/setuptools).

Once downloaded, enter the following command:

```python
python setup.py install
```

###Manual Installation

If you chose not install the Python bindings through setuptools, you can perform the
installation manually by first downloading the latest release of the package. Once
downloaded, enter the following command to import the package:

```python
import netapp.santricity
```

###Getting started

To get started using the Python SDK, access the ``api_client.py`` file and specify
the host URL for your REST service.

```python
#/usr/bin/python

from netapp.santricity.configuration import Configuration
from netapp.santricity.api_client import ApiClient
from netapp.santricity.api.v2.storage_systems_api import StorageSystemsApi
from netapp.santricity.models.v2.storage_system_response import StorageSystemResponse
from pprint import pprint

config = Configuration()
config.host = "http://localhost:8080" #
config.username = "rw"
config.password = "rw"

api_client = ApiClient()
config.api_client = api_client

storage_system = StorageSystemsApi(api_client=api_client)

ssr = storage_system.get_all_storage_systems()
```

##Using HTTPS with the Python SDK

The Python SDK uses a Configuration object to manage the primary settings controlling
the connection between the application that uses the SDK and the proxy. The following
are some of the more relevant settings for using an HTTPS connection to the proxy:

*	``host``	-	The URL of the proxy server to use, including protocol and port
* 	``ssl_ca_cert``	-	Path to a certificate bundle to use for verifying the connection
*	``verify_ssl``	-	Parameter to indicate if SSL verification should be performed or not

Additionally, the following two SSL-related parameters are also available, which are
used to identify a client certificate to be presented to the server:

*	``cert_file``
*	``key_file``

Depending on the level of security required, some or all of the settings may be adjusted.

###Using HTTPS with the default self-signed certificates

This method is not generally recommended, but is helpful to know how to quickly get
started using HTTPS with the proxy.


####Configure the Host Attribute

The first thing that must be done is to provide the URL to the proxy that utilizes SSL.
If the default ports were used, this will be port 8443. Enter the following command to
specify the host URL for the configuration object:

```python
from netapp.santricity.configuration import Configuration
config = Configuration
confg.host = https://testproxy.foo.com:8443
```


####Configuring the SSL Verification

If you are using the default self-signed certificate, the client will be unable to verify
the authenticity of the proxy server without additional configuration. In this case,
attempts to make an API call will result in ``certificate verify failed`` errors.

There are two methods to deal with the aforementioned scenario. First, you can disable
SSL verification, which is less secure. Alternatively, you can export and then import
the certificate to be used by the client SDK.


#####Disabling SSL Verification

To bypass ``certificate verify failed`` errors, set the ``verify_ssl`` attribute of
the Configuration object to False.

```python
from netapp.santricity.configuration import Configuration
config = Configuration
confg.host = https://testproxy.foo.com:8443
config.verify_ssl = False
```

Once configured, errors will not occur when performing requests. However, there will
be warning indicating that an unverified connection was made.

```python
/venvs/python-sdk/lib/python2.7/site-packages/urllib3/connectionpool.py:838: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/security.html
InsecureRequestWarning
```

The aforementioned warning can be disabled by adding a couple of lines to the program.

```python
import urllib3
urllib3.disable_warnings()
```

#####Using an exported certificate with the client

Using this method will export the self-signed certificate from the proxy web server
and make it available to the client SDK. This method allows you to keep the SSL
setting to ``true``.


######Export the certificate

Use the Java keytool to export the certificate to the ``proxy-cert-export.cer`` file.

```python
CWD = /opt/netapp/santricity_web_services_proxy
./jre/bin/keytool -export -rfc -alias jetty -storepass changeit -file proxy-cert-export.cer -keystore working/keystore
```


######Convert the certificate to PEM format

The Python SDK will expect the file containing the certificate bundle to use to verify
the connection to be in PEM format. The export will be in ``x.509`` binary format, so
it will need to be converted.

```python
openssl x509 -inform DER -in proxy-cert-export.cer -out prox-cert-export.pem
```


######Configure application to use certificate

Copy the PEM formatted certificate to a location accessible to the application using
the client SDK. Update the Configuration object's ``ssl_ca_cert`` attribute to the
location of the file and enable SSL verification.

```python
from netapp.santricity.configuration import Configuration
config = Configuration
confg.host = https://testproxy.foo.com:8443
config.verify_ssl = True
config.ssl_ca_cert = "path/to/proxy-cert-export.pem"
```

The client is now able to make verified SSL connections to the proxy server based on
the default self-signed certificate.

###Using HTTPS with a signed certificate

This section details how to use an authentic or "real" signed certificate and the SDK.
Content within this section is not a complete guide for configuring the Web Services
proxy with a signed certificate.

The following sections assume that the proxy server has been configured to use a
signed certificate.


####Application Configuration

Similar to the self-signed certificate method, you must configure the host to use the
HTTPS based URL for the proxy and enable SSL verification. You also must configure the
application to use a CA certificate file that contains a set of trusted CA certificates.

```python
from netapp.santricity.configuration import Configuration
config = Configuration
confg.host = https://testproxy.foo.com:8443
config.verify_ssl = True
config.ssl_ca_cert = "path/to/ca-file.pem"
```

If the certificate was signed from a trusted authority, there should be no additional
configuration needed on the client host (as long as you have access to a PEM file
containing the set of trusted root CA certificates.)


####CA certificate files

The SDK must have access to a file containing a set of trsuted CAs. This requirement
is applicable regardless if you are using a globally trusted certificate authority,
enterprise, or local certificate authority. This file should be in PEM format by
default.

#####Using a custom CA certificate file

If you do not have a certificate file of generally trusted CAs or you choose not to
use such a file, you can obtain the root certificate from the issuing CA and that
item available to the application in it's own file.

#####Using system-wide trusted CA files

Most operating systems have a system wide repository of trusted CAs. If this is
available in PEM format, you can use this as the file specified for the
``config.ssl_ca_cert`` attribute in the application.

```python
Default system trusted CAs = /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
```

You can use the system-wide trusted CA files even if you use your own CA to sign the
certificate for the web service proxy. In this case, simply add the root certificate
for your own CA to the system's CA configuration.