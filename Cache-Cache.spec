%include perl-header.spec

Summary: The Cache modules are designed to assist a developer in persisting data for a specified period of time.

Name: perl-module-Cache-Cache
Version: 0.09
Release: 3
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Cache-Cache-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl = %{perl_version}
BuildRequires: perl = %{perl_version}

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

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
%{clean_common_files}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Cache/*
%{site_perl_arch}/auto/Cache/Cache
%{perl_prefix}/man/man3/*
