Summary: OpenOffice.org office suite
Name: openoffice.org
Version: 1.1.1
Release: 1ru
Group: System Environment/Base
Copyright: GPL
Source: OpenOffice.org-%{version}.tar
BuildRoot: %{_tmppath}/%{name}-root
Provides: openoffice

%description
OpenOffice.org office suite.

%prep
%setup -q -n OpenOffice.org-%{version}


# NOTE: OpenOffice.org's install is a big piece of poop, in order to
# make the rpm package, you need to pre-install it first and then tar
# up that install, partly due to the way even the CLI install requires
# X and how the installer seems to hard-code paths. (There is a way 
# around this problem, anyway...)
#
# To do the pre-install, do this:
#  create an 'autoresponse' file containing this:
#  [ENVIRONMENT]
#   INSTALLATIONMODE=INSTALL_NETWORK
#   INSTALLATIONTYPE=STANDARD
#   DESTINATIONPATH=/usr/local/OpenOffice.org-%{version}
#   OUTERPATH=
#   LOGFILE=
#   LANGUAGELIST=<LANGUAGE>
#
#  [JAVA]
#   JavaSupport=preinstalled_or_none
#
# Then, run ./setup -v -r:autoresponse
# Finally, tar it up.. cp to /usr/local and do something like:
#     tar cvf OpenOffice-%{version}.tar OpenOffice.org-%{version}
#


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin
cd ..
mv OpenOffice.org-%{version} %{buildroot}/usr/local/

rm -f %{buildroot}/usr/local/OpenOffice.org-%{version}/program/{setup.log,sopatchlevel.sh}

# want to strip all the binaries but am too lazy to see which are
# strippable binaries, hence the exit 0
for i in "find %{buildroot}/usr/local/OpenOffice.org-%{version}/program/"; do
    strip $i && exit 0
done

#cat > %{buildroot}/usr/local/bin/ooffice << EOF
##!/bin/sh
#exec /usr/local/OpenOffice.org1.0/program/soffice $*
#EOF
#chmod +x %{buildroot}/usr/local/bin/ooffice

mkdir -p %{buildroot}/usr/local/bin
cd %{buildroot}/usr/local/bin

# Install component symlinks
for app in agenda calc draw fax impress label letter master math memo vcard writer padmin office; do
ln -sf /usr/local/OpenOffice.org-%{version}/program/s$app s$app
ln -sf /usr/local/OpenOffice.org-%{version}/program/s$app oo$app
done

mkdir -p %{buildroot}/etc/openoffice/
cat > %{buildroot}/etc/openoffice/autoresponse.conf <<EOF
[ENVIRONMENT]
INSTALLATIONMODE=INSTALL_WORKSTATION
INSTALLATIONTYPE=WORKSTATION
DESTINATIONPATH=<home>/.openoffice
 
[JAVA]
JavaSupport=none
EOF


%files
%defattr(-, root, other)
/usr/local/OpenOffice.org-%{version}
/usr/local/bin/*
