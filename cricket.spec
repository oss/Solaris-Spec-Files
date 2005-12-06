Summary: cricket
Name: cricket
Version: 1.0.5
Release: 1ru
Copyright: GPL
Group: Applications/Editors
Source: http://download.sourceforge.net/cricket/cricket-1.0.5.tar.gz
Distribution: GPL
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl-module-Digest-MD5 perl-module-libwww perl-module-TimeDate perl-module-Time-HiRes rrdtool SNMP_Session DB_File

%description
Cricket is a high performance, extremely flexible system for monitoring 
trends in time-series data. Cricket was expressly developed to help 
network managers visualize and understand the traffic on their networks, 
but it can be used all kinds of other jobs, as well. 

%prep 
%setup -q

%build
./configure

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/cricket-%{version}
cp -r * $RPM_BUILD_ROOT/usr/local/cricket-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, bin)
/usr/local/cricket-%{version}
