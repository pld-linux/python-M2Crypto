Summary:	Python interface to OpenSSL
Summary(pl):	Interfejs Pythona do OpenSSL
Name:		python-M2Crypto
Version:	0.16
Release:	1
License:	BSD-like
Source0:	http://wiki.osafoundation.org/pub/Projects/MeTooCrypto/m2crypto-%{version}.tar.gz
# Source0-md5:	6fc06583a2be56fc2a46872a0540d78e
Patch0:		%{name}-swig_sources.patch
Group:		Development/Languages/Python
URL:		http://wiki.osafoundation.org/bin/view/Projects/MeTooCrypto
%pyrequires_eq	python
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	swig >= 1.3.24
#BuildRequires:	swig-python >= 1.3.25
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
M2Crypto makes accessible to the Python programmer the following:
- DH, RSA, DSA, symmetric ciphers, message digests, HMACs.
- SSL functionality to implement clients and servers.
- S/MIME v2.

M2Crypto is released under a very liberal BSD-like licence. See
LICENCE for details.

%description -l pl
M2Crypto udostêpnia z poziomu Pythona nastêpuj±ce funkcje:
- DH, RSA, DSA, szyfry symetryczne, skróty, HMAC
- SSL do implementacji klientów i serwerów
- S/MIME v2.

%prep
%setup -q -n m2crypto-%{version}
%patch0 -p1

find demo -type d -name CVS | xargs rm -rf

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

# shutup check-files
find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py \
	-exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL LICENCE README doc/*.html demo
%dir %{py_sitedir}/M2Crypto
%attr(755,root,root) %{py_sitedir}/M2Crypto/*.so
%{py_sitedir}/M2Crypto/*.py[oc]
%dir %{py_sitedir}/M2Crypto/SSL
%{py_sitedir}/M2Crypto/SSL/*.py[oc]
%dir %{py_sitedir}/M2Crypto/PGP
%{py_sitedir}/M2Crypto/PGP/*.py[oc]
