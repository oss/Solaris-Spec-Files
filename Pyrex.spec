Name:		Pyrex
Version: 	0.9.6.4
Release: 	1
Copyright: 	GPL
Group: 		Applications/Python
Summary: 	Pyrex
Packager: 	Naveen Gavini <ngavini@nbcs.rutgers.edu>
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires:	python >= 2.4

%description
Pyrex lets you write code that mixes Python and C data types any way you 
want, and compiles it into a C extension for Python. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/local
python setup.py install --prefix=$RPM_BUILD_ROOT/usr/local

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/*

%changelog
* Wed Jan 02 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.9.6.4-1
- Updated to the latest version.
* Fri Aug 31 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.9.5.1a-1
- Updated to the latest version.
