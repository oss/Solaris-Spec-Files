%include perl-header.spec

Summary: The Storable extension brings persistency to your data.

Name: perl-module-Storable
Version: 2.07
Release: 1
Group: System Environment/Base
Copyright: GPL/Artistic
Source: Storable-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl
BuildRequires: perl

%description
Note -- This is replaced in Perl 5.8, so don't install both this and perl 5.8.  You have been warned.

You may recursively store to disk any data structure, no matter how
complex and circular it is, provided it contains only SCALAR, ARRAY,
HASH (possibly tied) and references (possibly blessed) to those items.

At a later stage, or in another program, you may retrieve data from
the stored file and recreate the same hiearchy in memory. If you
had blessed references, the retrieved references are blessed into
the same package, so you must make sure you have access to the
same perl class than the one used to create the relevant objects.

There is also a dclone() routine which performs an optimized mirroring
of any data structure, preserving its topology.

Objects (blessed references) may also redefine the way storage and
retrieval is performed, and/or what deep cloning should do on those
objects.

%prep

%setup -q -n Storable-%{version}

%build
perl Makefile.PL
make


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}
#%{clean_common_files}
rm -f `/usr/local/gnu/bin/find $RPM_BUILD_ROOT -iname perllocal.pod`
rm -f $RPM_BUILD_ROOT/%{global_perl_arch}/perllocal.pod


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc README ChangeLog
%{global_perl_arch}/Storable.pm
%{global_perl_arch}/auto/Storable
