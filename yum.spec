Summary:	Yellowdog Updater, Modified
Name:		yum
Version:	3.2.5
Release:	3
Copyright:	GPL
Group:		Applications/Internet
Source:		http://linux.duke.edu/projects/yum/download/3.2/%{name}-%{version}.tar.gz
URL:		http://linux.duke.edu/projects/yum/index.ptml
Patch:		yum-3.2.5-makefile.patch
Distribution:	RU-Solaris
Vendor:		NBCS-OSS
Packager:	David Lee Halik <dhalik@nbcs.rutgers.edu>
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	python >= 2.4
BuildArch:	sparc64

%description
Yum is an automatic updater and package installer/remover for rpm systems. 
It automatically computes dependencies and figures out what things should 
occur to install packages. It makes it easier to maintain groups of 
machines without having to manually update each one using rpm. 

%prep
%setup -q
%patch -p1

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS

#./configure \
#	--prefix=/usr/local \
#	--disable-nls
gmake

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
gmake install DESTDIR=%{buildroot}
mv $RPM_BUILD_ROOT/usr/local/etc/yum/yum.conf $RPM_BUILD_ROOT/usr/local/etc/yum/yum.conf.example

%post
cat<<EOF
==============================================
After the installation it would be a good idea
to add log rotation and a cron to periodically
update the yum database. The conf file has been
installed as /usr/local/etc/yum/yum.conf.example
==============================================

EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/local/etc/yum/*
/usr/local/bin/*
/usr/local/share/man/man5/*
/usr/local/share/man/man8/*
/usr/local/etc/dbus-1/system.d/yum-updatesd.conf
/usr/local/etc/logrotate.d/yum
/usr/local/etc/rc.d/init.d/yum-updatesd
/usr/local/lib/python2.4/site-packages/yum/*
/usr/local/sbin/yum-updatesd
/usr/local/share/yum-cli/*
/usr/local/lib/python2.4/site-packages/rpmUtils/*

%changelog
* Thu Sep 27 2007 David Lee Halik <dhalik@nbcs.rutgers.edu> - 3.2.5-1
- Bump to 3.2.5
* Tue Jun 1 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.6-3
- Removed a few files from the package, added %post message
* Tue Apr 27 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.6-2
- Fixed NLS problems
* Tue Apr 27 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 2.0.6-1
- Upgrade to yum 2.0.6
* Fri Apr 23 2004 Leo Zhadanovsky <leozh@nbcs.rutgers.edu> - 1.0.3-1
- Initial package
