Summary: White pages query tool
Name: wpwhois
Version: 2.1
Release: 3
Group: System Environment/Base
Copyright: Rutgers (based on GPL'd Lynx source)
Source: wpwhois-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Wpwhois lets you look up Rutgers faculty and students from the command
line.

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include -I/usr/local/ssl/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib -L/usr/local/ssl/lib -R/usr/local/ssl/lib" \
export PATH CC CXX CPPFLAGS LD LDFLAGS
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/usr/local/man/man1
install -m 0755 lynx $RPM_BUILD_ROOT/usr/local/bin/wpwhois
install -m 0644 wpwhois.1 $RPM_BUILD_ROOT/usr/local/man/man1/wpwhois.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/bin/wpwhois
/usr/local/man/man1/wpwhois.1
