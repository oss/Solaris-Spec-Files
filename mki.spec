Summary: MKI MacKerbInfo perl script
Name: mki
Version: 3.0
Release: 3
Group: System/Daemons
Copyright: Rutgers
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl-module-NIS

%description
MKI is a perl script that replaces MacKerbInfo. It sends an IID to a 
PC/Mac, given a username.

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/local/sbin
cp in.mki %{buildroot}/usr/local/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat <<EOF
You must modify your inetd to listen, traditionally on port 9897

    ex: mackrbinfo stream tcp nowait  nobody  /usr/local/sbin/tcpd \
               /usr/local/sbin/in.mki -G alumni
EOF

%files
%defattr(0711,nobody,other)
/usr/local/sbin/in.mki
