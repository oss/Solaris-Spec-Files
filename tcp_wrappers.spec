Summary: Tcp-wrappers security tool
Name: tcp_wrappers
Version: 7.6
Release: 4ru
License: Freely distributable
Group: Applications/Internet
Source: tcp_wrappers_7.6.tar.gz
BuildRoot: /var/tmp/%{name}-root

%description
Tcp-wrappers is a tool that lets you monitor and filter requests for
network services.

%prep
%setup -q -n tcp_wrappers_7.6

%build
sed "s/\#STYLE/STYLE/" Makefile > Makefile2
mv Makefile2 Makefile

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
