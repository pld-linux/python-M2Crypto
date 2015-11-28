Summary:	Python interface to OpenSSL
Summary(pl.UTF-8):	Interfejs Pythona do OpenSSL
Name:		python-M2Crypto
Version:	0.22.3
Release:	2
License:	BSD-like
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-%{version}.tar.gz
# Source0-md5:	573f21aaac7d5c9549798e72ffcefedd
Patch0:		%{name}-store2ssl.patch
Patch1:		%{name}-swig.patch
URL:		http://chandlerproject.org/bin/view/Projects/MeTooCrypto
BuildRequires:	openssl-devel >= 0.9.8
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	swig-python >= 2.0
BuildRequires:	unzip
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
M2Crypto makes accessible to the Python programmer the following:
- DH, RSA, DSA, symmetric ciphers, message digests, HMACs.
- SSL functionality to implement clients and servers.
- S/MIME v2.

M2Crypto is released under a very liberal BSD-like licence. See
LICENCE for details.

%description -l pl.UTF-8
M2Crypto udostępnia z poziomu Pythona następujące funkcje:
- DH, RSA, DSA, szyfry symetryczne, skróty, HMAC
- SSL do implementacji klientów i serwerów
- S/MIME v2.

%prep
%setup -q -n M2Crypto-%{version}
%patch0 -p1
%patch1 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/M2Crypto
%attr(755,root,root) %{py_sitedir}/M2Crypto/*.so
%{py_sitedir}/M2Crypto/*.py[co]
%dir %{py_sitedir}/M2Crypto/SSL
%{py_sitedir}/M2Crypto/SSL/*.py[co]
%{py_sitedir}/M2Crypto-*.egg-info
