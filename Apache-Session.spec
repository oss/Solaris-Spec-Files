%include perl-header.spec

Summary: Apache-Session A persistence framework for session data

Name: perl-module-Apache-Session
Version: 1.54
Release: 2
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Apache-Session-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
Apache::Session is a persistence framework which is particularly useful for tracking session 
data between httpd requests. Apache::Session is designed to work with Apache and mod_perl, 
but it should work under CGI and other web servers, and it also works outside of a web server 
altogether.

Apache::Session consists of five components: the interface, the object store, the lock 
manager, the ID generator, and the serializer. The interface is defined in Session.pm, which 
is meant to be easily subclassed. The object store can be the filesystem, a Berkeley DB, a 
MySQL DB, an Oracle DB, or a Postgres DB. Locking is done by lock files, semaphores, or the 
locking capabilities of MySQL and Postgres. Serialization is done via Storable, and 
optionally ASCII-fied via MIME or pack(). ID numbers are generated via MD5. The reader is 
encouraged to extend these capabilities to meet his own requirements.

A derived class of Apache::Session is used to tie together the three components. The derived 
class inherits the interface from Apache::Session, and specifies which store and locker 
classes to use. Apache::Session::MySQL, for instance, uses the MySQL storage class and also 
the MySQL locking class. You can easily plug in your own object store or locker class. 

%prep

%setup -q -n Apache-Session-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README Changes
%{site_perl}/Apache/Session.pm
%{site_perl}/Apache/Session
%{site_perl_arch}/auto/Apache/Session
%{perl_prefix}/man/man3/*
