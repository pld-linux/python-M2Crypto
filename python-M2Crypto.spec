#
# Conditional build:
%bcond_without	tests	# test target
%bcond_without	doc	# documentation
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define	module	M2Crypto

Summary:	Python interface to OpenSSL
Summary(pl.UTF-8):	Interfejs Pythona do OpenSSL
Name:		python-M2Crypto
Version:	0.40.1
Release:	3
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/m2crypto/
Source0:	https://files.pythonhosted.org/packages/source/M/M2Crypto/M2Crypto-%{version}.tar.gz
# Source0-md5:	280c20072afbe7010cf9e9620ea25c7b
URL:		https://gitlab.com/m2crypto/m2crypto
BuildRequires:	openssl-devel >= 1.0.1e
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	swig-python >= 4.0
Requires:	openssl >= 1.0.1e
Requires:	python-modules >= 1:2.7
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
Requires:	openssl >= 1.0.1e
Requires:	python3-modules >= 1:3.5

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

%package apidocs
Summary:	API documentation for Python M2Crypto module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona M2Crypto
Group:		Documentation

%description apidocs
API documentation for Python M2Crypto module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona M2Crypto.

%prep
%setup -q -n M2Crypto-%{version}

# test_verify_with_static_callback has some problems with multiple calls to SMIME.verify() with openssl 3.2.0
%{__sed} -i -e '/    def test_verify_with_static_callback/ i\
    @unittest.skip("fails with openssl 3.2.0")
' tests/test_smime.py

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

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/{_modules,_static,*.html,*.js}
