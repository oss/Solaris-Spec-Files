Summary: Sun patch-checking tool
Name: patchdiag
Version: 1.0.4
Release: 3ru
Group: System Environment/Base
Copyright: Rutgers
Source: patchdiag-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Patchdiag determines the patch levels on your system against Sun's
Recommended and Security patch list.  Additionally, it operates from
input files and lists all patches that pertain to packages installed
on the system.

%prep
%setup -q -n files

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
find . -print | cpio -pdm %{buildroot}
sed "s/sos/rutgers\/public/" %{buildroot}/usr/local/sbin/patchdiag > %{buildroot}/usr/local/sbin/patchdiag2
mv %{buildroot}/usr/local/sbin/patchdiag2 %{buildroot}/usr/local/sbin/patchdiag

#echo "%defattr(-, root, bin)" >RPM_FILE_LIST
#find . -type f -print | grep -v RPM_FILE_LIST | sed 's/^\.//' >>RPM_FILE_LIST

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, bin)
/usr/local/doc/patchdiag_userguide
/usr/local/man/manl/patchdiag.1m
/usr/local/sbin/patchdiag.pl
/usr/local/sbin/patchdiag.sparc
%defattr(0700, root, bin) 
/usr/local/sbin/patchdiag