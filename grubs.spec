%define cvsdate 20020910

Summary: GRUBS perl5 version of RUBS backup software
Name: grubs
Version: 0.%{cvsdate}
Release: 1ru
Group: System Environment/Base
Copyright: Rutgers
Source: grubs-%{cvsdate}.tar.bz2
#Patch: grubs-perlenv-var.patch
BuildRoot: /var/tmp/%{name}-root
Requires: perl

%description
Self-contained perl version of RUBS backup software.

%prep
%setup -q -n grubs-%{cvsdate}

#%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
find . -print | cpio -pdm $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ ! -d /backup ] ; then
    cat <<EOF
/backup does not exist.  RPM will create it, but you should run

 chmod 0750 /backup
 chown backup.ops /backup

to set the permissions correctly after this installation is over.
EOF
fi

%files
%defattr(-,root,other)
#%attr(0700, root, ops) /backup/rubs_status
%attr(0440, root, ops) /backup/sample_device_map
%attr(0440, root, ops) /backup/sample_schedule
%attr(0750, root, ops) /backup/rubs_restore
%attr(0550, root, ops) /backup/backup
%attr(4550, root, ops) /backup/tape_dump
%attr(0440, root, ops) /backup/snap_map.example
/usr/local/man/man8/*
/usr/local/man/man5/*
%attr(0700, root, ops) /var/adm/rubs_transcripts
