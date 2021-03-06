Name: maple
Summary: Maple 9
Version: 9.5
Release: 3
Group: Licensed
Copyright: Licensed
# to build the maple9.tar.gz, go through the GUI maple install on a 
# solaris box (install into /usr/local), then 
# mv /usr/local/maple /usr/local/maple9
# (put in README.rutgers and maple9.init.d into the directory)
# tar cf maple9.tar maple9
# gzip maple9.tar
Source: maple9.tar.gz

BuildRoot: /var/tmp/%{name}-root
BuildArch: noarch

%description
Maple 9


%prep
%setup -q -n maple9

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin
mkdir -p $RPM_BUILD_ROOT/etc/init.d
cd ..
cp -r maple9 $RPM_BUILD_ROOT/usr/local
mv maple9/maple.init.d $RPM_BUILD_ROOT/etc/init.d/maple

ln -sf /usr/local/maple9 $RPM_BUILD_ROOT/usr/local/maple
ln -sf /usr/local/maple9/bin/maple $RPM_BUILD_ROOT/usr/local/bin/maple
ln -sf /usr/local/maple9/bin/xmaple $RPM_BUILD_ROOT/usr/local/bin/xmaple

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
/usr/local/maple9/*
/usr/local/bin/maple
/usr/local/bin/xmaple
/usr/local/maple
%attr(755,root,root)/etc/init.d/maple

