Summary:      virtual package
Name: 	      vpkg-filesystem-rutgers
Version:      0.1
Release:      8
Group: 	      ---
License:      ---
Distribution: RU-Solaris
Vendor:       NBCS-OSS
Packager:     Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu>

Provides:     /
Provides:     /usr
Provides:     /usr/local
Provides:     /usr/local/bin
#Provides:     /usr/local/bin/sparcv9
# bash-2.05$ rpm -q --whatprovides /usr/local/bin/sparcv9
# gcc-3.4.5-4.sparc64
# ^ should not
Provides:     /usr/local/doc
Provides:     /usr/local/etc
Provides:     /usr/local/include
Provides:     /usr/local/info
Provides:     /usr/local/lib
Provides:     /usr/local/lib/sparcv9
Provides:     /usr/local/man
Provides:     /usr/local/man/fr
Provides:     /usr/local/man/fr/man1
Provides:     /usr/local/man/fr/man5
Provides:     /usr/local/man/man1
Provides:     /usr/local/man/man3
Provides:     /usr/local/man/man4
Provides:     /usr/local/man/man5
Provides:     /usr/local/man/man7
Provides:     /usr/local/man/man8
Provides:     /usr/local/share
Provides:     /usr/local/src
Provides:     /usr/perl5
Provides:     /usr/perl5/man
Provides:     /usr/perl5/man/man3
Provides:     /usr/perl5/site_perl
Provides:     /usr/perl5/site_perl/5.6.1
Provides:     /usr/perl5/site_perl/5.6.1/sun4-solaris-64int
Provides:     /usr/perl5/site_perl/5.6.1/sun4-solaris-64int/auto
Provides:     /var
Provides:     /var/local
Provides:     /var/local/lib

# get rid of these when their respective packages get rebuilt
Provides:     /usr/local/share/file

# dernyi: for terminals
Provides:     /usr/share/lib/terminfo
Provides:     /usr/share/lib/terminfo/1
Provides:     /usr/share/lib/terminfo/2
Provides:     /usr/share/lib/terminfo/3
Provides:     /usr/share/lib/terminfo/4
Provides:     /usr/share/lib/terminfo/5
Provides:     /usr/share/lib/terminfo/6
Provides:     /usr/share/lib/terminfo/7
Provides:     /usr/share/lib/terminfo/8
Provides:     /usr/share/lib/terminfo/9
Provides:     /usr/share/lib/terminfo/A
Provides:     /usr/share/lib/terminfo/B
Provides:     /usr/share/lib/terminfo/H
Provides:     /usr/share/lib/terminfo/M
Provides:     /usr/share/lib/terminfo/P
Provides:     /usr/share/lib/terminfo/S
Provides:     /usr/share/lib/terminfo/a
Provides:     /usr/share/lib/terminfo/b
Provides:     /usr/share/lib/terminfo/c
Provides:     /usr/share/lib/terminfo/d
Provides:     /usr/share/lib/terminfo/e
Provides:     /usr/share/lib/terminfo/f
Provides:     /usr/share/lib/terminfo/g
Provides:     /usr/share/lib/terminfo/h
Provides:     /usr/share/lib/terminfo/i
Provides:     /usr/share/lib/terminfo/j
Provides:     /usr/share/lib/terminfo/k
Provides:     /usr/share/lib/terminfo/l
Provides:     /usr/share/lib/terminfo/m
Provides:     /usr/share/lib/terminfo/n
Provides:     /usr/share/lib/terminfo/o
Provides:     /usr/share/lib/terminfo/p
Provides:     /usr/share/lib/terminfo/q
Provides:     /usr/share/lib/terminfo/r
Provides:     /usr/share/lib/terminfo/s
Provides:     /usr/share/lib/terminfo/t
Provides:     /usr/share/lib/terminfo/u
Provides:     /usr/share/lib/terminfo/v
Provides:     /usr/share/lib/terminfo/w
Provides:     /usr/share/lib/terminfo/x
Provides:     /usr/share/lib/terminfo/y
Provides:     /usr/share/lib/terminfo/z

# Test wildcards

%description
As of rpm 4.4.6, orphaned directories are not allowed. This means every
directory used has to be owned by some package. This package will own
those directories that we assume to be on the system, into which, we install
our files.

%prep
# nothing to do

%build
# nothing to do

%install
# nothing to do

%clean
# nothing to do

%files

%changelog
* Fri Jun 23 2006 Jonathan Kaczynski <jmkacz@nbcs.rutgers.edu> - 0.1-1
- Initial package
