%include perl-header.spec

Summary: 	Lightweight interface to shared memory
Name: 		perl-module-IPC-ShareLite
Version: 	0.13
Release: 	1
Group: 		System Environment/Base
Copyright: 	GPL/Artistic
Source: 	IPC-ShareLite-%{version}.tar.gz
BuildRoot: 	/var/tmp/%{name}-root
Requires: 	perl = %{perl_version}
BuildRequires: 	perl = %{perl_version}

%description
IPC::ShareLite provides a simple interface to shared memory, allowing 
data to be efficiently communicated between processes. Your operating 
system must support SysV IPC (shared memory and semaphores) in order 
to use this module.

IPC::ShareLite provides an abstraction of the shared memory and 
semaphore facilities of SysV IPC, allowing the storage of arbitrarily 
large data; the module automatically acquires and removes shared 
memory segments as needed. Storage and retrieval of data is atomic, 
and locking functions are provided for higher-level synchronization.

%prep
%setup -q -n IPC-ShareLite-%{version}

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
%doc Changes
%{site_perl_arch}/IPC/ShareLite.pm
%{site_perl_arch}/auto/IPC/ShareLite/*
%{site_perl_arch}/auto/IPC/ShareLite/.packlist
%{perl_prefix}/man/man3/*.3

%changelog
* Fri Jun 06 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 0.13-1
- Initial build

