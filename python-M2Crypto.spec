Summary:	Python interface to OpenSSL
Name:		python-M2Crypto
Version:	0.06
Release:	1
License:	BSD-style
Source0:	http://www.pobox.org.sg/home/ngps/m2/m2crypto-%{version}.zip
URL:		http://www.pobox.org.sg/home/ngps/m2/
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Requires:	python >= 1.5.2
BuildRequires:	python-devel >= 1.5.2
BuildRequires:	openssl-devel >= 0.9.6
BuildRequires:	swig 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define python_prefix      %(echo `python -c "import sys; print sys.prefix"`)
%define python_version     %(echo `python -c "import sys; print sys.version[:3]"`)
%define python_includedir  %{_includedir}/python%{python_version}
%define python_libdir      %{python_prefix}/lib/python%{python_version}
%define python_sitedir     %{python_libdir}/site-packages
%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"
%define python_compile     python -c "import compileall; compileall.compile_dir('.')"

%description
M2Crypto makes accessible to the Python programmer the following:
- DH, RSA, DSA, symmetric ciphers, message digests, HMACs.
- SSL functionality to implement clients and servers.
- S/MIME v2.

M2Crypto is released under a very liberal BSD-style licence. See 
LICENCE for details.

%prep
%setup -q -n m2crypto-%{version}

%build
make -C swig INCLUDE="-I. -I%{python_includedir}"
cd M2Crypto
%{python_compile}
%{python_compile_opt}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{python_sitedir}

find M2Crypto -name \*.py | xargs -r rm -f
cp -a M2Crypto $RPM_BUILD_ROOT%{python_sitedir}

gzip -9nf BUGS CHANGES INSTALL LICENCE README STORIES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html demo 
%{python_sitedir}/M2Crypto
