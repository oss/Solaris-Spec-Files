%include machine-header.spec
Summary: Tcp-wrappers security tool
Name: tcp_wrappers
Version: 7.6
Release: 5ru
License: Freely distributable
Group: Applications/Internet
Source: tcp_wrappers_7.6.tar.gz
Patch: tcp_wrappers_fix_sys_errlist.patch
BuildRoot: /var/tmp/%{name}-root

%description
Tcp-wrappers is a tool that lets you monitor and filter requests for
network services.

%prep
%setup -q -n tcp_wrappers_7.6
%patch -p 1

%build
sed "s/\#STYLE/STYLE/" Makefile > Makefile2
mv Makefile2 Makefile

%ifarch == sparc64
mkdir -p sparcv9/lib
mkdir -p sparcv9/bin
make CC=/usr/local/gcc3/bin/sparcv9-sun-%{sol_os}-gcc \
REAL_DAEMON_DIR=/usr/local/sbin/sparcv9 sunos5
mv libwrap.a sparcv9/lib
for i in safe_finger tcpd tcpdchk tcpdmatch try-from ; do
    mv $i sparcv9/bin
done
make clean
%endif

make CC=gcc REAL_DAEMON_DIR=/usr/local/sbin sunos5

%install
rm -rf $RPM_BUILD_ROOT
for i in 3 5 8 ; do
    mkdir -p $RPM_BUILD_ROOT/usr/local/man/man$i
done
for i in 3 5 8 ; do
    for j in *.$i ; do
        install -m 0644 $j $RPM_BUILD_ROOT/usr/local/man/man$i/$j
    done
done

mkdir $RPM_BUILD_ROOT/usr/local/sbin
for i in safe_finger tcpd tcpdchk tcpdmatch try-from ; do
    install -m 0511 $i $RPM_BUILD_ROOT/usr/local/sbin/
done

mkdir $RPM_BUILD_ROOT/usr/local/lib
install -m 0644 libwrap.a $RPM_BUILD_ROOT/usr/local/lib/libwrap.a

mkdir $RPM_BUILD_ROOT/usr/local/include
install -m 0644 tcpd.h $RPM_BUILD_ROOT/usr/local/include/tcpd.h

%ifarch == sparc64
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin/sparcv9
install -m 0511 sparcv9/bin/* $RPM_BUILD_ROOT/usr/local/sbin/sparcv9

mkdir -p $RPM_BUILD_ROOT/usr/local/lib/sparcv9
install -m 0644 sparcv9/lib/* $RPM_BUILD_ROOT/usr/local/lib/sparcv9
%endif3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
/usr/local/man/man3/*
/usr/local/man/man5/*
/usr/local/man/man8/*
/usr/local/sbin/*
/usr/local/lib/*
/usr/local/include/*
%ifarch == sparc64
/usr/local/lib/sparcv9/*
/usr/local/sbin/sparcv9/*
%endif
