%include	/usr/lib/rpm/macros.python

Summary:	Python interface to OpenSSL
Summary(pl):	Interfejs Pythona do OpenSSL
Name:		python-M2Crypto
Version:	0.06
Release:	2
License:	BSD-like
Source0:	http://www.pobox.org.sg/home/ngps/m2/m2crypto-%{version}.zip
URL:		http://www.pobox.org.sg/home/ngps/m2/
Group:		Development/Languages/Python
%pyrequires_eq	python
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	openssl-devel >= 0.9.6
BuildRequires:	swig
BuildRequires:	rpm-pythonprov
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

%build
%{__make} -C swig INCLUDE="-I. -I%{py_incdir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

cp -a M2Crypto $RPM_BUILD_ROOT%{py_sitedir}
%{py_comp} $RPM_BUILD_ROOT%{py_sitedir}
%{py_ocomp} $RPM_BUILD_ROOT%{py_sitedir}

gzip -9nf BUGS CHANGES INSTALL LICENCE README STORIES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html demo
%{py_sitedir}/M2Crypto
