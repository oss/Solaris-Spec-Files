Summary: DJB's publicfile server
Name: publicfile
Version: 0.52
Release: 2
Group: Applications/Internet
Copyright: BSD
Source: %{name}-%{version}.tar.gz
Patch: %{name}-%{version}.patch
BuildRequires: patch
Requires: daemontools ucspi-tcp
# and /usr/local/bin on the $PATH before /bin
BuildRoot: /var/tmp/%{name}-root

%description
Publicfile is an extremely simple (and thus probably secure) ftp and
http server.  If you only need to serve files (no CGI scripts),
consider using this package instead of apache, et al.

%prep
%setup -q
%patch -p1

%build
make

%install
build_dir=`pwd`
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/publicfile
make setup check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
/usr/local/publicfile
