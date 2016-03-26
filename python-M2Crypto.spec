#
# Conditional build:
%bcond_with	tests	# test target [fails, some files are missing]

Summary:	Python interface to OpenSSL
Summary(pl.UTF-8):	Interfejs Pythona do OpenSSL
Name:		python-M2Crypto
Version:	0.24.0
Release:	1
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/m2crypto/
Source0:	https://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-%{version}.tar.gz
# Source0-md5:	8e87235942c76d1ba9f999ee33764fdb
Patch0:		%{name}-store2ssl.patch
Patch1:		%{name}-swig.patch
URL:		https://gitlab.com/m2crypto/m2crypto
BuildRequires:	openssl-devel >= 1.0.1e
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	swig-python >= 2.0
BuildRequires:	unzip
%pyrequires_eq	python-libs
Requires:	openssl >= 1.0.1e
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

%prep
%setup -q -n M2Crypto-%{version}
%patch0 -p1
%patch1 -p1

%build
%py_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENCE README.rst
%dir %{py_sitedir}/M2Crypto
%attr(755,root,root) %{py_sitedir}/M2Crypto/__m2crypto.so
%{py_sitedir}/M2Crypto/*.py[co]
%dir %{py_sitedir}/M2Crypto/PGP
%{py_sitedir}/M2Crypto/PGP/*.py[co]
%dir %{py_sitedir}/M2Crypto/SSL
%{py_sitedir}/M2Crypto/SSL/*.py[co]
%{py_sitedir}/M2Crypto-*.egg-info
