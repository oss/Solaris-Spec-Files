%define maple_version 10
# %maple_version is the version # that comes from the name of the license
# file, referenced in the init.d script. %version is the version # of maple
# that you are building.
# Ex. license file  %maple_version  %version
#     maple10.lic    10              10
#     maple95.lic    95              9.5
# In the case of maple 10, they are the same.

Name: maple
Summary: Maple 10
Version: %{maple_version}
Release: 2
Group: Licensed
Copyright: Licensed
# To build the maple10.tar.gz, go through the GUI maple install on a 
# solaris box (install into /usr/local), 
# - mv /usr/local/maple /usr/local/maple10
# - Put README.rutgers and maple.init.d into the directory
# - tar cf maple10.tar maple10
# - gzip maple10.tar
Source: maple%{version}.tar.gz

BuildRoot: /var/tmp/%{name}-root
BuildArch: noarch

%description
Maple 10


%prep
%setup -q -n maple%{version}

%install
# Automagically change the version number of maple in the name 
# of the license file, in the init.d script
MAPLE_VERSION=%{maple_version}
export MAPLE_VERSION
sed "s/<MAPLE_RPM_VERSION>/`echo $MAPLE_VERSION`/" maple.init.d > maple.init.d2
mv maple.init.d2 maple.init.d
###

mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cd ..
cp -r maple%{version} $RPM_BUILD_ROOT/usr/local
mv maple%{version}/maple.init.d $RPM_BUILD_ROOT/etc/init.d/maple

ln -sf /usr/local/maple%{version} $RPM_BUILD_ROOT/usr/local/maple
ln -sf /usr/local/maple%{version}/bin/maple $RPM_BUILD_ROOT/usr/local/bin/maple
ln -sf /usr/local/maple%{version}/bin/xmaple $RPM_BUILD_ROOT/usr/local/bin/xmaple

%post
cat <<EOF

 
====================================================================
 You might want to make a /etc/rc2.d/maple link, to start the maple
 license server at boot time
 ln -s /etc/init.d/maple /etc/rc2.d/S99maple

 Read the README.rutgers for more hints on setting this software up
 for use at Rutgers
====================================================================


EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/maple%{version}/*
/usr/local/bin/maple
/usr/local/bin/xmaple
/usr/local/maple
%attr(755,root,root)/etc/init.d/maple

