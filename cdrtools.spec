Summary: Command line CD burning software
Name: cdrtools
Version: 2.01
Release: 2
Group: Applications/System
Vendor: NBCS-OSS
Packager: Naveen Gavini <ngavini@nbcs.rutgers.edu>
Copyright: GPL
Source: cdrtools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
cdrtools (formerly cdrecord) creates home-burned CDs with a CDR/CDRW recorder.
It works as a burn engine for several applications. It supports CD recorders
from many different vendors; all SCSI-3/mmc- and ATAPI/mmc-compliant drives
should also work. Supported features include IDE/ATAPI, parallel port, and
SCSI drives, audio CDs, data CDs, and mixed CDs, full multi-session support,
CDRWs (rewritable), TAO, DAO, RAW, and human-readable error messages. cdrtools
includes remote SCSI support and can access local or remote CD writers. 

%prep
%setup -q

%build
PATH="/opt/SUNWspro/bin:/usr/sfw/bin:${PATH}" \
export PATH
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
env INS_BASE=$RPM_BUILD_ROOT/usr/local make -e install
cd $RPM_BUILD_ROOT/usr/local
/usr/local/bin/unhardlinkify.py ./


%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
/usr/local/bin/*
/usr/local/man/*
/usr/local/lib/*
/usr/local/sbin/rscsi
/usr/local/include/align.h
/usr/local/include/avoffset.h


%doc ABOUT AN-1.10 AN-2.0 COPYING README

%changelog
* Tue Aug 07 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 2.01
- Updated to version 2.01
