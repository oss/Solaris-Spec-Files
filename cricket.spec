Summary: cricket
Name: cricket
Version: 1.0.3
Release: 1
Copyright: GPL
Group: Applications/Editors
Source: http://download.sourceforge.net/cricket/cricket-1.0.3.tar.gz
Distribution: GPL
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl-module-Digest-MD5 perl-module-libwww perl-module-TimeDate perl-module-Time-HiRes rrdtool SNMP_Session DB_File

%description
GNU Nano is designed to be a free replacement for the Pico text editor, part of the PINE email suite from The University of Washington.  It aims to emulate Pico as closely as possible and perhaps include extra functionality.

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
/usr/local/cricket-%{version}



