%include perl-header.spec

Summary:	Perl interface to the UNIX syslog(3) calls 
Name: 		perl-module-Sys-Syslog
Version: 	0.25
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL/Artistic
Source: 	Sys-Syslog-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
Sys::Syslog is an interface to the UNIX syslog(3) program.
Call syslog() with a string priority and a list of printf() 
args just like syslog(3).

%prep
%setup -q -n Sys-Syslog-%{version}

%build
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib"
export PATH CC CXX CPPFLAGS LD LDFLAGS
perl Makefile.PL
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}

# The contents of perllocal.pod are supposed to be appended to 
# an existing file, but rpm will try to replace the existing file, 
# causing a conflict.
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README
%{global_perl_arch}/Sys/Syslog.pm
%{global_perl_arch}/auto/Sys/Syslog/.packlist
%{global_perl_arch}/auto/Sys/Syslog/Syslog.bs
%{global_perl_arch}/auto/Sys/Syslog/Syslog.so
%{perl_prefix}/man/man3/*.3

%changelog
* Fri Jun 06 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.25-1
- Initial build

