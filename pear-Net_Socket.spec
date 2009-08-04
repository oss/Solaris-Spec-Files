Summary: PEAR: Network Socket Interface
Name: pear-Net_Socket
Version: 1.0.9
Release: 2 
License: PHP License
Group: Development/Libraries
Source: Net_Socket-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://pear.php.net/
Prefix: %{_prefix}

%description
Net_Socket is a class interface to TCP sockets.  It provides blocking
and non-blocking operation, with different reading and writing modes
(byte-wise, block-wise, line-wise and special formats like network
byte-order ip addresses).

%prep
%setup -q -n Net_Socket-%{version}

%build
mkdir -p %{buildroot}/usr/local/lib/php/Net

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%install
cp Socket.php %{buildroot}/usr/local/lib/php/Net

%files
%defattr(-,root,bin)
/usr/local/lib/php/Net/Socket.php
%doc

%changelog
* Mon Jul 27 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.0.9-1
- Fixed php requires.
