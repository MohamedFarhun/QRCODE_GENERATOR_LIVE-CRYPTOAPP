# QRCODE GENERATOR USING STREAMLIT

Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.

Python function as a web service to scrape and analyze web page data according to most common **HTML** tags.

Installed Python packages:-
altair==4.2.0
attrs==22.1.0
backports.zoneinfo==0.2.1
beautifulsoup4==4.11.1
blinker==1.5
cachetools==5.2.0
certifi==2022.6.15
charset-normalizer==2.1.1
click==8.1.3
commonmark==0.9.1
cycler==0.11.0
decorator==5.1.1
entrypoints==0.4
fonttools==4.37.1
gitdb==4.0.9
GitPython==3.1.27
idna==3.3
importlib-metadata==4.12.0
importlib-resources==5.9.0
Jinja2==3.1.2
jsonschema==4.15.0
kiwisolver==1.4.4
MarkupSafe==2.1.1
matplotlib==3.5.3
numpy==1.23.2
packaging==21.3
pandas==1.4.4
Pillow==9.2.0
pip==22.2.2
pkgutil_resolve_name==1.3.10
protobuf==3.20.1
pyarrow==9.0.0
pydeck==0.8.0b1
Pygments==2.13.0
Pympler==1.0.1
pyparsing==3.0.9
pyrsistent==0.18.1
python-dateutil==2.8.2
pytz==2022.2.1
pytz-deprecation-shim==0.1.0.post0
qrcode==6.1
requests==2.28.1
rich==12.5.1
semver==2.13.0
setuptools==63.4.3
six==1.16.0
smmap==5.0.0
soupsieve==2.3.2.post1
streamlit==1.12.0
toml==0.10.2
toolz==0.12.0
tornado==6.2
typing_extensions==4.3.0
tzdata==2022.2
tzlocal==4.2
urllib3==1.26.12
validators==0.20.0
watchdog==2.1.9
wheel==0.37.1
zipp==3.8.1

Scan the QRCode which will redirect to our App:
Our App:-
  url=https://infocryptos.netlify.app/

How to call it from Python:

Step 1 : Load the Daisi
<pre>
import pydaisi as pyd
qrcode_generator_infocrypto = pyd.Daisi("farhun/QRCODE GENERATOR-INFOCRYPTO")
</pre>


**Documented endpoints**
analyze_webpage
qrcode_generator_infocrypto.analyze_webpage(wp_url).value
qrcode_generator_infocrypto.st_ui().value




