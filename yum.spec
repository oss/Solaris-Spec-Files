Summary: Yellowdog Updater, Modified
Name: yum
Version: 1.0.3
Release: 1
Copyright: GPL
Group: Applications/Internet
Source: http://linux.duke.edu/projects/yum/download/1.0/yum-1.0.3.tar.gz
URL: http://linux.duke.edu/projects/yum/index.ptml
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: python >= 2.2.1

%description
Yum is an automatic updater and package installer/remover for rpm systems. 
It automatically computes dependencies and figures out what things should 
occur to install packages. It makes it easier to maintain groups of 
machines without having to manually update each one using rpm. 

%prep
%setup -q

%build
CC="gcc" ./configure --prefix=/usr/local
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}
mv $RPM_BUILD_ROOT/etc/yum.conf $RPM_BUILD_ROOT/etc/yum.conf.example

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/cron.daily/yum.cron
/etc/init.d/yum
/etc/logrotate.d/yum
/etc/yum.conf.example
/usr/local/bin/*
/usr/local/man/man5/*
/usr/local/man/man8/*
/usr/local/share/yum/*

%changelog
* Fri Apr 23 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.3-1
- Initial package
