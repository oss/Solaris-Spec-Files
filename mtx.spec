Name: mtx
Version: 1.2.15
Release: 1
Summary: SCSI media changer control program
Copyright: Redistributable
Group: Utilities/System
Source0: http://prdownloads.sourceforge.net/mtx/%{name}-%{version}.tar.gz
Url: http://%{name}.sourceforge.net
BuildRoot: /var/tmp/%{name}-%{version}


%description
The MTX program controls the robotic mechanism in autoloaders and tape
libraries such as the HP SureStore DAT 40x6, Exabyte EZ-17, and
Exabyte 220. This program is also reported to work with a variety of other tape
libraries and autochangers from Tandberg/Overland, Breece Hill, HP, and 
Seagate.

%prep
%setup -q

%build

./configure
make

%install
mkdir -p $RPM_BUILD_ROOT/sbin
install mtx $RPM_BUILD_ROOT/sbin/mtx
mkdir -p $RPM_BUILD_ROOT/usr/sbin
install loaderinfo $RPM_BUILD_ROOT/usr/sbin/loaderinfo
install scsitape $RPM_BUILD_ROOT/usr/sbin/scsitape
install tapeinfo $RPM_BUILD_ROOT/usr/sbin/tapeinfo
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install mtx.1 $RPM_BUILD_ROOT/%{_mandir}/man1/mtx.1
install scsitape.1 $RPM_BUILD_ROOT/%{_mandir}/man1/scsitape.1
install tapeinfo.1 $RPM_BUILD_ROOT/%{_mandir}/man1/tapeinfo.1


%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc mtx.doc CHANGES README mtxl.README.html
%doc COMPATABILITY FAQ LICENSE* TODO contrib
%{_mandir}/man1/*
/sbin/mtx
/usr/sbin/*

