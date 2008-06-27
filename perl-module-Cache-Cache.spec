%include perl-header.spec

Summary: The Cache modules are designed to assist a developer in persisting data for a specified period of time.

Name: perl-module-Cache-Cache
Version: 1.05
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Cache-Cache-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}, perl-module-IPC-ShareLite
BuildRequires: perl = %{perl_version}, perl-module-IPC-ShareLite

%description
The Cache modules are designed to assist a developer in persisting data for a specified period of time.  Often these modules are used
in web applications to store data locally to save repeated and
redundant expensive calls to remote machines or databases.  People
have also been known to use Cache::Cache for its straightforward
interface in sharing data between runs of an application or
invocations of a CGI-style script or simply as an easy to use
abstraction of the filesystem or shared memory.

The Cache package provides Cache::Cache, a generic interface
for creating persistent data stores.  This interface is implemented
by the Cache::MemoryCache, Cache::SharedMemoryCache, Cache::FileCache, 
Cache::SizeAwareFileCache, Cache::SizeAwareMemoryCache, and 
Cache::SizeAwareSharedMemoryCache classes. 

This work aggregates and extends the obsolete File::Cache and
IPC::Cache projects.

%prep

%setup -q -n Cache-Cache-%{version}

%build
perl Makefile.PL
make
make test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{perl_prefix}
%{pmake_install}
rm -f %{buildroot}%{global_perl_arch}/perllocal.pod

%clean
rm -rf %{buildroot}

%files
%defattr(-,bin,bin)
%doc README CHANGES
%{site_perl}/Cache/*
%{site_perl_arch}/auto/Cache/Cache
%{perl_prefix}/man/man3/*

%changelog
* Fri Jun 27 2008 Brian Schubert <schubert@nbcs.rutgers.edu> - 1.05-1
- Fixed spec file name, added changelog, and updated to version 1.05
