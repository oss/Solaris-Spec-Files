%include perl-header.spec

Summary:		SNMP library
Name: 			SNMP_Session
Version: 		0.92
Release:		0ru
Copyright: 		GPL
Group: 			Libraries/Perl
Source: 		ftp://ftp.switch.ch/software/sources/network/snmp/perl/SNMP_Session-0.92.tar.gz
#Patch:			rrdtool-rrdtutorial.pod.patch
Buildroot: 		/var/tmp/rrdtool-root
Prefix:	 		%{_prefix}
#BuildRequires:	tcl
Url: 			http://www.caida.org/Tools/RRDtool/
Vendor: 		Tobi Oetiker <oetiker@ee.ethz.ch>

%description
SNMP libraries for Perl

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{site_perl_arch}/
cp lib/BER.pm lib/SNMP_Session.pm lib/SNMP_util.pm $RPM_BUILD_ROOT/%{site_perl_arch}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,bin)
%{site_perl_arch}/*