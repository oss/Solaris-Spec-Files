%define name webtools 
%define version 0.7
%define release 5
%define prefix /usr/local

Summary: Core binaries, configs and templates for many Rutgers specific web applications (aka webtools). By default comes with the quota webtool to allow a user to check their quota via the web. 
Name: %name
Version: %version
Release: %release
Copyright: GPL
Group: Services
Source0: %{name}-%{version}.tar.gz 
BuildRoot: %{_tmppath}/%{name}-root

%description
Core binaries, configs and templates for many Rutgers specific web applications (aka webtools). By default comes with the quota webtool to allow a user to check their quota via the web. 

%prep
%setup -n %{name}-%{version}

%build
cd src/
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -m 0755 -p $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/images
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/quota
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/no-mail
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/etc
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/bin
mkdir -m 0755 $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin


install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/etc/index.php $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/etc/index.php-example
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/etc/cfg.php $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/etc/cfg.php-example
install -c -m 4510 $RPM_BUILD_DIR/%{name}-%{version}/src/runas $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/bin
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/makefile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/readfile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/removefile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/appendfile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/linkfile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0511 $RPM_BUILD_DIR/%{name}-%{version}/src/listfile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/movefile $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0555 $RPM_BUILD_DIR/%{name}-%{version}/src/userinfo $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/htaccess-example $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/*.php $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/*.css $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/
install -c -m 0444 $RPM_BUILD_DIR/%{name}-%{version}/html/images/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/images/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/quota/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/quota/
install -c -m 0644 $RPM_BUILD_DIR/%{name}-%{version}/html/no-mail/* $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/html/no-mail/


cd $RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT%{prefix}/%{name}-%{version}/webbin/quota

%post
rm %{prefix}/%{name}-%{version}/webbin/quota
echo "README is located at %{prefix}/doc/%{name}-%{version}";
echo "Do the following:";
echo "rm %{prefix}/%{name}";
echo "ln -s %{prefix}/%{name}-%{version} %{prefix}/%{name}";
echo "ln -s /usr/sbin/quota %{prefix}/%{name}/webbin/quota";
echo "chgrp -h www %{prefix}/%{name}";
echo "chgrp -h www %{prefix}/%{name}/webbin/quota";
echo "READ the README!!";

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
