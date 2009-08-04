%define name webtools 
%define version 0.8
%define release 11
%define prefix /usr/local

Summary: Core binaries, configs and templates for many Rutgers specific web applications (aka webtools). By default comes with the quota webtool to allow a user to check their quota via the web. 
Name: %name
Version: %version
Release: %release
License: GPL
Group: Services
Source0: %{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-root
Requires: check-criteria

%description
Core binaries, configs and templates for many Rutgers specific web applications (aka webtools). By default comes with the quota webtool to allow a user to check their quota via the web. 

%prep
%setup -n %{name}-%{version}

%build
cd src/
make

%install

PATH="/usr/local/gnu/bin:$PATH"
export PATH

rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/quota
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/no-mail
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/etc
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/bin
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin


install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/etc/index.php $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/etc/index.php-example
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/etc/cfg.php $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/etc/cfg.php-example

install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/maildirmakefolder $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin
install -c -m 4510 $RPM_BUILD_DIR/%{name}-%{version}/src/runas $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/bin
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/makefile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/readfile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/removefile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/appendfile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/link $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/linkA $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/listfile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/move $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/userinfo $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/copydir $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/copy $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/statfile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/

install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/htaccess-example $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/*.php $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/quota/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/quota/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/no-mail/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/no-mail/

%post
rm %{prefix}/%{name}-%{version}/webbin/quota
echo "README is located at %{prefix}/doc/%{name}-%{version}";
echo "Do the following:";
echo "rm %{prefix}/%{name}";
echo "ln -s %{prefix}/%{name}-%{version} %{prefix}/%{name}";
echo "ln -s /usr/bin/chmod %{prefix}/%{name}/webbin/chmod";
echo "ln -s /usr/bin/find %{prefix}/%{name}/webbin/find";
echo "ln -s /usr/bin/mkdir %{prefix}/%{name}/webbin/mkdir";
echo "ln -s /usr/sbin/quota %{prefix}/%{name}/webbin/quota";
echo "ln -s /usr/bin/touch %{prefix}/%{name}/webbin/touch";
echo "chgrp -h www %{prefix}/%{name}";
echo "chgrp -h www %{prefix}/%{name}/webbin/chmod";
echo "chgrp -h www %{prefix}/%{name}/webbin/find";
echo "chgrp -h www %{prefix}/%{name}/webbin/mkdir";
echo "chgrp -h www %{prefix}/%{name}/webbin/quota";
echo "chgrp -h www %{prefix}/%{name}/webbin/touch";
echo "READ the README!!";
echo
echo "Changing permissions on html/no-mail"
chmod 0000 %{prefix}/%{name}-%{version}/html/no-mail

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, www)
%dir %{prefix}/%{name}-%{version}
%dir %{prefix}/%{name}-%{version}/html
%dir %{prefix}/%{name}-%{version}/etc
%dir %attr(710,root,www)%{prefix}/%{name}-%{version}/bin
%dir %attr(511,root,www)%{prefix}/%{name}-%{version}/webbin

%defattr(-, root, www)
%doc README
%{prefix}/%{name}-%{version}/html/*
%{prefix}/%{name}-%{version}/etc/*
%{prefix}/%{name}-%{version}/bin/*
%{prefix}/%{name}-%{version}/webbin/*


%changelog
* Tue Aug 4 2009 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 0.8-11
- Updated tarball and added check-criteria to requires.
