%include perl-header.spec

Summary: Simple Network Management Protocol applications
Name: cmu-snmpapps
Version: 1.4d3
Release: 2
Group: Applications/Internet
License: BSD-type
Source: cmu-snmpapps-V1.4.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: cmu-snmp >= 1.14
BuildRequires: perl

%description
The snmpapps are snmpdelta, snmpget, snmpgetnext, snmpset, snmpstatus,
snmptest, snmptranslate, snmptrap, snmptrap2, snmptrapd and snmpwalk.

%prep
%setup -q -n snmpapps

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
 LDFLAGS="-L/usr/local/lib -R/usr/local/lib" CC="gcc -I/usr/local/include" \
 ./configure
make

%install
rm -rf $RPM_BUILD_ROOT
for i in usr/local/bin usr/local/man/man1 ; do
    mkdir -p $RPM_BUILD_ROOT/$i
done

PROGS="snmpstatus snmpget snmpwalk snmptranslate snmpgetnext snmptrap \
       snmptest snmptrapd snmptrap2 snmpdelta snmpset"

%{perl_binary} make-manpages.pl $PROGS

for i in $PROGS ; do
    install -c -m 755 -s $i $RPM_BUILD_ROOT/usr/local/bin
    install -c -m 644 $i.1 $RPM_BUILD_ROOT/usr/local/man/man1
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
%doc README TODO
/usr/local/bin/*
/usr/local/man/man1/*


