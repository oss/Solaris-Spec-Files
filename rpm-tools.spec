Summary: RPM repository managment tools
Name: rpm-tools
Version: 2002.01.17
Release: 1
Group: System Environment/Base
Copyright: Rutgers
Source: rpm-tools-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root
Requires: perl
Conflicts: rpm-management

%description
The rpm-management tools are:

   genspec       (an automatic specfile generator)
   rpmdiff       (diffs filelists of rpms)
   find-dup-rpm  (finds outdated rpms)
   inc-rel       (increment the release number of a specfile)
   used-sources  (find the sources used by a specfile)
   update-rpm-database (updates RPM database for use after pkgadd/etc)

%prep
%setup -q -n rpm-tools-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
install -m 0755 check-apps.pl %{buildroot}/usr/local/bin/check-apps
install -m 0755 find-dup.pl   %{buildroot}/usr/local/bin/find-dup
install -m 0755 genspec.pl    %{buildroot}/usr/local/bin/genspec
install -m 0755 inc-rel       %{buildroot}/usr/local/bin/inc-rel
install -m 0755 used-sources  %{buildroot}/usr/local/bin/used-sources
install -m 0755 update-rpm-database.sh %{buildroot}/usr/local/bin/update-rpm-database

%clean
rm -rf %{buildroot}

%post
if [ ! -x /usr/local/bin/perl ]; then
    echo "You need to link perl to /usr/local/bin/perl."
fi
if [ ! -x /usr/bin/perl ]; then
    echo "You need to link perl to /usr/bin/perl."
fi

%files
%defattr(-, root, bin)
%doc README
/usr/local/bin/check-apps
/usr/local/bin/find-dup
/usr/local/bin/genspec
/usr/local/bin/inc-rel
/usr/local/bin/used-sources
/usr/local/bin/update-rpm-database

