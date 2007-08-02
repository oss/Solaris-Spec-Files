Summary:	Process viewer
Name:		top
Version:	3.6.1
Release: 	1
Group:		System Environment/Base
License:	Freely distributable
Source:		%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-root

%description
"top" is a program that will give continual reports about the state of
the system, including a list of the top cpu using processes.  Version
3 of "top" has three primary design goals: provide an accurate
snapshot of the system and process state, not be one of the top
processes itself, be as portable as possible.

%prep
%setup -q

%build
#/bin/echo "sunos5\n\n\n\n/opt/SUNWspro/bin/cc\n\n\n\n-1\n\n5\nyes\n104281\n\n\n" | ./Configure

PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

./configure --prefix=%{buildroot}/usr/local

make

%install
rm -rf %{buildroot}
#mkdir -p %{buildroot}/usr/local/man/man1
#mkdir %{buildroot}/usr/local/bin
#install -m 0755 top %{buildroot}/usr/local/bin/top
#install -m 0444 top.1 %{buildroot}/usr/local/man/man1/top.1

make install 

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, bin)
%doc Changes FAQ INSTALL LICENSE Porting README Y2K
/usr/local/bin/top
/usr/local/man/man1/top.1

%changelog
* Fri Jul 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.6.1-1
- Bump to 3.6.1
