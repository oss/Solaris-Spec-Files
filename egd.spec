%include perl-header.spec

Summary: Entropy Gathering Daemon
Name: egd
Version: 0.8
Release: 4
Group: System Environment/Base
Copyright: GPL
Source: egd-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-root
Requires: perl-module-Digest-MD5
Requires: perl
BuildRequires: perl
BuildRequires: perl-module-Digest-MD5

%description
This is a standalone daemon that sits around running various
statistics collection programs (ps, vmstat, iostat, etc). It hashes
the results into an "entropy pool". If things happen on your system at
relatively random and unpredictable times, then some of that
randomness will become a part of the entropy pool and can be used to
generate random numbers. It is basically a user-space implementation
of the Linux kernel /dev/random device. As such, it should be runnable
on all unix-like systems. It is intended to make up for the lack of
/dev/random on non-Linux systems so that programs like GPG can be used
safely. [ from README ]

%prep
%setup -q

%build
perl Makefile.PL
make
make check

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{perl_prefix}
%{pmake_install}

%post
ln -s %{perl_prefix}/bin/egd.pl /usr/local/bin/egd.pl

%preun
rm -f /usr/local/bin/egd.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,bin,bin)
%doc COPYING README
%{perl_prefix}/bin/egd.pl
