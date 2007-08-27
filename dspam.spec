Summary: Anti-Spam Solution.
URL: http://dspam.nuclearelephant.org
%define ver     3.8.0
%define name    dspam
%define rel     2
Name: %{name}
Version: %{ver}
Release: %{rel}
License: GPL
Group: System Environment/Daemons
Distribution: RU-Solaris
Vendor: NBCS-OSS
Packager:       Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu>
Source0: %{name}-%{ver}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
%define bindir 	/usr/local/bin
%define mandir  /usr/local/man
%define includedir	/usr/local/include
%define libdir	/usr/local/lib


%description
DSPAM (as in De-Spam) is an open-source project to create a new kind of
anti-spam mechanism, and is currently effective as both a server-side agent
for UNIX email servers and a developer's library for mail clients, other
anti-spam tools, and similar projects requiring drop-in spam filtering.

The DSPAM agent masquerades as the email server's local delivery agent and
filters/learns spams using an advanced Bayesian statistical approach (based on
Baye's theorem of combined probabilities) which provides an administratively
maintenance-free, easy-learning Anti-Spam service custom tailored to each
individual user's behavior. Advanced because on top of standard Bayesian
filtering is also incorporated the use of Chained Tokens, de-obfuscation, and
other enhancements. DSPAM works great with Sendmail and Exim, and should work
well with any other MTA that supports an external local delivery agent
(postfix, qmail, etc.)

%prep
%setup -q 

%build

./configure --prefix=/usr/local --enable-daemon --with-storage-driver=hash_drv --enable-clamav --enable-virtual-users

%install
make 
make install DESTDIR=$RPM_BUILD_ROOT

echo done

%post
chkconfig --add dspam

%clean
test "x$RPM_BUILD_ROOT" != "x/" && rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT

%files
%doc README LICENSE CHANGELOG doc
%config(noreplace) /usr/local/etc/dspam.conf
%{_bindir}/cssclean
%{_bindir}/csscompress
%{_bindir}/cssconvert
%{_bindir}/cssstat
%{_bindir}/dspam
%{_bindir}/dspam_2sql
%{_bindir}/dspam_admin
%{_bindir}/dspam_clean
#%{_bindir}/dspam_corpus
%{_bindir}/dspam_train
%{_bindir}/dspam_crc
%{_bindir}/dspam_dump
#%{_bindir}/dspam_genaliases
%{_bindir}/dspam_logrotate
%{_bindir}/dspam_merge
%{_bindir}/dspam_stats
%{_bindir}/dspamc
%{_includedir}/dspam/buffer.h
%{_includedir}/dspam/config.h
%{_includedir}/dspam/config_shared.h
%{_includedir}/dspam/decode.h
%{_includedir}/dspam/diction.h
%{_includedir}/dspam/error.h
%{_includedir}/dspam/heap.h
%{_includedir}/dspam/libdspam.h
%{_includedir}/dspam/libdspam_objects.h
%{_includedir}/dspam/ldap_client.h
%{_includedir}/dspam/nodetree.h
%{_includedir}/dspam/storage_driver.h
%{_includedir}/dspam/tokenizer.h
%{_libdir}/libdspam.a
%{_libdir}/libdspam.la
%{_libdir}/libdspam.so
%{_libdir}/libdspam.so.7
%{_libdir}/libdspam.so.7.0.0
%{_libdir}/pkgconfig/dspam.pc
%{_mandir}/man1/*
%{_prefix}/var/dspam

%changelog
* Mon Aug 27 2007 Kevin Mulvey <kmulvey at nbcs dot rutgers dot edu> - 3.8.0-1
 - Initial build
