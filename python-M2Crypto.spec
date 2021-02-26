#
# Conditional build:
%bcond_with	tests	# test target [fails, some files are missing]
%bcond_without	doc	# don't build doc
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define	module	M2Crypto

Summary:	Python interface to OpenSSL
Summary(pl.UTF-8):	Interfejs Pythona do OpenSSL
Name:		python-M2Crypto
Version:	0.30.1
Release:	5
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/m2crypto/
Source0:	https://pypi.debian.net/M2Crypto/M2Crypto-%{version}.tar.gz
# Source0-md5:	7fce3cbf85eb84a669682892b935746b
Patch0:		%{name}-store2ssl.patch
Patch1:		%{name}-swig.patch
URL:		https://gitlab.com/m2crypto/m2crypto
BuildRequires:	openssl-devel >= 1.0.1e
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	swig-python >= 2.0
BuildRequires:	unzip
Requires:	openssl >= 1.0.1e
Requires:	python-libs
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

M2Crypto jest wydane na bardzo liberalnej licencji BSD - szczegóły w
pliku LICENCE.

%package -n python3-%{module}
Summary:	Python interface to OpenSSL
Summary(pl.UTF-8):	Interfejs Pythona do OpenSSL
Group:		Libraries/Python
Requires:	openssl >= 1.0.1
Requires:	python3-libs
Requires:	python3-modules

%description -n python3-%{module}
M2Crypto makes accessible to the Python programmer the following:
- DH, RSA, DSA, symmetric ciphers, message digests, HMACs.
- SSL functionality to implement clients and servers.
- S/MIME v2.

M2Crypto is released under a very liberal BSD-like licence. See
LICENCE for details.

%description -n python3-%{module} -l pl.UTF-8
M2Crypto udostępnia z poziomu Pythona następujące funkcje:
- DH, RSA, DSA, szyfry symetryczne, skróty, HMAC
- SSL do implementacji klientów i serwerów
- S/MIME v2.

M2Crypto jest wydane na bardzo liberalnej licencji BSD - szczegóły w
pliku LICENCE.

%prep
%setup -q -n M2Crypto-%{version}
%patch0 -p1
%patch1 -p1

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENCE README.rst
%dir %{py_sitedir}/M2Crypto
%attr(755,root,root) %{py_sitedir}/M2Crypto/_m2crypto.so
%{py_sitedir}/M2Crypto/*.py[co]
%dir %{py_sitedir}/M2Crypto/SSL
%{py_sitedir}/M2Crypto/SSL/*.py[co]
%{py_sitedir}/M2Crypto-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES LICENCE README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%dir %{py3_sitedir}/%{module}/SSL
%{py3_sitedir}/%{module}/SSL/*.py
%{py3_sitedir}/%{module}/SSL/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
%endif

