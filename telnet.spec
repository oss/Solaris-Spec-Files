Summary: telnet client with Rutgers-style logging
Name: telnet
Version: 91.03.25
Release: 1
Group: Applications/Internet
License: Rutgers
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: rcs

%description
This is a telnet client which provides logging.

%prep
%setup -q -n %{name}.%{version}

%build
(cd telnetd && co pathnames.h)
ed Config.generic <<__EOF__
    /-Xlinker/s/-Xlinker//
    w
    q
__EOF__
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin %{buildroot}/etc
install -m 0711 telnet/telnet %{buildroot}/usr/local/bin/telnet

# In the tint package, this file is empty:
touch %{buildroot}/etc/telnet.conf.rpm
chmod 0600 %{buildroot}/etc/telnet.conf.rpm

%clean
rm -rf %{buildroot}

%post
echo "To finish this installation, edit and move /etc/telnet.conf.rpm."

%files
%defattr(-, root, bin)
/etc/telnet.conf.rpm
/usr/local/bin/telnet
