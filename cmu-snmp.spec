%include perl-header.spec

Summary: CMU Simple Network Management Protocol library
Name: cmu-snmp
Version: 1.14
Release: 2
Group: System Environment/Libraries
License: BSD-type
Source: cmu-snmp-V1.14.tar.gz
Patch: cmu-snmp.patch
BuildRoot: /var/tmp/%{name}-root
BuildRequires: fileutils
BuildRequires: perl

%description
CMU Simple Network Management Protocol Library, supports SNMPv1 and
SNMPv2 User.

%prep
%setup -q -n snmp
%patch -p1

%build
LD="/usr/ccs/bin/ld -L/usr/local/lib -R/usr/local/lib" \
  LDFLAGS="-L/usr/local/lib -R/usr/local/lib" \
  INSTALL="/usr/local/gnu/bin/install" ./configure \
  --prefix=/usr/local --sysconfdir=/etc
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/include/snmp

HEADER_FILES="asn1.h mib.h parse.h snmp.h snmp_dump.h snmp_extra.h \
   snmp_api.h snmp_api_util.h snmp_client.h snmp_impl.h snmp_pdu.h \
   snmp_vars.h snmp_error.h snmp_session.h snmp_api_error.h snmp-internal.h \
   snmp_msg.h mibii.h snmp_coexist.h mib.h version.h mini-client.h \
   snmp_compat.h"

for i in $HEADER_FILES ; do
    install -c -m 644 $i $RPM_BUILD_ROOT/usr/local/include/snmp
done

%{perl_binary} ./snmp-man.pl -create
for i in /usr/local/man/man3 /usr/local/man/man5 ; do
    mkdir -p $RPM_BUILD_ROOT/$i
done
%{perl_binary} ./snmp-man.pl -install \
    "/usr/local/gnu/bin/install -c -m 644" $RPM_BUILD_ROOT/usr/local/man

mkdir $RPM_BUILD_ROOT/etc
install -c -m 644 mib-v2.txt $RPM_BUILD_ROOT/etc

mkdir $RPM_BUILD_ROOT/usr/local/lib

./libtool install -c -m 755 libsnmp.la \
   $RPM_BUILD_ROOT/usr/local/lib

ar crv libsnmp.a mibii.o snmp_error.o snmp_extra.o snmp_dump.o asn1.o \
   coexistance.o snmp_msg.o snmp_pdu.o snmp_vars.o snmp_api_error.o \
   snmp_client.o snmp_api.o mini-client.o mib.o parse.o new-parse.o \
   version.o snmp_api_util.o

ranlib libsnmp.a

./libtool install -c -m 755 libsnmp.a \
   $RPM_BUILD_ROOT/usr/local/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,other)
%doc README TODO 
/usr/local/man/man3/*
/usr/local/man/man5/*
/usr/local/lib/*
/usr/local/include/snmp
/etc/mib-v2.txt
