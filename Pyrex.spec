Name:		Pyrex
Version: 	0.9.8.4
Release: 	3
License: 	GPL
Group: 		Applications/Python
Summary: 	Pyrex
Packager: 	Brian Schubert <schubert@nbcs.rutgers.edu>
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
%defattr(-,root,root,-)
%doc USAGE.txt ToDo.txt README.txt CHECKLIST.txt CHANGES.txt
%attr(-,bin,bin) /usr/local/*

%changelog
* Wed Dec 02 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.9.8.4-3
- I will not publish unsigned packages again
* Mon Nov 30 2009 Orcan Ogetbil <orcan@nbcs.rutgers.edu> - 0.9.8.4-2
- Rebuild against python 2.6
* Tue Jun 17 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.9.8.4-1
- Updated to version 0.9.8.4
* Wed Jan 02 2008 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.9.6.4-1
- Updated to the latest version.
* Fri Aug 31 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.9.5.1a-1
- Updated to the latest version.
