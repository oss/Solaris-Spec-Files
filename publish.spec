%define cvsdate 20030501

Summary: Software to automatically publish RPM packages into repository
Name: publish
Version: 0.%{cvsdate}
Release: 3
Group: System Environment/Base
Copyright: Rutgers
Source: repository-scripts-%{cvsdate}.tar.bz2
BuildRoot: /var/tmp/%{name}-root
Requires: bash checkrelease

%description
Software to automatically publish RPM packages into repository

%prep
%setup -q -n repository-scripts

#%patch -p1

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/bin \
    $RPM_BUILD_ROOT/etc/init.d/

cp publish.sh publish-agent.sh $RPM_BUILD_ROOT/usr/local/bin/
cp publish-initd.sh $RPM_BUILD_ROOT/etc/init.d/publish

chmod 500 $RPM_BUILD_ROOT/usr/local/bin/publish*.sh
chmod 500 $RPM_BUILD_ROOT/etc/init.d/publish

%clean
rm -rf $RPM_BUILD_ROOT

%post
cat<<EOF
You will need to add this line:

0,5,10,15,20,25,30,35,40,45,50,55 * * * * /usr/local/bin/publish-agent.sh > /dev/null 2>&1

to your crontab in order for publish to run.
EOF

%files
%defattr(-,root,other)
/usr/local/bin/publish*.sh
/etc/init.d/publish

