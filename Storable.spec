%include perl-header.spec

Summary: The Storable extension brings persistency to your data.

Name: perl-module-Storable
Version: 2.13
Release: 2
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
PATH="/opt/SUNWspro/bin:${PATH}" \
CC="cc" CXX="CC" CPPFLAGS="-I/usr/local/include" \
LD="/usr/ccs/bin/ld" \
LDFLAGS="-L/usr/local/lib -R/usr/local/lib" 
export PATH CC CXX CPPFLAGS LD LDFLAGS
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
%doc README ChangeLog
%{global_perl_arch}/*
#%{global_perl_arch}/auto/Storable
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/Storable.pm
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/.packlist
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/CAN_FLOCK.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/Storable.bs
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/Storable.so
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/_freeze.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/_retrieve.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/_store.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/_store_fd.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/autosplit.ix
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/fd_retrieve.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/freeze.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/lock_nstore.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/lock_retrieve.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/lock_store.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/logcarp.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/logcroak.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/nfreeze.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/nstore.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/nstore_fd.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/read_magic.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/retrieve.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/show_file_magic.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/store.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/store_fd.al
/usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto/Storable/thaw.al


%changelog
* Tue Jul 31 2007 Naveen Gavini <ngavini@nbcs.rutgers.edu> - 1.4.5-2
- Respun.

