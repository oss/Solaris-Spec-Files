Summary: Scripts to check on timeliness of backups
Name: check-backups
Version: 1.7
Release: 4
Group: System Environment/Base
Copyright: Rutgers
Source: check-backups.tar.gz
Patch: check-backups-perlenv.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: rcs

%description
Check-backups is a script that checks the timeliness of local fs backups.

%prep
%setup -q -n check-backups

%patch -p1

%build
co getdate.c check-backups
gcc -o getdate getdate.c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/backup
install -m 0644 check-backups.exclude.example %{buildroot}/backup
install -m 0744 check-backups.wrapper %{buildroot}/backup
install -m 0555 getdate %{buildroot}/backup
install -m 0555 check-backups %{buildroot}/backup

%clean
rm -rf %{buildroot}

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
/backup/*
