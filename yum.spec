Summary: Yellowdog Updater, Modified
Name: yum
Version: 2.0.6
Release: 4
Copyright: GPL
Group: Applications/Internet
Source: http://linux.duke.edu/projects/yum/download/2.0/yum-2.0.6.tar.gz
URL: http://linux.duke.edu/projects/yum/index.ptml
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager: Leonid Zhadanovsky <leozh@nbcs.rutgers.edu>
BuildRoot: %{_tmppath}/%{name}-root
Requires: python >= 2.2.1, rpm = 4.3

%description
Yum is an automatic updater and package installer/remover for rpm systems. 
It automatically computes dependencies and figures out what things should 
occur to install packages. It makes it easier to maintain groups of 
machines without having to manually update each one using rpm. 

%prep
%setup -q

%build
CC="gcc" ./configure --prefix=/usr/local --disable-nls
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
make install DESTDIR=%{buildroot}
mv $RPM_BUILD_ROOT/etc/yum.conf $RPM_BUILD_ROOT/etc/yum.conf.example

%post
echo Now that Yum has been installed, now setup log rotation in accordance to your system and also add a cron task to do yum -update periodically.

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/yum.conf.example
/etc/init.d/yum
/usr/local/bin/*
/usr/local/man/man5/*
/usr/local/man/man8/*
/usr/local/share/yum/*
/usr/local/share/locale/*

%changelog
* Tue Jun 1 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.6-3
- Removed a few files from the packaged, added %post message

* Tue Apr 27 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.6-2
- Fixed NLS problems

* Tue Apr 27 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.6-1
- Upgrade to yum 2.0.6

* Fri Apr 23 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.3-1
- Initial package
