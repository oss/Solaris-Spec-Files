%define cvsdate 20030617

Summary: shrubs
Name: shrubs
Version: 0.%{cvsdate}
Release: 1ru
Group: System Environment/Base
Copyright: Rutgers
Source: shrubs-%{cvsdate}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: perl

%description
shrubs software

%prep
%setup -q -n shrubs

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/backup
find . -print | cpio -pdm $RPM_BUILD_ROOT/backup/

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
%attr(0550, root, ops) /backup/.backup_netapp
%attr(0550, root, ops) /backup/check-backups-netapp
%attr(0440, root, ops) /backup/check-backups-netapp.exclude.sample
%attr(0550, root, ops) /backup/check-backups-netapp.wrapper
%attr(0440, root, ops) /backup/sample_schedule.netapp
%attr(0750, root, ops) /backup/shrubs

